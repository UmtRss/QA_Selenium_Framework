from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def find (self, locator):
        return self.browser.find_element(*locator)

    def finds(self, locator):
        return self.browser.find_elements(*locator)