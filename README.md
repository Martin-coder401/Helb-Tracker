# HELB Tracker CLI Application

## Overview
This Phase 3 project is a **Python CLI application** for managing student HELB loans. It uses **SQLite** as the database and demonstrates the use of **SQLAlchemy ORM**, **lists, tuples, and dictionaries**, and proper **CLI design practices**.An explanation of this project is inside this link https://www.veed.io/view/b0b58915-6bd2-4832-ab12-876e2e84a43e?panel=share

The application allows students to register, apply for loans, track loan balances, and allows admins to add disbursements and view analytics.

---


## Folder Structure
helb-tracker/
├─ app.py # Main CLI application
├─ README.md # Project documentation

markdown
Copy code

---

## Features

### Student Module
- **Register Student**: Add a new student with name, email, course, and year of study.
- **View Students**: Display all registered students in a formatted table.
- **Search Student**: Find students by name or email.
- **Apply for Loan**: Students can request a loan amount.
- **View Loan Status**: Display loan amount, balance, and status.

### Admin Module
- **Add Disbursement**: Record when a loan amount is released to a student.
- **View Disbursements**: Display all disbursements with amounts and dates.
- **Automatic Status Update**: Loan status changes to “Active” after disbursement.



## Installation & Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd helb-tracker
Install dependencies with Pipenv:

bash
Copy code
pipenv install
pipenv shell
Run database migrations:

bash
Copy code
alembic upgrade head
Start the application:

bash
Copy code
python app.py
Usage
Run python app.py to start the CLI.

Choose an option from the menu:

markdown
Copy code
1. Register Student
2. View Students
3. Search Student
4. Apply for Loan
5. View Loans
6. Add Disbursement
7. View Disbursements
8. Exit
Follow prompts to input data.

Tables are displayed in a neatly formatted style using tabulate.