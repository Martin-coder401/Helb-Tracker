import sys
import os

# Ensure project root is in sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context

from helb_tracker.database import Base, DATABASE_URL
import helb_tracker.models  # ensures models are imported


from helb_tracker.database import Base
from helb_tracker.models import Student, Loan, Disbursement


# This is the Alembic Config object, which provides access to .ini values
config = context.config

# Setup Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Point Alembic to your models' metadata for autogenerate
target_metadata = Base.metadata

# Hardcode SQLite URL here
DATABASE_URL = "sqlite:///helb_tracker.db"


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.
    Configures the context with just a URL and not an Engine.
    Calls to context.execute() emit given SQL to the output.
    """
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.
    Creates an Engine and associates a connection with the context.
    """
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
