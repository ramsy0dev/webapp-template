"""
This file contains a database class for handling database interactions.


file:backend/backend/database/handler.py
"""
import sqlalchemy

from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker
)

# Database connection
from backend.backend.database.conn import Database

# Tables
from backend.backend.database.tables import *

# Logger
from backend.backend.logger import logger

class DatabaseHandler:
    def __init__(self, database_engine: sqlalchemy.create_engine) -> None:
        self.database_engine = database_engine
        self.database_session = sessionmaker(
            bind=self.database_engine, expire_on_commit=False
        )


        self.setup_tables(base=Base)

    def setup_tables(self, base: DeclarativeBase) -> None:
        """
        Setup the needed database tables

        Args:
            base (DeclarativeBase): A DeclarativeBase sub-class.


        Returns:
            None
        """
        # Test the connection first
        try:
            with self.database_engine.connect() as conn:
                logger.debug("Database connection successful")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise
        
        # Create the database tables.
        logger.debug("Setting up PostgreSQL tables for production")
        try:
            # Use migration-safe approach for PostgreSQL
            self._create_tables_safely(base)
        except Exception as e:
            logger.error(f"PostgreSQL table creation failed: {e}")
            raise

    def _create_tables_safely(self, base: DeclarativeBase) -> None:
        """
        Safely create tables, handling schema evolution.
        """

        try:
            # Try creating all tables at once
            base.metadata.create_all(self.database_engine)
            logger.debug("Table creation completed successfully")
        except Exception as e:
            logger.error(f"Table creation failed: {str(e)}")
            logger.info("If you have an existing database, you may need to manually update the schema.")
            logger.info("Please refer to the migration documentation for schema updates.")
            raise
