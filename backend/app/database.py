import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Đọc DATABASE_URL từ môi trường (Nếu sau này có tạo Postgres trên Azure)
DATABASE_URL = os.getenv("DATABASE_URL")

connect_args = {}

# 2. Nếu chưa tạo DB trên Azure (biến DATABASE_URL trống), tự động fallback về SQLite
if not DATABASE_URL or DATABASE_URL.strip() == "":
    # Sử dụng cú pháp tương đối chuẩn, không dùng os.path.abspath để tránh lỗi phân tách URI trên Linux
    DATABASE_URL = "sqlite:///./test.db"
    connect_args = {"check_same_thread": False}
    print("--> [DATABASE] Cấu hình trống. Tự động chạy SQLite tạm thời: ./test.db")
else:
    print(f"--> [DATABASE] Đang kết nối tới Production DB: {DATABASE_URL}")

# 3. Khởi tạo Engine
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()