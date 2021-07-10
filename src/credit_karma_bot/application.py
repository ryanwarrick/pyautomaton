# from selenium.webdriver import ActionChains
import time
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
import keyring
from credit_karma_bot.pages import internal_page

from credit_karma_bot.pages.login_page import LoginPage
from credit_karma_bot.pages.internal_page import InternalPage


class Application(object):
    APP_NAME = "CreditKarma"
    BASE_URL = "https://www.creditkarma.com"

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(self.BASE_URL)
        # self.logged_in = False
        # self.login_page = LoginPage(self.driver)
        # self.internal_page = InternalPage(self.driver)

    def login(self, username: str):
        login_page = LoginPage(self.driver, self.wait, self.BASE_URL)
        login_page.navigate_driver_to_page()
        login_page.username_field().clear()
        login_page.username_field().send_keys(username)
        login_page.password_field().clear()
        password = keyring.get_password(self.APP_NAME, username)
        login_page.password_field().send_keys(password)
        login_page.submit_button().click()
        # Wait for a redirect to avoid prog flow issues
        self.wait.until(EC.url_to_be("https://www.creditkarma.com/today"))

    def get_credit_scores(self):
        internal_page = InternalPage(self.driver, self.wait, self.BASE_URL)
        scores = {}
        for credit_reporting_agency_name in internal_page.CREDIT_REPORTING_AGENCY_NAMES:
            internal_page.navigate_driver_to_scores_page(
                credit_reporting_agency_name)
            scores[credit_reporting_agency_name.capitalize(
            )] = internal_page.score_text().text
        return scores

    def get_credit_details(self):
        internal_page = InternalPage(self.driver, self.wait, self.BASE_URL)
        credit_details = {}
        for credit_reporting_agency_name in internal_page.CREDIT_REPORTING_AGENCY_NAMES:
            internal_page.navigate_driver_to_scores_page(
                credit_reporting_agency_name)
            credit_details[credit_reporting_agency_name.capitalize()] = {}
            for factor_tile_index in range(0, 5):
                factor_tile_detail = internal_page.factor_tile_detail(
                    factor_tile_index)
                credit_details[credit_reporting_agency_name.capitalize(
                )][factor_tile_detail['name']] = factor_tile_detail['value']
        return credit_details

    def logout(self):
        internal_page = InternalPage(self.driver, self.wait, self.BASE_URL)
        internal_page.logout_link()
        # ip.accept_alert_if_present()

    # def ensure_is_not_logged_in(self):
    #     assert self.login_page.is_this_page

    # def delete_all_cookies(self):
    #     self.delete_all_cookies()
