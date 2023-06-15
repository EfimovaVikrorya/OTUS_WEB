from config import time_sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:

    def __init__(self, driver):
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

    def autorization(self):
        el_user = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-username")))
        el_user.send_keys("user")
        el_pwd = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password")))
        el_pwd.send_keys("eY49_PqZ")
        batton = WebDriverWait(self.driver, time_sleep.VERY_SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-key")))
        batton.click()
        el_profile = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-profile")))

    def menu_catalog(self):
        el_catalog = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#menu-catalog")))
        el_catalog.click()

    def menu_products(self):
        el_products = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#collapse1 a[href*="route=catalog/product"]')))
        el_products.click()

    def button_plus(self):
        btn_plus = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-plus")))
        btn_plus.click()

    def field_product_name(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-name1")))

    def field_meta_title(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-meta-title1")))

    def field_model(self):
        data = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.nav-tabs a[href*="#tab-data"]')))
        data.click()
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-model")))

    def save(self):
        btn_save = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-save")))
        btn_save.click()

    def field_product_name_serch(self):
        return WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#input-name")))

    def click_filter(self):
        btn_filter = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#button-filter")))
        btn_filter.click()

    def click_checkbox_element_for_delete(self):
        checkbox = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.table-responsive tbody input')))
        checkbox.click()

    def click_tresh(self):
        btn_tresh = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".fa-trash-o")))
        btn_tresh.click()


    def admin_logo(self):
        admin_logo = WebDriverWait(self.driver, time_sleep.SLOW, poll_frequency=1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#header-logo")))

