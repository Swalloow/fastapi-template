# type: ignore
import os
import sys
from logging.config import fileConfig

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool

sys.path.append(os.getcwd())
config = context.config

fileConfig(config.config_file_name)


from app.db import metadata  # isort:skip

target_metadata = metadata


def get_url():
    load_dotenv(verbose=True)
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    host = os.getenv("POSTGRES_HOST", "localhost")
    db = os.getenv("POSTGRES_DB", "postgres")
    return f"postgresql://{user}:{password}@{host}/{db}"


config.set_main_option("sqlalchemy.url", get_url())


def run_migrations_online() -> None:
    # configuration = config.get_section(config.config_ini_section)
    # configuration["sqlalchemy.url"] = get_url()
    # print(get_url())

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            version_table="alembic_project_name",
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
