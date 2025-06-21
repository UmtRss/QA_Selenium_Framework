from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = "https://practicetestautomation.com/practice-test-login/"
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.ID, "submit")

    def load(self):
        self.open(self.url)

    def login(self, username, password):
        self.browser.find_element(*self.username_input).send_keys(username)
        self.browser.find_element(*self.password_input).send_keys(password)
        self.browser.find_element(*self.submit_button).click()
