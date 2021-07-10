import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import MaxRetryError
from urllib.parse import urljoin


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver: webdriver, wait: WebDriverWait, base_url):
        self.driver = driver
        self.wait = wait
        self.base_url = base_url
        self.page_path = None

    def fetch_element(self, locator):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator))
            return element
        except MaxRetryError as err:
            print("Failed to find element...")
            print(err)
            print(err.args)
            self.driver.quit()
            sys.exit(1)
        except TimeoutException as err:
            print("Failed to find element...")
            print(err)
            print(err.args)
            self.driver.quit()
            sys.exit(1)

    def url(self):
        if self.page_path is not None:
            print(urljoin(self.base_url, self.page_path))
            return urljoin(self.base_url, self.page_path)
        else:
            return None

    def get_page(self):
        print(self.url())
        self.driver.get(self.url())

    def is_this_page(self, page_unique_locator: tuple):
        try:
            WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located(page_unique_locator))
            # self.wait.until(EC.presence_of_element_located(
            #     page_unique_locator))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

    # def wait_for_element_presence(self, locator):
    #     self.wait.until(EC.presence_of_element_located(locator))

    # def is_element_visible(self, locator):
    #     try:
    #         self.wait.until(visibility_of_element_located(locator))
    #         return True
    #     except WebDriverException:
    #         return False

    # def is_element_present(self, *locator):
    #     try:
    #         self.wait.until(EC.presence_of_element_located(*locator))
    #         return True
    #     except NoSuchElementException:
    #         return False
    #     finally:
    #         self.wait.until(EC.presence_of_element_located(*locator))
