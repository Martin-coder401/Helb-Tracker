# Helb-Tracker

Helb-Tracker is a simple Python/SQLite application for managing students, loans, and disbursements using SQLAlchemy and Alembic for database migrations.
Video recording of the app has been embended in this link https://www.veed.io/view/a334ac69-13c7-405f-b906-7e09219a454a?panel=share

- Manage students, loans, and loan disbursements
- Track loan balances
- Database migrations with Alembic
- Seed database with initial data

## Tech Stack

- Python 3.8+
- SQLAlchemy ORM
- SQLite database
- Alembic for migrations
- Pipenv for virtual environment management

## Project Structure



Helb-Tracker/
├── helb_tracker/
│ ├── models.py
│ ├── migrations/
│ ├── init.py
├── seed.py
├── Pipfile
├── Pipfile.lock
├── README.md
└── helb_tracker.db


## Setup

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd Helb-Tracker


Install dependencies

pipenv install
pipenv shell


Create the database

The database will be automatically created when running migrations or seed scripts.

Database Migrations

Generate a new migration

pipenv run alembic revision --autogenerate -m "Your migration message"


Apply migrations

pipenv run alembic upgrade head


Stamp head (if database is manually updated and you want Alembic to recognize it):

pipenv run alembic stamp head

Seeding the Database

Seed the database with sample data for students, loans, and disbursements:

pipenv run python seed.py


Note: Dates in disbursements must be in YYYY-MM-DD format. The seed script converts them to Python date objects automatically.

Running the Project

The project currently consists of database models and seed scripts. You can interact with the database using Python scripts or extend it with a CLI or web interface.

Example:

from helb_tracker.models import Student, Loan, Disbursement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///helb_tracker.db")
Session = sessionmaker(bind=engine)
session = Session()

students = session.query(Student).all()
print(students)