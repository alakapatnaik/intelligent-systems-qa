import pytest
from playwright.sync_api import sync_playwright,Page,Browser
from src.config.settings import BASE_URL_UI, HEADLESS, BROWSER
from src.utils.utils_logger import get_logger


logger = get_logger(__name__)

@pytest.fixture(scope = "session")
def browser_instance():
    logger.info("Launching Browser...")
    with sync_playwright() as p:
        browser = getattr(p,BROWSER).launch(headless = HEADLESS)
        logger.info(f"Browser launched: {BROWSER}")
        yield browser
        logger.info("closing browser...")
        browser.close()

@pytest.fixture(scope = "function")
def ui_page(browser_instance: Browser) -> Page:
    context = browser_instance.new_context()
    page = context.new_page()
    page.goto(BASE_URL_UI, wait_until="load")
    logger.info(f"navigates to : {BASE_URL_UI}")
    yield page
    logger.info("Closing page...")
    context.close()
    

