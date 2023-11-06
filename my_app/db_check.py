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


try:
    # Establish the database connection
    conn = pyodbc.connect(conn_str)

    # Create an SQLAlchemy engine using the existing pyodbc connection
    engine = create_engine("mssql+pyodbc://", creator=lambda: conn)

    # Create an SQLAlchemy session maker
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # You are now connected to the database
    print("Connected to the database")

    # Define your SQL query
    sql_query = text("SELECT top(1) * FROM HUB_TEST")

    # Execute the query using the engine
    with engine.connect() as connection:
        result = connection.execute(sql_query)

        for row in result:
            print(row)

except Exception as e:
    print(f"Error connecting to the database: {e}")
finally:
    if "conn" in locals():
        conn.close()
