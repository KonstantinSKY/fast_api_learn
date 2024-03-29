from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

SECRET_AUTH_TOKEN = os.environ.get("SECRET_AUTH")
SECRET_RESET_TOKEN = os.environ.get("SECRET_RESET_PASSW")
SECRET_VERIFICATION_TOKEN = os.environ.get("SECRET_VERIFICATION_AUTH")