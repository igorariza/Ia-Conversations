FROM python:3.9-slim


WORKDIR /app


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 8000

#uvicorn src.main:app --reload
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]