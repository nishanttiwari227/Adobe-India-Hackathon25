# src/serializer.py

import json
import os
from datetime import datetime
from typing import List, Dict

def serialize_output(
    output_path: str,
    collection_name: str,
    input_docs: List[str],
    persona: Dict,
    ranked_sections: List[Dict]
):
    """
    Creates the challenge1b_output.json file with required format.

    Args:
        output_path (str): Folder to write the output file.
        collection_name (str): Subfolder name for saving.
        input_docs (List[str]): List of input PDF filenames.
        persona (Dict): Contains role, focus, job_to_be_done.
        ranked_sections (List[Dict]): Output from ranker with importance_rank.
    """
    # Metadata
    metadata = {
        "input_documents": input_docs,
        "persona": persona.get("role", ""),
        "job_to_be_done": persona.get("job_to_be_done", ""),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # Extracted Section = Title + Page + Rank
    extracted = [
        {
            "document": r["document"],
            "page": r["page"],
            "section_title": r["section_title"],
            "importance_rank": r["importance_rank"]
        }
        for r in ranked_sections
    ]

    # Sub-section analysis = Full text
    subsections = [
        {
            "document": r["document"],
            "page": r["page"],
            "section_title": r["section_title"],
            "refined_text": r["refined_text"],
            "importance_rank": r["importance_rank"]
        }
        for r in ranked_sections
    ]

    final_output = {
        "metadata": metadata,
        "extracted_sections": extracted,
        "subsection_analysis": subsections
    }

    # Create subfolder if needed
    final_dir = os.path.join(output_path, collection_name)
    os.makedirs(final_dir, exist_ok=True)

    with open(os.path.join(final_dir, "challenge1b_output.json"), "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved: {os.path.join(final_dir, 'challenge1b_output.json')}")
