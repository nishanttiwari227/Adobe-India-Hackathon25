import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.extractor import extract_outline

def test_extractor_output_format():
    out = extract_outline("tests/sample.pdf")
    data = json.loads(out)

    assert "title" in data
    assert isinstance(data["title"], str)
    assert "outline" in data
    assert isinstance(data["outline"], list)
    if data["outline"]:
        first = data["outline"][0]
        assert "level" in first and first["level"] in ["H1", "H2", "H3"]
        assert "text" in first and isinstance(first["text"], str)
        assert "page" in first and isinstance(first["page"], int)
