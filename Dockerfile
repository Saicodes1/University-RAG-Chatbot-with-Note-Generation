FROM python:3.11-slim

COPY chroma /work/chroma
COPY Data /work/Data
COPY generated_notes /work/generated_notes
COPY app.py /work/
COPY data_embedding_and_vector_store.py /work/
COPY data_reading_and_splitting.py /work/
COPY LLM_response.py /work/
COPY notes_generator.py /work/
COPY README.md /work/
COPY requirements.txt /work/

WORKDIR /work


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]