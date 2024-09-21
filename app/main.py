from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
# from models import Student, Task
from schemas import StudentCreate, Student
from crud import get_students, get_student_by_id, get_student_by_name, create_student

from database import SessionLocal, engine

models.Student.metadata.create_all(bind=engine)
models.Task.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = get_student_by_name(db, student_name=student.name)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already exist")
    return create_student(db=db, student=student)


@app.get("/students/", response_model=list[Student])
def read_users(db: Session = Depends(get_db)):
    students = get_students(db)
    return students


@app.get("/students/{student_id}", response_model=Student)
def read_user(student_id: int, db: Session = Depends(get_db)):
    db_student = get_student_by_id(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")


# class TaskAdd(BaseModel):
#     name: str
#     description: str | None = None
#
#
# class Task(BaseModel):
#     id: int
#
# tasks = []
#
# @app.post("/tasks")
# async def add_task(
#   task: TaskAdd
# ):
#     tasks.append(task)
#     return {"message": "Task was added"}
#
#
# @app.get("/tasks")
# def get_tasks():
#     task = Task(name="Your name")
#     return {"data": task}
