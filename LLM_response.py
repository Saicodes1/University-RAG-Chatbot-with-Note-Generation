from ollama import chat
from langchain_community.llms import Ollama
from sentence_transformers import SentenceTransformer
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import FlashrankRerank
from langchain_classic.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from flashrank import Ranker
from flask_sqlalchemy import SQLAlchemy
from flask import Flask 
from notes_generator import notes_generation
import os
import numpy as np
def response(user_input, collection, Chat):
    embedding = HuggingFaceEmbeddings(
        model_name="nomic-ai/nomic-embed-text-v1",
        model_kwargs={"trust_remote_code": True}
    )
    if "notes" in user_input.lower():
        file_path=notes_generation(user_input,collection)
        return file_path
    
    else:
        vectorstore =  Chroma(
            persist_directory="E:/Projects/RAG-For-University-Learning/chroma",
            collection_name=collection,
            embedding_function=embedding
        )

        retriever = vectorstore.as_retriever(search_kwargs={"k": 40})

        ranker=Ranker(model_name="ms-marco-MiniLM-L-12-v2")

        compressor = FlashrankRerank(top_n=30)
        compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=retriever
        )


        compressed_docs=compression_retriever.invoke(user_input)
        last_response = Chat.query.with_entities(Chat.bot_answer).order_by(Chat.id.desc()).first()
        if last_response:
            last_response_text=last_response.bot_answer
        else: 
            last_response_text=None
        print("Compressed_docs are: ",compressed_docs)
        #context = "\n\n".join([doc.page_content for doc in compressed_docs])
        context=""
        for doc in compressed_docs:
            if doc.metadata["relevance_score"]>0.05:
                context +="\n\n"+doc.page_content
        prompt=f'''
    You are a highly trusted academic chatbot designed for university-level learning and assessment.

    You will be provided with:

    User Question: {user_input}

    Context: {context} 

    Previous Responses: {last_response_text}

    Instructions

    IF THERE IS NO CONTEXT, DO NOT MAKE UP CONTEXT.
    Answer strictly based on the given context. Do not introduce assumptions, external knowledge, or hallucinated details.

    Carefully analyze the user question and ensure your response is directly relevant to it.

    Use the previous responses only if required, or else dont use it. VERY IMPORTANT.


    WHEN CONTEXT AND  PREVIOUS RESPONSES IS NOTHING, AND THE USER IS ASKING ANYTHING RELATED TO PREVIOUS DISCUSSIONS, SAY NOTHING HAS BEEN DISCUSSED.

    Maintain full consistency with previous responses.

    Do not contradict, modify, or invalidate any prior discussion.


    If the question is unrelated to the given context or previous discussion, clearly state that it cannot be answered.

    Ensure all information is factually correct, precise, and academically sound.

    Provide the answer as a clear, well-structured summary.

    Keep the response concise and focused, with a maximum length of 300–400 words (shorter answers are acceptable if sufficient).

    Do not include irrelevant explanations, disclaimers, or extra commentary.

    Output Requirements

    The response must be clear, accurate, and context-aligned.

    Use formal academic language suitable for university students.

    Do not repeat the question or restate the prompt.

    Most important: Understand the user question extremely carefully before answering and ensure every statement is supported by the provided context.
                '''
        print(prompt)

        response=chat(
            model="gemma3:4b",
            messages=[{"role":"user","content":prompt}]
        )
        #filtered_response = response.message.content.replace("*","")

        return response.message.content