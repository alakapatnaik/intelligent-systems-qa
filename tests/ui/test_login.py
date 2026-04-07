import pytest
from src.pages.login_page import LoginPage
from src.config.settings import USERNAME, PASSWORD


# -----------------------------
# 1. Verify Login Page Loads
# -----------------------------
def test_verify_login_page_loaded(ui_page):
    login_page = LoginPage(ui_page)

    assert "demo.applitools.com" in login_page.get_url()
    assert login_page.is_visible(login_page.username_input)
    assert login_page.is_visible(login_page.password_input)


# -----------------------------
# 2. Valid Login Test
# -----------------------------
def test_valid_login(ui_page):
    login_page = LoginPage(ui_page)

    login_page.login(USERNAME, PASSWORD)

    assert login_page.is_logged_in()


# -----------------------------
# 3. Verify Username Field Input
# -----------------------------
def test_enter_username(ui_page):
    login_page = LoginPage(ui_page)

    login_page.enter_email("testUser")

    value = login_page.get_value(login_page.username_input)
    assert value == "testUser"


# -----------------------------
# 4. Verify Password Field Input
# -----------------------------
def test_enter_password(ui_page):
    login_page = LoginPage(ui_page)

    login_page.enter_password("testPass")

    value = login_page.get_value(login_page.password_input)
    assert value == "testPass"


# -----------------------------
# 5. Verify Remember Me Checkbox
# -----------------------------
def test_remember_me_checkbox(ui_page):
    login_page = LoginPage(ui_page)

    login_page.check_remember_me()

    assert login_page.remember_me.is_checked()