from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base  # import Base from database.py

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    course = Column(String, nullable=False)
    year = Column(Integer, nullable=False)   # ✅ changed from year_of_study → year

    loans = relationship("Loan", back_populates="student")


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    amount = Column(Float, nullable=False)
    balance = Column(Float, nullable=False)
    status = Column(String, nullable=False)

    student = relationship("Student", back_populates="loans")
    disbursements = relationship("Disbursement", back_populates="loan")


class Disbursement(Base):
    __tablename__ = "disbursements"

    id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey("loans.id"))
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    loan = relationship("Loan", back_populates="disbursements")
