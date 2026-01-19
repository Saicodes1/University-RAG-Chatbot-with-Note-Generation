# RAG-For-University-Learning

A Retrieval-Augmented Generation (RAG) based web application for university-level learning and note generation, using LLMs and vector search.

## Features
- **Question Answering:** Ask questions about course topics and get context-aware, academic responses.
- **Notes Generation:** Generate well-structured, markdown-formatted notes for specific chapters or topics ( Chapter wise ).
- **Document Retrieval:** Uses Chroma vector store and semantic search for relevant content.
- **Web Interface:** Flask-based web app with separate pages for different subjects.
- **Downloadable Notes:** Download generated notes as markdown files.

## Project Structure
```
app.py                        # Main Flask app
LLM_response.py               # Handles LLM-based responses and context retrieval
notes_generator.py            # Generates notes from retrieved content
requirements.txt              # Python dependencies
chroma/                       # Chroma vector store data
Data/                         # Source data for embedding
static/style.css              # CSS styles
templates/                    # HTML templates for web pages
  ├── welcome.html
  ├── compiler_construction.html
  └── computer_networks.html
```

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the app:**
   ```bash
   python app.py
   ```
4. **Access in browser:**
   Visit [http://localhost:5000](http://localhost:5000)

## Usage
- Go to the homepage and select a subject.
- Ask questions or request notes (e.g., "Generate notes for Chapter 2").
 ### How to Generate Notes

To generate notes, include the word **"notes"** in your prompt along with the relevant topic keywords:

- **Compiler Construction notes**  
  Include **"notes"** and one of:
  - **"introduction to compilers and phases"**
  - **"syntax analysis"**

- **Computer Networks notes**  
  Include **"notes"** and one of:
  - **"chapter 2"**
  - **"chapter 3"**
- Download notes from the provided link.

## Key Technologies
- **Flask**: Web framework
- **LangChain**: LLM orchestration and retrieval
- **Chroma**: Vector database
- **Gemma 3.1 4B params**: LLM backend
- **Nomic Embed Text**: Embeddings


