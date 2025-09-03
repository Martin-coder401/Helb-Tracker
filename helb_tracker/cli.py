
from database import SessionLocal
from models import Student, Loan, Disbursement

def register_student():
    session = SessionLocal()
    name = input("Enter name: ")
    email = input("Enter email: ")
    course = input("Enter course: ")
    year = int(input("Enter year: "))

    student = Student(name=name, email=email, course=course, year=year)
    session.add(student)
    session.commit()
    print("Student registered successfully!")
    session.close()

def menu():
    while True:
        print("\n HELB Tracker CLI")
        print("1. Register Student")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            break
        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
