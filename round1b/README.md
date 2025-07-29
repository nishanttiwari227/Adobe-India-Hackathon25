# Round 1B: Persona‑Driven Document Intelligence

This project builds on your Round 1A PDF outline extractor to produce persona‑driven insights from a collection of PDFs. It processes multiple documents, ranks sections by relevance to a given persona and job, and outputs structured JSON.

---

## 📦 Project Structure

round1b/
├── collections/
│ ├── round_1b_001/
│ │ ├── challenge1b_input.json
│ │ └── *.pdf
│ ├── round_1b_002/
│ └── round_1b_003/
├── outputs/
│ ├── round_1b_001/ # generated outputs here
│ ├── round_1b_002/
│ └── round_1b_003/
├── src/
│ ├── loader.py
│ ├── segmenter.py
│ ├── ranker.py
│ ├── serializer.py
│ └── main.py
├── run_all_collections.ps1 # Windows batch script
├── requirements.txt
└── Dockerfile



---

## 📋 Requirements

- **Python** 3.11 (container base)
- **Dependencies** (in `requirements.txt`):

pymupdf==1.26.3
numpy==1.25.0
scikit-learn==1.3.0
pytest==7.4.0
python-dotenv==1.0.0


- **No internet** access during Docker run
- **CPU-only**, AMD64

---

## 🛠️ Setup & Build

1. **Clone** this repo into your workspace.
2. Ensure Python 3.11 is installed locally if you want to run outside Docker.
3. **Build** the Docker image (from `round1b/` folder):
 ```bash
 docker build --platform linux/amd64 -t pdf-intel-r1b .

Local (non‑Docker) Usage
If someone wants to run it straight in Python (e.g. for development), show how to set up the venv and run:

python -m venv .venv
source .venv/bin/activate       # or .\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
python src/main.py collections/round_1b_001


Environment Variables / .env
If you ever introduce configurable settings (like max sections to return, logging level, etc.), note that you use a .env (with python‑dotenv) and give an example:

MAX_SECTIONS=10
LOG_LEVEL=INFO

🚀 Usage
Single Collection
Run the container for one collection (e.g. round_1b_001):

Windows (single line)

docker run --rm -v "%cd%/collections:/app/collections" -v "%cd%/outputs:/app/outputs" --network none pdf-intel-r1b collections/round_1b_001

Windows (multi-line PowerShell)

docker run --rm `
  -v "${PWD}/collections:/app/collections" `
  -v "${PWD}/outputs:/app/outputs" `
  --network none `
  pdf-intel-r1b collections/round_1b_001


Linux/macOS

docker run --rm \
  -v "$(pwd)/collections:/app/collections" \
  -v "$(pwd)/outputs:/app/outputs" \
  --network none \
  pdf-intel-r1b collections/round_1b_001


Batch Process All Collections
We’ve provided a PowerShell script to process all three folders:

# run_all_collections.ps1
$collections = @("round_1b_001","round_1b_002","round_1b_003")
foreach ($col in $collections) {
    Write-Host "🔄 Processing $col ..."
    docker run --rm `
      -v "${PWD}/collections:/app/collections" `
      -v "${PWD}/outputs:/app/outputs" `
      --network none `
      pdf-intel-r1b "collections/$col"
    Write-Host "✅ Done: outputs\$col\challenge1b_output.json"
}
Write-Host "🏁 All collections processed!"

Run it from PowerShell:

powershell -ExecutionPolicy Bypass -File run_all_collections.ps1

📂 Outputs
After running, you’ll find for each collection:

outputs/
└── round_1b_00X/
    └── challenge1b_output.json

Each JSON contains:

metadata: input documents, persona role, job, timestamp

extracted_sections: list of sections with importance_rank

subsection_analysis: section text summaries with ranking

🧪 Testing
Run unit tests locally (requires pytest):

pytest -q

