
from pathlib import Path
import pymupdf

pdf_path = Path("LIS122.pdf")

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



