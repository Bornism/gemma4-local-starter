# gemma4-local-starter

Run Google's Gemma 4 locally on your machine using Ollama and Python.
Zero cloud cost. Zero API keys. Your data never leaves your machine.

Built and documented by a Google Cloud Solutions Architect and Army veteran
learning in public.

---

## What this is

Three escalating Python demos that show what's possible when you run a
frontier-class open model locally:

- **Demo 1** — Basic chat with streaming responses
- **Demo 2** — Document summarization with structured output
- **Demo 3** — Personal notes Q&A across multiple files (lightweight RAG)

All three run on CPU only if needed. No GPU required.

---

## Why Gemma 4

Gemma 4 is Google DeepMind's fourth generation open-weight model family,
released April 2, 2026 under the **Apache 2.0 license** — meaning free to
use, modify, and deploy commercially with no restrictions.

The E4B variant used here runs on most modern laptops with 8GB+ RAM.
No cloud account. No per-token billing. One download, runs forever.

The license change from Gemma 3's custom restricted terms to Apache 2.0
is arguably more significant than the benchmark improvements. Enterprise
legal teams can approve it without custom review.

---

## Stack

- [Ollama](https://ollama.com) — local model runtime
- Gemma 4 E4B — 9.6GB, Apache 2.0, runs on CPU or GPU
- Python 3.10+
- ollama Python library 0.6.2

---

## Requirements

- Windows, Mac, or Linux
- 8GB RAM minimum (16GB recommended)
- ~10GB free disk space for the model
- Python 3.10+
- Ollama installed

---

## Setup

**Step 1 — Install Ollama**

Download from https://ollama.com/download

**Step 2 — Pull Gemma 4**

    ollama pull gemma4:e4b

**Step 3 — Clone this repo**

    git clone https://github.com/Bornism/gemma4-local-starter.git
    cd gemma4-local-starter

**Step 4 — Create virtual environment and install dependencies**

    python -m venv venv

    # Mac/Linux
    source venv/bin/activate

    # Windows Git Bash
    source venv/Scripts/activate

    # Windows PowerShell
    .\venv\Scripts\Activate.ps1

    pip install -r requirements.txt

**Step 5 — Make sure Ollama is running**

On Windows, check your system tray for the Ollama icon.
Then verify it's responding:

    curl http://localhost:11434
    # Should return: Ollama is running

---

## Running the demos

**Demo 1 — Basic chat**

    python demo1_chat.py

Asks Gemma 4 three questions and streams the responses back in real time.
Shows basic local inference working end to end.

**Demo 2 — Document summarization**

    python demo2_summarize.py

Feeds sample.txt into the model and asks for a structured summary,
key takeaways, and one unanswered question. Swap sample.txt for any
text document you want to summarize.

**Demo 3 — Personal notes Q&A**

    python demo3_notes_qa.py

Loads all .txt files from the notes/ folder and answers questions
across all of them. Drop your own notes into the notes/ folder and
change the questions in the script to match your content.

---

## Windows note

The ollama run gemma4:e4b interactive terminal command may hang in
Git Bash on Windows due to a TTY compatibility issue. This does not
affect the Python demos — they talk to Ollama via the REST API at
localhost:11434 directly, which works perfectly.

If you want to test the model from the terminal on Windows use
PowerShell or Command Prompt instead of Git Bash.

---

## Project structure

```
gemma4-local-starter/
├── demo1_chat.py          # Basic streaming chat
├── demo2_summarize.py     # Document summarization
├── demo3_notes_qa.py      # Multi-file notes Q&A
├── sample.txt             # Sample document for demo 2
├── notes/                 # Sample notes for demo 3
│   ├── finance.txt
│   ├── ai_ideas.txt
│   └── books.txt
├── requirements.txt       # Python dependencies
└── README.md
```

## What's next

This repo is the foundation for a deeper RAG implementation — adding
vector embeddings and proper retrieval so the notes Q&A scales to
hundreds of documents. That build is covered in the companion blog post.

For enterprise deployment patterns — private cloud on GKE, air-gapped
factory floor deployments, Vertex AI Model Garden — see the full blog
post linked below.

---

## Blog post

Full writeup including enterprise deployment architecture, manufacturing
use cases, and the story behind this build:

[Link coming soon]

---

## License

Code in this repo is MIT licensed.
Gemma 4 model weights are Apache 2.0 — see
Google DeepMind's model card at https://ai.google.dev/gemma for details.
