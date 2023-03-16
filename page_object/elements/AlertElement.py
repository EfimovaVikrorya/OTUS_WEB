from config import TimeSleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertElement:
    def __init__(self, driver):
        self.driver = driver

    def find_alert_warning(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

    def find_text_danger(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-danger")))

    def find_alert_success(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success")))

    def find_alert_shopping_cart_empty(self):
        return WebDriverWait(self.driver, time_sleep.VERY_SLOW, poll_frequency=1).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".col-sm-12")))
