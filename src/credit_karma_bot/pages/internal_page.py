import sys

from credit_karma_bot.locators import LoginPageLocators
from credit_karma_bot.locators import InternalPageLocators
from credit_karma_bot.pages.page import BasePage

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException


class InternalPage(BasePage):
    SCORE_PAGE_PATH = "credit-health/{credit_reporting_agency_name}/factors/"
    CREDIT_REPORTING_AGENCY_NAMES = [
        "transunion",
        "equifax"
    ]

    def __init__(self, driver, wait, base_url):
        super().__init__(driver, wait, base_url)
        # self.page_path = InternalPage.SCORE_PAGE_PATH

    def navigate_driver_to_scores_page(self, credit_reporting_agency_name):
        self.page_path = self.SCORE_PAGE_PATH.format(
            credit_reporting_agency_name=credit_reporting_agency_name)
        self.driver.get(self.url())
        try:
            if not self.is_this_page():
                raise RuntimeError(
                    "Expected 'internal page', but current page determined to not be an 'internal page'.")
        except RuntimeError as err:
            print("Loading of 'internal page' detected as unsuccessful. Aborting.")
            print(err)
            self.driver.quit()
            sys.exit(1)

    def logout_link(self):
        return self.driver.get("https://www.creditkarma.com/auth/logout/lockdown")

    def score_text_alt(self):
        return self.fetch_element(InternalPageLocators.score_text)

    def is_this_page(self):
        return super().is_this_page(
            InternalPageLocators.internal_page_identifier)
