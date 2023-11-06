from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

import os

import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

# Retrieve the environment variables using os.getenv()
conn_str = os.getenv("DATABASE_CONNECTION_URL")

# Establish the database connection
conn = None  # Define the 'conn' variable in a higher scope
cursor = None

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


# Create an SQLAlchemy engine using the existing pyodbc connection
engine = create_engine("mssql+pyodbc://", creator=lambda: conn)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
