from playwright.sync_api import Page, Locator
from src.utils.utils_logger import get_logger

logger = get_logger(__name__)

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # ---------------------------
    # Element Actions
    # ---------------------------
    def click(self, locator):
        locator.click() if isinstance(locator, Locator) else self.page.click(locator)

    def fill(self, locator, value: str):
        locator.fill(value) if isinstance(locator, Locator) else self.page.fill(locator, value)

    def is_visible(self, locator):
        return locator.is_visible() if isinstance(locator, Locator) else self.page.is_visible(locator)

    def get_value(self, locator):
        return locator.input_value() if isinstance(locator, Locator) else self.page.input_value(locator)

    def is_checked(self, locator):
        return locator.is_checked() if isinstance(locator, Locator) else self.page.is_checked(locator)

    def get_url(self):
        return self.page.url
