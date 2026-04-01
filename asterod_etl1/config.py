import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "nasa"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "Babajana123"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}