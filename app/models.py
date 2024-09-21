from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

import database
from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    tasks = relationship("Task", back_populates="student")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String, nullable=True)
    student_id = Column(Integer, ForeignKey("students.id"))

    student = relationship("Student", back_populates="tasks")
