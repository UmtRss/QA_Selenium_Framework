from login_page import LoginPage
import pytest

def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("wronguser", " wrongpass")


    error_message = browser.find_element ("id", "error").text
    assert "Your username is invalid!" in error_message

    