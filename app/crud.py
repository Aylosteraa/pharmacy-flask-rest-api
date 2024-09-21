from sqlalchemy.orm import Session

from models import Student, Task, Base
from schemas import TaskBase, TaskCreate, Task, StudentBase, StudentCreate, Student


def get_students(db: Session):
    return db.query(Student).order_by(Student.name).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id)


def get_student_by_name(db: Session, student_name: str):
    return db.query(Student).filter(Student.name == student_name)


def create_student(db:Session, student: StudentCreate):
    db_student = Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_tasks(db: Session):
    return db.query(Task).all()


def create_task(db:Session, task: TaskCreate, student_id: int):
    db_task = Student(**task.dict(), student_id=student_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
