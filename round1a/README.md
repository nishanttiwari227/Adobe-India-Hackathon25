# PDF Outline Extractor (Adobe Hackathon Round 1A)

Extract structured outlines (Title, H1–H3 headings with page numbers) from PDFs.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows PowerShell
pip install -r requirements.txt
```

# Round 1A: PDF Outline Extractor

Extract clean, hierarchical outlines (Title, H1–H3 headings with page numbers) from PDFs.
This is your “brains” for Adobe’s “Connecting the Dots” challenge—structure is everything!

---

## 📂 Project Structure

```bash
round1a/
├── inputs/            # Place your PDFs here (≤ 50 pages each)
├── outputs/           # JSON outlines appear here
├── src/
│   ├── __init__.py
│   ├── detector.py    # Heading–font detection & filtering
│   ├── extractor.py   # Main script: calls detector + serializer
│   ├── hierarchy.py   # (Optional) Nested tree builder
│   └── serializer.py  # JSON dump helper
├── tests/
│   ├── sample.pdf     # Small test document
│   ├── sample.json    # Expected JSON output example
│   └── test_outline.py # Pytest cases for format correctness
├── batch_run.py       # Process all PDFs in inputs/ → outputs/
├── requirements.txt   # PyMuPDF, pytest
├── Dockerfile         # AMD64 Linux, no‑network container
└── README.md          # You are here
```

---

## 🛠️ Setup & Usage

1. **Clone** this repo (or copy this folder into your own hackathon repo).
2. **Create** and **activate** a Python venv:

   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .\.venv\Scripts\Activate.ps1
   # macOS/Linux:
   source .venv/bin/activate
   pip install --no-cache-dir -r requirements.txt
   ```

### 🚀 Usage

**Single PDF**

```bash
python src/extractor.py inputs/your_doc.pdf
```

Saves `outputs/your_doc.json`.

**Batch Mode**

```bash
python batch_run.py
```

Loops through every `*.pdf` in `inputs/`, producing matching `.json` in `outputs/`.

**Automated Tests**

```bash
pytest -q
```

**🐳 Docker (AMD64, Offline)**
Build the image:

```bash
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .
```

Run against your folders:

```bash
docker run --rm \
  -v "$(pwd)/inputs":/app/inputs \
  -v "$(pwd)/outputs":/app/outputs \
  --network none \
  pdf-outline-extractor:latest
```

---

## ⚡ Performance

* **Goal:** ≤ 10 seconds per 50‑page PDF on a standard AMD64 CPU.
* **Measured:** 0.14 s for a 50‑page sample (⚡ blazing fast!).

---

## 💡 Approach

* PyMuPDF (fitz) to extract every span’s text + font‑size per page.
* Detect Title: the largest‑font spans on page 1, concatenated.
* Detect Headings: the next three distinct font sizes → H1, H2, H3.
* **Fallback heuristics:** if font sizes alone are ambiguous, use style cues (bold/italic) or indentation patterns.
* Filter noise: emails, phone numbers, URLs, dates, very short spans.
* Flatten into ordered list of `{ level, text, page }`.
* *(Optional)* Build nested H1→H2→H3 trees in `hierarchy.py`.
* Serialize to JSON with 2‑space indentation.

---

## 🏁 Challenge Requirements

* **Input:** PDFs up to 50 pages.
* **Output:** JSON `{ "title": ..., "outline": [ ... ] }` with title + H1–H3 headings and page numbers.
* **Levels:** Title + H1, H2, H3 headings.
* **Performance:** ≤ 10 s/PDF.
* **Docker:** Linux/AMD64, CPU‑only, offline, `--network none`.
* **No hard‑coding:** works on *any* PDF (font‑size + style-based detection).

