# alembic/env.py
import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import importlib

# --- Add project root to path ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- Load .env variables ---
from dotenv import load_dotenv
load_dotenv()

# --- Alembic config ---
config = context.config
fileConfig(config.config_file_name)

# --- Import Base ---
from app.database.base import Base

# --- Set target metadata for Alembic ---
target_metadata = Base.metadata

# --- Use DATABASE_URL from .env ---
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env file")

config.set_main_option("sqlalchemy.url", DATABASE_URL)

# --- Offline migrations ---
def run_migrations_offline():
    context.configure(url=DATABASE_URL, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

# --- Online migrations ---
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()