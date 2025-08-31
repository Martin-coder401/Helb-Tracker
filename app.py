import sqlite3
from tabulate import tabulate

DB_NAME = "helb_tracker.db"

def register_student():
    name = input("Enter name: ")
    email = input("Enter email: ")
    course = input("Enter course: ")
    year = int(input("Enter year of study: "))

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO students (name, email, course, year_of_study)
            VALUES (?, ?, ?, ?)
        """, (name, email, course, year))
        conn.commit()
    print(f"Student {name} registered successfully!")

def view_students():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()

    if rows:
        headers = ["ID", "Name", "Email", "Course", "Year of Study"]
        print(tabulate(rows, headers, tablefmt="grid"))
    else:
        print("No students found.")

def search_student():
    keyword = input("Enter name or email to search: ")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM students
            WHERE name LIKE ? OR email LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))
        rows = cursor.fetchall()

    if rows:
        headers = ["ID", "Name", "Email", "Course", "Year of Study"]
        print(tabulate(rows, headers, tablefmt="grid"))
    else:
        print("No matching student found.")

def apply_loan():
    student_id = int(input("Enter student ID: "))
    amount = float(input("Enter loan amount: "))

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO loans (student_id, amount, balance)
            VALUES (?, ?, ?)
        """, (student_id, amount, amount))
        conn.commit()
    print(f"Loan of {amount} applied for student ID {student_id}!")

def view_loans():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT loan_id, student_id, amount, status, balance 
            FROM loans
        """)
        rows = cursor.fetchall()

    if rows:
        headers = ["Loan ID", "Student ID", "Amount", "Status", "Balance"]
        print(tabulate(rows, headers, tablefmt="grid"))
    else:
        print("No loans found.")

def add_disbursement():
    loan_id = int(input("Enter loan ID: "))
    amount = float(input("Enter disbursement amount: "))
    date = input("Enter disbursement date (YYYY-MM-DD): ")

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO disbursements (loan_id, amount, date)
            VALUES (?, ?, ?)
        """, (loan_id, amount, date))
        cursor.execute("""
            UPDATE loans 
            SET balance = balance - ?
            WHERE loan_id = ?
        """, (amount, loan_id))
        cursor.execute("""
            UPDATE loans 
            SET status = 'Active'
            WHERE loan_id = ?
        """, (loan_id,))
        conn.commit()
    print(f"Disbursement of {amount} added to loan {loan_id}!")

def view_disbursements():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disbursements")
        rows = cursor.fetchall()

    if rows:
        headers = ["Disbursement ID", "Loan ID", "Amount", "Date"]
        print(tabulate(rows, headers, tablefmt="grid"))
    else:
        print("No disbursements found.")

def menu():
    while True:
        print("\n--- HELB Tracker Menu ---")
        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Apply for Loan")
        print("5. View Loans")
        print("6. Add Disbursement")
        print("7. View Disbursements")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            apply_loan()
        elif choice == "5":
            view_loans()
        elif choice == "6":
            add_disbursement()
        elif choice == "7":
            view_disbursements()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()
