import sys
from pprint import pprint

from selenium import webdriver

from credit_karma_bot.application import Application as CreditKarmaApp


class PyAutomatonMgr(object):

    def __init__(self):
        self.name = "name"

    def review_credit_karma(self, username):
        driver = webdriver.Chrome()
        credit_karma_app = CreditKarmaApp(driver)
        credit_karma_app.login(username)
        credit_scores = credit_karma_app.get_credit_scores()
        pprint(credit_scores)
        credit_details = credit_karma_app.get_credit_details()
        pprint(credit_details)
        credit_karma_app.logout()
