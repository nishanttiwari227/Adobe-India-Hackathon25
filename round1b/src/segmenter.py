# src/segmenter.py

import fitz  # PyMuPDF
from collections import namedtuple
from typing import List

Section = namedtuple("Section", ["doc_name", "page", "title", "text"])

def segment_document(doc: fitz.Document, doc_name: str) -> List[Section]:
    sections = []
    heading_font_sizes = []
    all_text = []

    # First pass to gather font sizes and spans
    for page_num, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                line_text = ""
                for span in line.get("spans", []):
                    size = span["size"]
                    text = span["text"].strip()
                    if not text:
                        continue
                    all_text.append((size, text, page_num + 1))
                    heading_font_sizes.append(size)
                    line_text += text + " "
                if line_text.strip():
                    all_text.append((size, line_text.strip(), page_num + 1))

    # Determine heading sizes (top 2-3 font sizes)
    heading_font_sizes = sorted(set(heading_font_sizes), reverse=True)
    if not heading_font_sizes:
        return []

    h1_size = heading_font_sizes[0]
    h2_size = heading_font_sizes[1] if len(heading_font_sizes) > 1 else h1_size

    # Group into sections
    current_title = None
    current_text = ""
    current_page = 1

    for size, text, page in all_text:
        if size == h1_size or size == h2_size:
            if current_title:
                sections.append(Section(doc_name, current_page, current_title, current_text.strip()))
            current_title = text
            current_text = ""
            current_page = page
        else:
            current_text += " " + text

    if current_title:
        sections.append(Section(doc_name, current_page, current_title, current_text.strip()))

    return sections
