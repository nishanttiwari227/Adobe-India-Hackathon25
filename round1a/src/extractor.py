import sys
import os
import fitz  # PyMuPDF
from src.detector import detect_headings
from src.serializer import serialize_to_json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    pages = [page.get_text("dict") for page in doc]
    title, outline = detect_headings(pages)
    return serialize_to_json({"title": title, "outline": outline})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extractor.py <pdf_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    # derive output filename
    base = os.path.splitext(os.path.basename(pdf_path))[0]
    out_path = os.path.join("outputs", f"{base}.json")
    os.makedirs("outputs", exist_ok=True)

    result = extract_outline(pdf_path)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"✅ Extracted outline saved to {out_path}")
