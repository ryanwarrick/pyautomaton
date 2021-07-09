from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from urllib.parse import urljoin


class Page(object):
    BASE_URL = "https://www.creditkarma.com"

    def __init__(self, driver: webdriver, page_path=None):
        self.driver = driver
        self.page_path = page_path
        self.wait = WebDriverWait(driver, 20)
        # self.driver.get(self.url)

    @property
    def url(self):
        if self.page_path is not None:
            return urljoin(self.BASE_URL, self.page_path)
        else:
            return None

    def get_page(self):
        print(self.url)
        self.driver.get(self.url)

    def wait_for_element_presence(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def is_element_visible(self, locator):
        try:
            self.wait.until(visibility_of_element_located(locator))
            return True
        except WebDriverException:
            return False

    def is_element_present(self, *locator):
        try:
            self.wait.until(EC.presence_of_element_located(*locator))
            return True
        except NoSuchElementException:
            return False
        finally:
            self.wait.until(EC.presence_of_element_located(*locator))
