from typing import List, Tuple
import fitz  # PyMuPDF

def extract_text(doc: fitz.Document) -> List[Tuple[int, str]]:
    """
    Extracts all text by page.

    Returns:
        List of (page_number, text) tuples
    """
    results = []
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            results.append((i + 1, text))  # 1-based index
    return results
