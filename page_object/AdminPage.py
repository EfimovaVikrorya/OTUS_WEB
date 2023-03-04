from config import time_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:

    def __init__(self,driver):
        self.driver = driver

    def open_page(self):
        PAGE_NAME = "/admin"
        self.driver.get(self.driver.url + PAGE_NAME)

    def field_username(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-username")))


    def field_password(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password")))


    def click_button_login(self):
        batton = WebDriverWait(self.driver, time_sleep.VERY_SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-key")))
        batton.click()


    def text_forgotten_password(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".help-block")))