from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PAGE_NAME = "/apple"


class Config:
    FAST = 1
    NORM = 2
    SLOW = 3
    VERY_SLOW = 4


def test_catalog_brand_name(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.SLOW, poll_frequency=1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
    assert el.text == 'Brand Apple'


def test_catalog_brand_items(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-layout")))
    assert len(el) == 10


def test_catalog_sort(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-sort")))
    assert (el.text == '                                          Default\n' +
            '                                                        Name (A - Z)\n' +
            '                                                        Name (Z - A)\n' +
            '                                                        Price (Low > High)\n' +
            '                                                        Price (High > Low)\n' +
            '                                                        Rating (Highest)\n' +
            '                                                        Rating (Lowest)\n' +
            '                                                        Model (A - Z)\n' +
            '                                                        Model (Z - A)\n' +
            '                                        \n'
            '            ')


def test_catalog_limit(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-limit")))
    assert (el.text == '                                          15\n' +
            '                                                        25\n' +
            '                                                        50\n' +
            '                                                        75\n' +
            '                                                        100\n' +
            '                                        \n' +
            '            ')


def test_catalog_compare(driver):
    driver.get(driver.url + PAGE_NAME)
    el = WebDriverWait(driver, Config.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#compare-total")))
    el.click()
    el_cont = WebDriverWait(driver, Config.VERY_SLOW, poll_frequency=1).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#content")))
    assert el_cont.text == "Product Comparison\nYou have not chosen any products to compare.\nContinue"
