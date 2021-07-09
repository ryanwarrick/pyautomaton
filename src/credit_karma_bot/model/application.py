# from gmail.pages.internal_page import InternalPage
# from selenium.webdriver import ActionChains
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
import keyring

from credit_karma_bot.pages.login_page import LoginPage
from credit_karma_bot.pages.internal_page import InternalPage


class Application(object):
    APP_NAME = "CreditKarma"

    def __init__(self, driver: webdriver):
        # driver.get(base_url)
        # self.wait = WebDriverWait(self.driver, 20)
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.internal_page = InternalPage(self.driver)
        # self.logged_in = False

    def login(self, username: str):
        self.login_page.get_page()
        self.login_page.username_field.clear()
        self.login_page.username_field.send_keys(username)
        self.login_page.password_field.clear()
        password = keyring.get_password(self.APP_NAME, username)
        self.login_page.password_field.send_keys(password)
        self.login_page.submit_button.click()
        # self.logged_in = True

    # def ensure_is_logged_in(self):
    #     return self.internal_page.is_this_page

    def get_credit_scores(self):
        self.internal_page.page_path = "today/"
        self.internal_page.get_page()
        self.internal_page.is_this_page
        # TODO: Build out real selenium logic here based on working logic from other.py file
        scores = []
        for credit_reporting_agency_name in self.internal_page.CREDIT_REPORTING_AGENCY_NAMES:
            self.internal_page.page_path = self.internal_page.SCORE_PAGE_PATH.format(
                credit_reporting_agency_name=credit_reporting_agency_name)
            self.internal_page.get_page()
            scores.append(self.internal_page.score_text.text)
        return scores

    def logout(self):
        ip = self.internal_page
        ip.logout_link()
        # ip.accept_alert_if_present()

    def ensure_is_not_logged_in(self):
        assert self.login_page.is_this_page

    # def go_to_sign_in_form(self):
    #     lp = self.login_page
    #     if lp.sign_in_links:
    #         lp.sign_in_links[0].click()

    def delete_all_cookies(self):
        self.delete_all_cookies()
