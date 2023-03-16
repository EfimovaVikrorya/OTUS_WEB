from config import time_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CatalogPage:

    def __init__(self,driver):
        self.driver = driver

    def open_page(self):
        PAGE_NAME = "/apple"
        self.driver.get(self.driver.url + PAGE_NAME)

    def brend(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))

    def element_on_the_page(self):
        return WebDriverWait(self.driver, time_sleep.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))


    def dropdown_of_sort(self):
        return WebDriverWait(self.driver, time_sleep.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-sort")))


    def dropdown_of_limit(self):
        return WebDriverWait(self.driver, time_sleep.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-limit")))


    def product_compare(self):
        el = WebDriverWait(self.driver, time_sleep.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#compare-total")))
        el.click()


    def product_comparison(self):
        return WebDriverWait(self.driver, time_sleep.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content")))