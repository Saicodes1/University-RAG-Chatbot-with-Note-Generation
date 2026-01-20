from langchain_classic.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from ollama import chat
import os

def notes_generation(user_input,collection):
    embedding = HuggingFaceEmbeddings(
        model_name="nomic-ai/nomic-embed-text-v1",
        model_kwargs={"trust_remote_code": True}
    )
    print(collection)
    vectorstore =  Chroma(
        persist_directory="E:/Projects/RAG-For-University-Learning/chroma",
        collection_name=collection,
        embedding_function=embedding
    )

    chapter = None
    if "chapter_2" in user_input.lower() or "chapter 2" in user_input.lower():
        chapter = "Chapter_2"
    elif "chapter_3" in user_input.lower() or "chapter 3" in user_input.lower():
        chapter = "Chapter_3"
    elif "syntax analysis" in user_input.lower():
        chapter = "Syntax Analysis"
    elif "introduction to compilers and phases" in user_input.lower():
        chapter = "Introduction to Compilers and Phases"

    print("chapter is:",chapter)
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 99999,
            "filter": {"Chapter_name": chapter}
        }
    )

    docs = retriever.invoke(user_input)
    print(docs)
    context ="" 
    page_content_completed=[doc.page_content for doc in docs]
    print("The page content:",page_content_completed)
    for page_done in page_content_completed:
        context += "\n\n"+page_done

    print("Context is:",context)
    prompt=f'''
            You are a notes generator. Your task is to convert the given {context} into precise, well-structured notes.

Rules

Use Markdown formatting.

Break the content into topics.

Whenever a new concept or idea appears, create a new heading.

Explain every concept clearly, using:

short definitions

examples (if needed)

key points and bullet lists

Keep it concise but complete.

Add important formulas, definitions, and steps wherever necessary.

Use subheadings, bullets, and tables for clarity.

Output Format

Heading for each topic

Short explanation

Important points in bullets

Examples (optional)

Summary (optional)'''
    
    response=chat(
            model="gemma3:4b",
            messages=[{"role":"user","content":prompt}]
        )
    
    filename = "notes.md"
    filepath= os.path.join("generated_notes",filename)
    os.makedirs("generated_notes",exist_ok=True)
    with open(filepath, "w",encoding="utf-8") as f:
        f.write(response.message.content)
    
    return filepath


