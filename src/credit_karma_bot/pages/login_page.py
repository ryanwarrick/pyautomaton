from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

from credit_karma_bot.pages.page import Page


class LoginPage(Page):
    PAGE_PATH = "auth/logon/"

    def __init__(self, driver):
        super().__init__(driver, page_path=self.PAGE_PATH)

    @property
    def username_field(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        return self.driver.find_element_by_id("username")

    @property
    def password_field(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "password")))
        return self.driver.find_element_by_id("password")

    @property
    def submit_button(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "Logon")))
        return self.driver.find_element_by_id("Logon")

    @property
    def is_this_page(self):
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.Class, "login-body")))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

    # @property
    # def is_this_base_page(self):
    #     try:
    #         self.wait.until(EC.presence_of_element_located(
    #             (By.ID, "gmail-sign-in")))
    #         return True
    #     except NoSuchElementException:
    #         return False
    #     except TimeoutException:
    #         return False
