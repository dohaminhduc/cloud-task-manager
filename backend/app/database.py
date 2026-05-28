import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")

connect_args = {}

if not DATABASE_URL or DATABASE_URL.strip() == "":
    DATABASE_URL = "sqlite:///./test.db"
    connect_args = {"check_same_thread": False}
    print("--> [DATABASE] Missing configuration. Falling back to temporary SQLite: ./test.db")
else:
    print(f"--> [DATABASE] Connecting to Production DB: {DATABASE_URL}")

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()