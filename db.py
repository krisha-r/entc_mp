from supabase import create_client, Client, AuthApiError
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash


load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def register_user(username, password):
    if username is None or password is None:
        return False
    hashed_password = generate_password_hash(password)
    data = {
        "username": username,
        "password": hashed_password,
    }
    response = supabase.table("Users").insert(data).execute()
    return response


def login_user(username, password):
    if username is None or password is None:
        return False
    try:
        response = supabase.table("Users").select("*").eq("username", username).single().execute()
        response = response.data
        return check_password_hash(response["password"], password)
    except:
        return False
    