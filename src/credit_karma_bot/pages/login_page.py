import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from credit_karma_bot.pages.page import BasePage
from credit_karma_bot.locators import LoginPageLocators


class LoginPage(BasePage):

    PAGE_PATH = "auth/logon/"

    def __init__(self, driver: webdriver, wait: WebDriverWait, base_url: str):
        super().__init__(driver, wait, base_url)
        self.page_path = LoginPage.PAGE_PATH

    def navigate_driver_to_page(self):
        self.driver.get(self.url())
        try:
            if not self.is_this_page():
                raise RuntimeError(
                    "Expected 'login page', but current page determined to not be login page.")
        except RuntimeError as err:
            print("Loading of login page detected as unsuccessful. Aborting.")
            print(err)
            self.driver.quit()
            sys.exit(1)

    def username_field(self):
        return self.fetch_element(LoginPageLocators.username_field)

    def password_field(self):
        return self.fetch_element(LoginPageLocators.password_field)

    def submit_button(self):
        return self.fetch_element(LoginPageLocators.submit_button)

    def is_this_page(self):
        return super().is_this_page(LoginPageLocators.login_page_identifier)
