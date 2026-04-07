import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL_UI = os.getenv("BASE_URL_UI")
BASE_URL_API = os.getenv("BASE_URL_API")

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

HEADLESS = os.getenv("HEADLESS","true").lower() == "true"
BROWSER = os.getenv("BROWSER","chromium")

ENV = os.getenv("ENV","dev")