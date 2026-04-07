import pytest
from src.fixtures.ui_fixture import ui_page,browser_instance
from playwright.sync_api import Page
from src.fixtures.api_fixture import api_client
from src.utils.utils_logger import get_logger

logger = get_logger(__name__)

def pytest_configure(config):
    logger.info("="*50)
    logger.info("Intelligent systems QA - Test Suite starting !")
    logger.info("="*50)

def pytest_terminal_summary(terminalreporter):
    try:
        passed = len(terminalreporter.stats.get("passed", []))
        failed = len(terminalreporter.stats.get("failed", []))
        total = passed + failed

        logger.info("=" * 50)
        logger.info(f"Total : {total}")
        logger.info(f"Passed : {passed}")
        logger.info(f"Failed : {failed}")

        if total > 0:
            rate = round(passed / total * 100, 2)
            logger.info(f"Rate : {rate}%")

        logger.info("=" * 50)
    except Exception:
        # Prevent pytest from crashing due to closed stdout
        pass