from page_object.RegisterPage import RegisterPage
from page_object.elements.AlertElement import AlertElement
import time
import pytest


@pytest.mark.ui
@pytest.mark.all
def test_register_account(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    #  надпись где домик
    el = register_page.house()
    assert el.text == "Account Register"


@pytest.mark.ui
@pytest.mark.all
def test__register_not_checkbox_privacy_policy(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    # поле ввода firstname
    el_first_name = register_page.set_firstname()
    el_first_name.send_keys("Ivan")
    #  поле ввода lastname
    el_last_name = register_page.set_lastname()
    el_last_name.send_keys("Ivanov")
    #  поле ввода email
    el_email = register_page.set_email()
    el_email.send_keys("ivanov@example.com")
    #  поле вввода телефон
    el_phone = register_page.set_telephone()
    el_phone.send_keys("12345")
    #  поле ввода пароля
    el_pwd = register_page.set_confirm_password()
    el_pwd.send_keys("12345")
    #  поле ввода подтвержения пароля
    el_pwd = register_page.set_confirm_password()
    el_pwd.send_keys("12345")
    #  кнопка континью и клик на нее
    register_page.click_btn_continue()
    #  алерта ванринг
    el_alert = AlertElement(driver).find_alert_warning()
    assert el_alert.text == "Warning: You must agree to the Privacy Policy!"


@pytest.mark.ui
@pytest.mark.all
def test__register_invalid_phone(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    el_first_name = register_page.set_firstname()
    el_first_name.send_keys("Ivan")
    el_last_name = register_page.set_lastname()
    el_last_name.send_keys("Ivanov")
    el_email = register_page.set_email()
    el_email.send_keys("ivanov@example.com")
    el_phone = register_page.set_telephone()
    el_phone.send_keys("12")
    el_pwd = register_page.set_password()
    el_pwd.send_keys("12345")
    el_pwd = register_page.set_confirm_password()
    el_pwd.send_keys("12345")
    el_btn_cont = register_page.click_btn_continue()
    #  алерта текст данжер
    el_alert = AlertElement(driver).find_text_danger()
    assert el_alert.text == "Telephone must be between 3 and 32 characters!"


@pytest.mark.ui
@pytest.mark.all
def test__register_invalid_email(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    el_first_name = register_page.set_firstname()
    el_first_name.send_keys("Ivan")
    el_last_name = register_page.set_lastname()
    el_last_name.send_keys("Ivanov")
    el_email = register_page.set_email()
    el_email.send_keys("ivanov@example")
    el_phone = register_page.set_telephone()
    el_phone.send_keys("1245")
    el_pwd = register_page.set_password()
    el_pwd.send_keys("12345")
    el_pwd = register_page.set_confirm_password()
    el_pwd.send_keys("12345")
    el_btn_cont = register_page.click_btn_continue()
    #  алерта текст данжер
    el_alert = AlertElement(driver).find_text_danger()
    assert el_alert.text == "E-Mail Address does not appear to be valid!"


@pytest.mark.ui
@pytest.mark.all
def test__register_invalid_confirm_pwd(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    el_first_name = register_page.set_firstname()
    el_first_name.send_keys("Ivan")
    el_last_name = register_page.set_lastname()
    el_last_name.send_keys("Ivanov")
    el_email = register_page.set_email()
    el_email.send_keys("ivanov@example.com")
    el_phone = register_page.set_telephone()
    el_phone.send_keys("1245")
    el_pwd = register_page.set_password()
    el_pwd.send_keys("12345")
    el_pwd = register_page.set_confirm_password()
    el_pwd.send_keys("")
    el_btn_cont = register_page.click_btn_continue()
    #  алерта текст данжер
    el_alert = AlertElement(driver).find_text_danger()
    assert el_alert.text == "Password confirmation does not match password!"


@pytest.mark.ui
@pytest.mark.all
def test__register_user(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    el_first_name = register_page.set_firstname()
    el_first_name.send_keys("ttte22")
    el_last_name = register_page.set_lastname()
    el_last_name.send_keys("ttte2")
    el_email = register_page.set_email()
    el_email.send_keys("te2tt@example.com")
    el_phone = register_page.set_telephone()
    el_phone.send_keys("15555")
    el_pwd = register_page.set_password()
    el_pwd.send_keys("qwer")
    el_pwd = register_page.set_confirm_password()
    el_pwd.send_keys("qwer")
    el_checkbox = register_page.agree()
    el_btn_cont = register_page.click_btn_continue()
    el_congr = register_page.congradulations()
