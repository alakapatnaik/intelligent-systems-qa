from playwright.sync_api import Page
from src.utils.utils_logger import get_logger
from src.pages.base_page import BasePage

logger = get_logger(__name__)

class LoginPage(BasePage):

    @property
    def username_input(self):
        return self.page.locator("#username")

    @property
    def password_input(self):
        return self.page.locator("#password")

    @property
    def signin_button(self):
        return self.page.locator("#log-in")   # FIXED

    @property
    def remember_me(self):
        return self.page.get_by_label("Remember Me")

    def __init__(self, page: Page):
        super().__init__(page)
        logger.info("Login page initialized")

    def enter_email(self, username: str):
        logger.info(f"Entering email: {username}")
        self.username_input.fill(username)

    def enter_password(self, password: str):
        logger.info(f"Entering password: {password}")
        self.password_input.fill(password)

    def click_signin(self):
        logger.info("Clicking signin button")
        self.signin_button.click()

    def check_remember_me(self):
        logger.info("Checking remember me")
        self.remember_me.check()

    def login(self, username: str, password: str):
        self.enter_email(username)
        self.enter_password(password)
        self.click_signin()
        logger.info("Login attempted!")

    def is_logged_in(self):
        return "app" in self.page.url
