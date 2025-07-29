# src/main.py

import os
import sys
from src.loader import load_collection
from src.segmenter import segment_document
from src.ranker import rank_sections
from src.serializer import serialize_output


def run_pipeline(collection_path: str, output_dir: str = "outputs"):
    """
    Full Round 1B pipeline:
    1. Loads input PDFs and persona config
    2. Segments sections
    3. Ranks them by relevance
    4. Serializes final output
    """
    if not os.path.exists(collection_path):
        print(f"❌ Collection path not found: {collection_path}")
        return

    # Load config and PDFs
    config, docs = load_collection(collection_path)
    persona = config.get("persona", {})
    if not persona:
        print("❌ Persona data missing in input JSON.")
        return

    all_sections = []
    for doc_name, doc in docs:
        sections = segment_document(doc, doc_name)
        all_sections.extend(sections)

    if not all_sections:
        print("⚠️ No sections extracted from documents.")
        return

    # Rank sections based on persona
    ranked = rank_sections(all_sections, persona)

    # Serialize final output
    collection_name = os.path.basename(collection_path.rstrip("/\\"))
    input_doc_names = [name for name, _ in docs]

    serialize_output(
        output_path=output_dir,
        collection_name=collection_name,
        input_docs=input_doc_names,
        persona=persona,
        ranked_sections=ranked
    )


# Optional CLI usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/main.py collections/round_1b_001")
        sys.exit(1)

    run_pipeline(sys.argv[1])
