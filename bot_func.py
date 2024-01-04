from dotenv import load_dotenv
import os


def get_token_env():
    load_dotenv(
        dotenv_path=".env",
    )
    token = os.getenv("BOT_TOKEN")
    return token
