FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt .
COPY .env .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY src/ .

EXPOSE 8000

#uvicorn src.main:app --reload
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]