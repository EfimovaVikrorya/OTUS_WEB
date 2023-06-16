from page_object.MainPage import MainPage
from page_object.elements.HederElement import HederElement
from page_object.elements.AlertElement import AlertElement
from selenium.webdriver.support.ui import Select
import time
import pytest


# @pytest.mark.ui
# @pytest.mark.all
# def test_main_currency(driver):
#     main_page = MainPage(driver)
#     main_page.open_page()
#     # надпись валюта
#     el = HederElement(driver).currency()
#     time.sleep(100)
#     assert el.text == "Currency"


@pytest.mark.ui
@pytest.mark.all
def test_check_currency(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    el_BRP = HederElement(driver).GBP_currency()
    assert el_BRP.text == "£"
    el_EUR = HederElement(driver).Euro_currency()
    assert el_EUR.text == "€"
    el_USD = HederElement(driver).USD_currency()
    assert el_USD.text == '$'


@pytest.mark.ui
@pytest.mark.all
def test_main_logo(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    # лого
    HederElement(driver).logo()


@pytest.mark.ui
@pytest.mark.all
def test_main_sopping_cart(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    #  клик по корзине сверху
    el = HederElement(driver).shopping_cart()
    el.click()
    # надпись
    el1 = AlertElement(driver).find_alert_shopping_cart_empty()
    time.sleep(100)
    assert el1.text == "Shopping Cart\nYour shopping cart is empty!\nContinue"


@pytest.mark.ui
@pytest.mark.all
def test_main_search(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    #  поле поиска продукта
    el = HederElement(driver).field_serch()
    assert el.text == ""


@pytest.mark.ui
@pytest.mark.all
def test_main_acccount(driver):
    main_page = MainPage(driver)
    main_page.open_page()
    #  клик по знаку телефона
    el = HederElement(driver).phone()
    el.click()
    # открытие формы контактные данные
    el = main_page.form_contact_us()
    assert el.text == ('Contact Us\n'
                       'Our Location\n'
                       'Your Store\n'
                       'Address 1\n'
                       'Telephone\n'
                       '123456789\n'
                       '\n'
                       'Contact Form\n'
                       'Your Name\n'
                       'E-Mail Address\n'
                       'Enquiry')
