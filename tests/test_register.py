from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PAGE_NAME = "/index.php?route=account/register"


class Config:
    FAST = 1
    NORM = 2
    SLOW = 3
    VERY_SLOW = 4


def test_register_account(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
    assert el.text == "Account Register"


def test__register_not_checkbox_privacy_policy(driver):
    driver.get(driver.url + PAGE_NAME)
    el_first_name = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    el_first_name.send_keys("Ivan")
    el_last_name = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    el_last_name.send_keys("Ivanov")
    el_email = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    el_email.send_keys("ivanov@example.com")
    el_phone = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))
    el_phone.send_keys("12345")
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    el_pwd.send_keys("12345")
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-confirm")))
    el_pwd.send_keys("12345")
    el_btn_cont = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
    el_btn_cont.click()
    el_alert = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    assert el_alert.text == "Warning: You must agree to the Privacy Policy!"


def test__register_invalid_phone(driver):
    driver.get(driver.url + PAGE_NAME)
    el_first_name = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    el_first_name.send_keys("Ivan")
    el_last_name = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    el_last_name.send_keys("Ivanov")
    el_email = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    el_email.send_keys("ivanov@example.com")
    el_phone = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))
    el_phone.send_keys("12")
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    el_pwd.send_keys("12345")
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-confirm")))
    el_pwd.send_keys("12345")
    el_btn_cont = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
    el_btn_cont.click()
    el_alert = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-danger")))
    assert el_alert.text == "Telephone must be between 3 and 32 characters!"


def test__register_invalid_email(driver):
    driver.get(driver.url + PAGE_NAME)
    el_first_name = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    el_first_name.send_keys("Ivan")
    el_last_name = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    el_last_name.send_keys("Ivanov")
    el_email = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    el_email.send_keys("ivanov@example")
    el_phone = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))
    el_phone.send_keys("1245")
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    el_pwd.send_keys("12345")
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-confirm")))
    el_pwd.send_keys("12345")
    el_btn_cont = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
    el_btn_cont.click()
    el_alert = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-danger")))
    assert el_alert.text == "E-Mail Address does not appear to be valid!"


def test__register_invalid_confirm_pwd(driver):
    driver.get(driver.url + PAGE_NAME)
    el_first_name = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))
    el_first_name.send_keys("Ivan")
    el_last_name = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))
    el_last_name.send_keys("Ivanov")
    el_email = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-email")))
    el_email.send_keys("ivanov@example.com")
    el_phone = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-telephone")))
    el_phone.send_keys("1245")
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-password")))
    el_pwd.send_keys("12345")
    el_pwd = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-confirm")))
    el_pwd.send_keys("")
    el_btn_cont = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary")))
    el_btn_cont.click()
    el_alert = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-danger")))
    assert el_alert.text == "Password confirmation does not match password!"
