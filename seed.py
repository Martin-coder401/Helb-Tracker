
from datetime import date
from helb_tracker.models import Base, Student, Loan, Disbursement  
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///helb_tracker.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def seed():
    
    students = [
        {'name': 'Alice Wanjiku', 'email': 'alice@example.com', 'course': 'Computer Science', 'year': 2},
        {'name': 'Brian Otieno', 'email': 'brian@example.com', 'course': 'Mathematics', 'year': 3},
    ]

    for s in students:
        if not session.query(Student).filter_by(email=s['email']).first():
            student = Student(**s)
            session.add(student)

    session.commit()
    print("Students seeded successfully.")

    
    loans = [
        {'student_id': 1, 'amount': 5000.0, 'balance': 5000.0},
        {'student_id': 2, 'amount': 7000.0, 'balance': 7000.0},
    ]

    for l in loans:
        if not session.query(Loan).filter_by(student_id=l['student_id'], amount=l['amount']).first():
            loan = Loan(**l)
            session.add(loan)

    session.commit()
    print("Loans seeded successfully.")

    
    disbursements = [
        {'loan_id': 1, 'date': '2025-09-03', 'amount': 1000.0},
        {'loan_id': 2, 'date': '2025-09-04', 'amount': 2000.0},
    ]

    for d in disbursements:
        
        d['date'] = date.fromisoformat(d['date'])
        if not session.query(Disbursement).filter_by(loan_id=d['loan_id'], date=d['date']).first():
            disb = Disbursement(**d)
            session.add(disb)

    session.commit()
    print("Disbursements seeded successfully.")

if __name__ == "__main__":
    seed()
