import re

# skip anything that looks like a date or footer
_DATE_RX = re.compile(r'\b(?:\d{1,2}[\/\-]\d{1,2}[\/\-]\d{2,4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},?\s*\d{2,4})\b', re.IGNORECASE)
_YEAR_RX = re.compile(r'\b(?:19|20)\d{2}\b')

def detect_headings(pages):
    # Collect all spans: (page, font-size, text)
    all_spans = []
    for page_idx, page in enumerate(pages):
        for block in page.get("blocks", []):
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    size = span.get("size")
                    text = span.get("text", "").strip()
                    if text:
                        all_spans.append((page_idx + 1, size, text))

    if not all_spans:
        return "Untitled", []

    # Determine title size and heading sizes
    sizes = sorted({fs for _, fs, _ in all_spans}, reverse=True)
    title_size = sizes[0]
    heading_sizes = sizes[1:4]  # next three sizes → H1, H2, H3

    # 1) Build the full title: all title_size spans on page 1, in order
    title_parts = [
        text for pg, fs, text in all_spans
        if fs == title_size and pg == 1
    ]
    title = " ".join(title_parts).strip() or "Untitled"

    # 2) Extract headings flat
    outline = []
    last = None
    for pg, fs, text in all_spans:
        if fs not in heading_sizes:
            continue

        # noise filters
        if len(text) < 4:
            continue
        if any(tok in text.lower() for tok in ("@", "+91", "http", "www")):
            continue
        if _DATE_RX.search(text) or _YEAR_RX.search(text):
            continue

        level = f"H{heading_sizes.index(fs) + 1}"
        entry = {"level": level, "text": text, "page": pg}

        # merge if same level & page as previous
        if last and last["level"] == entry["level"] and last["page"] == entry["page"]:
            last["text"] += " " + entry["text"]
        else:
            outline.append(entry)
            last = entry

    return title, outline
