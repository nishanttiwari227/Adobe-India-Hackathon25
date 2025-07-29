# Adobe India Hackathon 2025 Solutions

This repository contains my solutions for Round 1A and Round 1B of the Adobe “Connecting the Dots” Hackathon.

---

## 📂 Repository Layout

```
.
├── round1a/               # Outline extractor challenge
│   ├── input/            # Sample PDFs
│   ├── output/           # Generated JSON outlines
│   ├── src/              # Python code (extractor, detector, serializer)
│   ├── Dockerfile         # Container build for Round 1A
│   ├── requirements.txt
│   └── README.md          # Round 1A–specific instructions
│
├── round1b/               # Persona-driven analysis challenge
│   ├── collections/      # 3 sample collections (001, 002, 003)
│   ├── inputs/           # (Optional) alternative inputs folder
│   ├── outputs/          # Generated JSON results
│   ├── src/              # Python pipeline (loader, segmenter, ranker, serializer, main)
│   ├── persona.json      # Persona + job definition
│   ├── Dockerfile         # Container build for Round 1B
│   ├── requirements.txt
│   ├── approach_explanation.md
│   └── README.md          # Round 1B–specific instructions
│
├── .gitignore
└── README.md              # This file
```

---

## 🚀 Quick Start

### Round 1A: Outline Extraction

1. **Enter the Round 1A folder**

   ```bash
   cd round1a
   ```
2. **Build Docker image**

   ```bash
   docker build -t round1a:latest .
   ```
3. **Run against sample PDFs**

   ```bash
   docker run --rm \
     -v "$(pwd)/input":/app/input \
     -v "$(pwd)/output":/app/output \
     round1a:latest
   ```
4. **View JSON outlines** in `round1a/output/`.

See [`round1a/README.md`](round1a/README.md) for full details.

### Round 1B: Persona‑Driven Analysis

1. **Enter the Round 1B folder**

   ```bash
   cd round1b
   ```
2. **Build Docker image**

   ```bash
   docker build -t round1b:latest .
   ```
3. **Run pipeline**

   ```bash
   docker run --rm \
     -v "$(pwd)/collections":/app/collections \
     -v "$(pwd)/outputs":/app/outputs \
     round1b:latest
   ```
4. **Inspect results** in `round1b/outputs/`.

See [`round1b/README.md`](round1b/README.md) for full details.

---

## 🧠 Solution Highlights

### Round 1A

* Fast, on-device outline extraction (Title, H1–H3)
* JSON output for downstream processing
* Modular detector + serializer

### Round 1B

* Persona‑driven section segmentation (via headings)
* Semantic ranking using MiniLM embeddings
* Structured JSON output with metadata

*All components run offline, CPU‑only, and within the specified performance constraints.*

---

## 🛠️ Requirements

* **Docker** (for containerized runs)
* **Python 3.11+** (for local development)

Install dependencies in each folder via:

```bash
pip install -r round1a/requirements.txt
pip install -r round1b/requirements.txt
```

---

