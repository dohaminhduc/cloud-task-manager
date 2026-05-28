from fastapi import APIRouter

# This is the exact 'router' variable that main.py is looking for!
router = APIRouter()

tasks = []

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return task