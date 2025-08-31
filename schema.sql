CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    course TEXT NOT NULL,
    year_of_study INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS loans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    amount REAL NOT NULL,
    status TEXT DEFAULT 'Pending',
    balance REAL NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE IF NOT EXISTS disbursements (
    disbursement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    loan_id INTEGER,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);
