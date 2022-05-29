import os

from dotenv import load_dotenv


load_dotenv()

database_info = {
    "database": str(os.getenv("DATABASE_NAME")),
    "host": str(os.getenv("MONGO_URL")),
}
