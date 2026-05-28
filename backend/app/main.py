from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import tasks

app = FastAPI(title="Cloud Native Task Manager API")

# 1. Sửa lỗi CORS nghiêm trọng khi Frontend gọi API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trong thực tế thay bằng URL của Frontend trên Azure
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tạo tables trong DB nếu chưa tồn tại
Base.metadata.create_all(bind=engine)

# Đăng ký Router
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"status": "healthy", "message": "API is running smoothly"}