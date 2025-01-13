FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Use PORT environment variable from Render
CMD ["sh", "-c", "hypercorn app:app --bind 0.0.0.0:$PORT"]
