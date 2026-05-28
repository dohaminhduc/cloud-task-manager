FROM python:3.11-slim

WORKDIR /app

# Cài đặt các thư viện hệ thống cần thiết cho psycopg2 (nếu cần build từ source)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Chạy production mode: Bỏ --reload, tăng số lượng workers bằng uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]