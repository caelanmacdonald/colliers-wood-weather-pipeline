import os

import psycopg
from dotenv import load_dotenv


load_dotenv()

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise RuntimeError("DATABASE_URL was not found in the .env file.")

with psycopg.connect(database_url) as connection:
    with connection.cursor() as cursor:
        cursor.execute("SELECT current_database(), current_user;")
        database_name, user_name = cursor.fetchone()

print("Connected successfully.")
print(f"Database: {database_name}")
print(f"User: {user_name}")