import fitz  # PyMuPDF
from src.segmenter import segment_document

# Use a sample file path from your actual structure
pdf_path = "collections/round_1b_001/South of France - History.pdf"
doc = fitz.open(pdf_path)

sections = segment_document(doc, "South of France - History.pdf")

for sec in sections:
    print("--------")
    print(f"📄 Doc: {sec.doc_name}")
    print(f"📄 Page: {sec.page}")
    print(f"🧠 Title: {sec.title}")
    print(f"📑 Text snippet: {sec.text[:150]}...")
