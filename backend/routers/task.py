"""Main module."""

from ..main import app
from pydantic import BaseModel

tasks = []

class Task(BaseModel):
    text: str = ""
    is_done: bool = False
    deadline: str = ""
    urgency: str = ""


@app.get("/")
def root():
    # LATER TAKE FROM DB.PY
    return {"Hello": "World"}

@app.post("/tasks")
def tasksubmission(submittedtask: str):
    tasks.append(submittedtask)
    return submittedtask



