import sys

from credit_karma_bot.locators import InternalPageLocators, LoginPageLocators
from credit_karma_bot.pages.page import BasePage
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException,
                                        TimeoutException, WebDriverException)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class InternalPage(BasePage):
    SCORE_PAGE_PATH = "credit-health/{credit_reporting_agency_name}/factors/"
    CREDIT_REPORTING_AGENCY_NAMES = [
        "transunion",
        "equifax"
    ]

    def __init__(self, driver, wait, base_url):
        super().__init__(driver, wait, base_url)

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

    def get_score_text(self):
        return self.fetch_element(InternalPageLocators.score_text).text

    def get_factor_tile_details(self, index):
        factor_tile = self.get_factor_tile(index)
        factor_tile_details = {}
        for key, value in InternalPageLocators.factor_tile_detail.items():
            # Exception has occurred: AttributeError
            # 'WebElement' object has no attribute 'fetch_element'
            factor_tile_detail = factor_tile.find_element(*value)
            factor_tile_details[key] = factor_tile_detail.text
        return factor_tile_details

    def get_factor_tile(self, index):
        # TODO: Break this out and represent it in OOP form in element.py
        # https://github.com/jdi-testing/jdi-python/tree/master/JDI/web/selenium/elements/base
        factor_tile = self.fetch_elements(
            InternalPageLocators.factor_tiles)[index]
        return factor_tile

    def logout(self):
        return self.driver.get("https://www.creditkarma.com/auth/logout/lockdown")

    def is_this_page(self):
        return super().is_this_page(
            InternalPageLocators.internal_page_identifier)
