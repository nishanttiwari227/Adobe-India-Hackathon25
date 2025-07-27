# batch_run.py
import os
import glob
from src.extractor import extract_outline

INPUT_DIR = "inputs"
OUTPUT_DIR = "outputs"

def batch_process():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pdf_files = glob.glob(os.path.join(INPUT_DIR, "*.pdf"))
    if not pdf_files:
        print(f"❌ No PDFs found in '{INPUT_DIR}'")
        return

    for pdf_path in pdf_files:
        base = os.path.splitext(os.path.basename(pdf_path))[0]
        out_path = os.path.join(OUTPUT_DIR, f"{base}.json")
        print(f"📄 Processing {pdf_path} → {out_path}")
        result = extract_outline(pdf_path)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(result)
    print("✅ All PDFs processed.")

if __name__ == "__main__":
    batch_process()
