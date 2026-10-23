
import pymupdf
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


MODEL_NAME = "all-MiniLM-L6-v2"


def split_into_chunks(text, chunk_size=180, overlap=30):
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid chunk_size or overlap")

    words = text.split()
    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(words), step):
        chunk_words = words[start:start + chunk_size]

        if not chunk_words:
            break

        chunks.append(" ".join(chunk_words))

        if start + chunk_size >= len(words):
            break

    return chunks


class PDFHybridRetriever:
    def __init__(self, pdf_path, material_id, title, course_code):
        self.chunks = self._extract_chunks(
            pdf_path, material_id, title, course_code
        )

        if not self.chunks:
            raise ValueError(
                "No text chunks found. Check the PDF or use OCR "
                "if it contains scanned pages."
            )

        self.model = SentenceTransformer(MODEL_NAME)

        self.chunk_texts = [
            chunk["text"] for chunk in self.chunks
        ]

        # Build semantic index.
        self.chunk_embeddings = self.model.encode(
            self.chunk_texts,
            normalize_embeddings=True
        )

        # Build keyword index.
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(
            self.chunk_texts
        )

    @staticmethod
    def _extract_chunks(
        pdf_path, material_id, title, course_code
    ):
        chunks = []

        with pymupdf.open(pdf_path) as pdf:
            for page_index, page in enumerate(pdf):
                page_number = page_index + 1
                text = page.get_text("text", sort=True)

                for chunk_index, chunk_text in enumerate(
                    split_into_chunks(text)
                ):
                    chunks.append({
                        "material_id": material_id,
                        "title": title,
                        "course_code": course_code,
                        "page_number": page_number,
                        "chunk_index": chunk_index,
                        "text": chunk_text,
                    })

        return chunks

    def semantic_search(self, query, top_k=3):
        query_embedding = self.model.encode(
            [query],
            normalize_embeddings=True
        )

        scores = cosine_similarity(
            query_embedding, self.chunk_embeddings
        )[0]

        ranked_indices = scores.argsort()[::-1][:top_k]

        return [
            {
                **self.chunks[index],
                "score": float(scores[index]),
            }
            for index in ranked_indices
        ]

    def hybrid_search(self, query, top_k=3, rrf_k=60):
        # 1. Keyword ranking.
        query_tfidf = self.vectorizer.transform([query])

        keyword_scores = cosine_similarity(
            query_tfidf, self.tfidf_matrix
        )[0]

        keyword_ranking = [
            int(i)
            for i in keyword_scores.argsort()[::-1]
            if keyword_scores[i] > 0
        ]

        # 2. Semantic ranking.
        query_embedding = self.model.encode(
            [query],
            normalize_embeddings=True
        )

        semantic_scores = cosine_similarity(
            query_embedding, self.chunk_embeddings
        )[0]

        semantic_ranking = [
            int(i) for i in semantic_scores.argsort()[::-1]
        ]

        # 3. Reciprocal Rank Fusion.
        fused_scores = {}

        for ranking in (keyword_ranking, semantic_ranking):
            for rank, index in enumerate(ranking, start=1):
                contribution = 1 / (rrf_k + rank)

                fused_scores[index] = (
                    fused_scores.get(index, 0) + contribution
                )

        ranked = sorted(
            fused_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        # 4. Return ranked chunks with source metadata.
        results = []

        for index, hybrid_score in ranked[:top_k]:
            results.append({
                **self.chunks[index],
                "hybrid_score": float(hybrid_score),
                "keyword_score": float(keyword_scores[index]),
                "semantic_score": float(semantic_scores[index]),
            })

        return results


def main():
    retriever = PDFHybridRetriever(
        pdf_path="UNIT7.pdf",
        material_id=42,  # Example only
        title="Communication Media",
        course_code="215",  # Example only
    )

    query = "What are the standards in communication media?"
    # query = "What types of communication media are discussed?"

    print(f"Indexed chunks: {len(retriever.chunks)}")
    print(f"\nQuery: {query}\n")

    for result in retriever.hybrid_search(query, top_k=3):
        print(
            f"Page: {result['page_number']} | "
            f"Hybrid: {result['hybrid_score']:.4f} | "
            f"Keyword: {result['keyword_score']:.3f} | "
            f"Semantic: {result['semantic_score']:.3f}"
        )
        print(result["text"][:300])
        print("-" * 50)


if __name__ == "__main__":
    main()
