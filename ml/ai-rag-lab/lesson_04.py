
from pathlib import Path
import pymupdf

pdf_path = Path("UNIT7.pdf")

if not pdf_path.exists():
    raise FileNotFoundError(
        f"Could not find PDF: {pdf_path.resolve()}"
    )

with pymupdf.open(pdf_path) as pdf:
    print(f"Total pages: {len(pdf)}")

    for page_index, page in enumerate(pdf):
        # PDF page indexes start at zero.
        # Human-readable page numbers start at one.
        page_number = page_index + 1

        text = page.get_text("text", sort=True)

        print(f"\n--- Page {page_number} ---")
        print(text[:1000])

        if not text.strip():
            print("[No extractable text found on this page]")





def split_into_chunks(text, chunk_size=1000, overlap=150):
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be >= 0 and smaller than chunk_size"
        )

    # Remove leading and trailing whitespace.
    text = text.strip()

    if not text:
        return []

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

    return chunks




def split_into_chunks(text, chunk_size=180, overlap=30):
    """
    Split text into chunks measured in words.

    chunk_size: maximum words per chunk
    overlap: words repeated between consecutive chunks
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid overlap")

    words = text.split()

    if not words:
        return []

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(words), step):
        chunk_words = words[start:start + chunk_size]
        chunks.append(" ".join(chunk_words))

        if start + chunk_size >= len(words):
            break

    return chunks

def extract_pdf_chunks(
    pdf_path,
    material_id,
    title,
    course_code
):
    pdf_path = Path(pdf_path)

    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)

    all_chunks = []

    with pymupdf.open(pdf_path) as pdf:
        for page_index, page in enumerate(pdf):
            page_number = page_index + 1
            page_text = page.get_text("text", sort=True)

            if not page_text.strip():
                continue

            page_chunks = split_into_chunks(page_text)

            for chunk_index, chunk_text in enumerate(
                page_chunks
            ):
                all_chunks.append({
                    "material_id": material_id,
                    "title": title,
                    "course_code": course_code,
                    "page_number": page_number,
                    "chunk_index": chunk_index,
                    "text": chunk_text,
                })

    return all_chunks


if __name__ == "__main__":
    chunks = extract_pdf_chunks(
        pdf_path="UNIT7.pdf",
        material_id=42,
        title="Introduction to Physics",
        course_code="PHY101",
    )

    print(f"Total chunks created: {len(chunks)}")

    for chunk in chunks[:3]:
        print("\n--- CHUNK ---")
        print(f"Material ID: {chunk['material_id']}")
        print(f"Course: {chunk['course_code']}")
        print(f"Page: {chunk['page_number']}")
        print(f"Chunk index: {chunk['chunk_index']}")
        print(chunk["text"][:250])
