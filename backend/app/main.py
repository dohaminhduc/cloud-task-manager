from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import tasks

app = FastAPI(title="Cloud Native Task Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(tasks.router)

@app.get("/")
def home():
    return {"status": "healthy", "message": "API is running smoothly"}