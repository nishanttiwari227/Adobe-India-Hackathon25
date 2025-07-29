import os
import pytest
import json
import fitz  # PyMuPDF

from src.loader import load_collection
from src.extractor import extract_sections

# Adjust this path if your collections folder is elsewhere
COLLECTION_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "collections", "round_1b_001")


def test_loader_load_collection():
    """
    loader.load_collection should return:
      - config: a dict containing at least 'persona' and 'job_to_be_done'
      - docs: a non-empty list of (filename, fitz.Document) tuples
    """
    config, docs = load_collection(COLLECTION_PATH)
    
    # Config checks
    assert isinstance(config, dict), "Config should be a dict"
    assert "persona" in config, "Config must contain 'persona'"
    assert "job_to_be_done" in config, "Config must contain 'job_to_be_done'"
    
    # Docs checks
    assert isinstance(docs, list), "Docs should be a list"
    assert len(docs) > 0, "Docs list should not be empty"
    for fname, doc in docs:
        assert isinstance(fname, str), "Filename should be a string"
        assert isinstance(doc, fitz.Document), "Each doc should be a fitz.Document"
        # Basic sanity: should have at least one page
        assert doc.page_count >= 1, f"{fname} should have ≥1 page"


def test_extract_sections_structure():
    """
    extractor.extract_sections should return a list of dicts,
    each with keys: 'doc_id', 'page_num', 'heading', 'text'.
    """
    # First load the docs
    config, docs = load_collection(COLLECTION_PATH)
    
    sections = extract_sections(docs)
    assert isinstance(sections, list), "extract_sections must return a list"
    assert len(sections) > 0, "There should be at least one section extracted"
    
    sample = sections[0]
    # Check presence of all required keys
    for key in ("doc_id", "page_num", "heading", "text"):
        assert key in sample, f"Each section must have '{key}'"
    
    # Check types of each field
    assert isinstance(sample["doc_id"], str), "'doc_id' must be a string"
    assert isinstance(sample["page_num"], int), "'page_num' must be an int"
    assert isinstance(sample["heading"], str), "'heading' must be a string"
    assert isinstance(sample["text"], str), "'text' must be a string"
    
    # There should be non-empty text
    assert len(sample["text"].strip()) > 0, "Extracted 'text' should not be empty"


if __name__ == "__main__":
    # Allow script-style execution
    pytest.main([__file__])
