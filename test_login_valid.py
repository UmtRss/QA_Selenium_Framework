from login_page import LoginPage
import time

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("student", "Password123")

    success_message = browser.find_element("xpath", "//h1").text
    assert "Logged In Successfully" in success_message