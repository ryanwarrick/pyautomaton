from credit_karma_bot.pages.page import Page

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException


class InternalPage(Page):
    SCORE_PAGE_PATH = "credit-health/{credit_reporting_agency_name}/factors/"
    CREDIT_REPORTING_AGENCY_NAMES = [
        "transunion",
        "equifax"
    ]

    def __init__(self, driver):
        super().__init__(driver)

    def logout_link(self):
        return self.driver.get("https://www.creditkarma.com/auth/logout/lockdown")

    @property
    def score_text(self):
        score_xpath = '//*[@id = "__render-farm"]//*[@class = "credit-health"]/div[1]//*[@class = "section-content"]/div[1]/div[1]/div[1]/div[1]//*[name() = "svg"]/*[name() = "text"][position() = (last() - 1)]'
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, score_xpath)))
        return self.driver.find_element_by_xpath(score_xpath)

    @property
    def is_this_page(self):
        try:
            self.wait.until(EC.presence_of_element_located(
                (By.ID, 'top-nav')))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
