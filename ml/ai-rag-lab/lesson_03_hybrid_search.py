
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

documents = [
    {
        "id": 1,
        "title": "Introduction to Thermodynamics",
        "content": "Thermodynamics studies heat, temperature, energy, and work."
    },
    {
        "id": 2,
        "title": "Database Management Systems",
        "content": "Database systems organize data using tables, SQL, and relationships."
    },
    {
        "id": 3,
        "title": "Heat Transfer Fundamentals",
        "content": "Heat transfer explains how thermal energy moves between objects."
    },
    {
        "id": 4,
        "title": "Introduction to Machine Learning",
        "content": "Machine learning uses data to learn patterns and make predictions."
    },
]

# Prepare document text for keyword retrieval.
texts = [
    f"{doc['title']}. {doc['content']}"
    for doc in documents
]

# 1. Build the TF-IDF index.
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# 2. Build the semantic index.
model = SentenceTransformer("all-MiniLM-L6-v2")
embedding_matrix = model.encode(
    texts,
    normalize_embeddings=True
)


def rank_by_score(scores):
    """Return document indexes, best first."""
    return scores.argsort()[::-1]


def hybrid_search(query, top_k=2, rrf_k=10):
    # Keyword scores.
    query_tfidf = vectorizer.transform([query])
    keyword_scores = cosine_similarity(
        query_tfidf, tfidf_matrix
    )[0]

    # Semantic scores.
    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )
    semantic_scores = cosine_similarity(
        query_embedding, embedding_matrix
    )[0]

    # Keep only positive keyword matches.
    keyword_ranking = [
        i for i in rank_by_score(keyword_scores)
        if keyword_scores[i] > 0
    ]

    # Semantic retrieval ranks all documents.
    semantic_ranking = list(
        rank_by_score(semantic_scores)
    )

    # Combine rankings using Reciprocal Rank Fusion.
    fused_scores = {}

    for ranking in (keyword_ranking, semantic_ranking):
        for rank, doc_index in enumerate(ranking, start=1):
            contribution = 1 / (rrf_k + rank)
            fused_scores[doc_index] = (
                fused_scores.get(doc_index, 0) + contribution
            )

    # Sort by the combined score.
    ranked_results = sorted(
        fused_scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    results = []

    for doc_index, fused_score in ranked_results[:top_k]:
        results.append({
            "id": documents[doc_index]["id"],
            "title": documents[doc_index]["title"],
            "hybrid_score": fused_score,
            "keyword_score": float(keyword_scores[doc_index]),
            "semantic_score": float(semantic_scores[doc_index]),
        })

    return results


if __name__ == "__main__":
    query = "How does computer understands data?"

    for result in hybrid_search(query):
        print(
            f"{result['title']} | "
            f"Hybrid: {result['hybrid_score']:.4f} | "
            f"Keyword: {result['keyword_score']:.4f} | "
            f"Semantic: {result['semantic_score']:.4f}"
        )
