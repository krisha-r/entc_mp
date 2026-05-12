from supabase import create_client, Client
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def register_user(username, password, dob):
    if username is None or password is None:
        return False
    hashed_password = generate_password_hash(password)
    data = {
        "username": username,
        "password": hashed_password,
        "dob": dob
    }
    response = supabase.table("Users").insert(data).execute()
    return response
