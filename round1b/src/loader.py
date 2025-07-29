import os
import json
import fitz  # PyMuPDF
from typing import List, Dict, Tuple

def load_collection(collection_path: str) -> Tuple[Dict, List[Tuple[str, fitz.Document]]]:
    """
    Loads input JSON and all PDFs from the specified collection folder.

    Args:
        collection_path (str): Path to folder like collections/round_1b_001

    Returns:
        Tuple of (config_dict, list of (filename, fitz.Document))
    """
    # Load challenge1b_input.json
    cfg_path = os.path.join(collection_path, "challenge1b_input.json")
    with open(cfg_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    # Load PDFs directly from the same collection folder
    docs = []
    for fname in sorted(os.listdir(collection_path)):
        if fname.lower().endswith(".pdf"):
            full_path = os.path.join(collection_path, fname)
            try:
                doc = fitz.open(full_path)
                docs.append((fname, doc))
            except Exception as e:
                print(f"⚠️ Skipping {fname}: {e}")

    return config, docs

# Optional CLI test
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python src/loader.py <collection_path>")
        sys.exit(1)

    cfg, docs = load_collection(sys.argv[1])
    print("✅ Loaded config:", cfg["challenge_info"])
    print("📄 Persona:", cfg["persona"])
    print(f"📚 Loaded {len(docs)} PDFs:")
    for name, _ in docs:
        print("   └─", name)
