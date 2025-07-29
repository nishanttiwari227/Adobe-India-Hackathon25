# Approach Explanation – Round 1B

## Problem Overview

Given a set of PDFs, a user persona, and a job-to-be-done, the task is to extract and rank the most relevant sections and sub-sections. The solution must run in under 60 seconds, offline, on a CPU-only environment with <1GB models.

---

## 1. Input Loader

- Used PyMuPDF to parse each PDF.
- JSON-based config file (`challenge1b_input.json`) lists document names, persona, and job.
- Persona definition is separately stored in `persona.json`.

---

## 2. Section Detection & Segmentation

- Reused Round 1A’s heading extractor to identify `H1`, `H2`, and `H3` text elements.
- Text blocks are segmented into “sections” based on heading hierarchy.
- Each section contains:
  - document name
  - page number
  - section title
  - full section text

---

## 3. Ranking Logic

- Used `sentence-transformers` (MiniLM-L6-v2) to generate embeddings for:
  - Section title + first 100 words
  - Job description
- Cosine similarity computed between job embedding and each section.
- Top-ranked sections are selected and sorted.

---

## 4. Output Format

- JSON contains:
  - `metadata`: document names, persona, job, timestamp
  - `extracted_sections`: top-ranked sections with titles and page numbers
  - `subsection_analysis`: refined text blocks for deeper insight

---

## 5. Performance & Constraints

- Processing time: <60s for 3–10 docs
- All components run offline
- Dockerized for reproducibility
- Model size <1GB and CPU-compatible

---

## Reusability

- Heading detection reused from Round 1A
- Modular architecture for easy testability
