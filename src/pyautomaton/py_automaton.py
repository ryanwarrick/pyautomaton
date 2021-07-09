import sys

from selenium import webdriver

from credit_karma_bot.model.application import Application as CreditKarmaApp


class PyAutomatonMgr(object):

    def __init__(self):
        self.name = "name"

    def review_credit_karma(self, username):
        driver = webdriver.Chrome()
        credit_karma_app = CreditKarmaApp(driver)
        credit_karma_app.login(username)
        credit_scores = credit_karma_app.get_credit_scores()
        print(credit_scores)
        credit_karma_app.logout()