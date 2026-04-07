import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL_UI = os.getenv("BASE_URL_UI", "https://demo.applitools.com/")
BASE_URL_API = os.getenv("BASE_URL_API", "https://jsonplaceholder.typicode.com")

USERNAME = os.getenv("USERNAME","demoUser")
PASSWORD = os.getenv("PASSWORD","demoPass")

HEADLESS = os.getenv("HEADLESS","true").lower() == "true"
BROWSER = os.getenv("BROWSER","chromium")

ENV = os.getenv("ENV","dev")