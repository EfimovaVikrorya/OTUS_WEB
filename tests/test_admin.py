import time
import pytest
from page_object.AdminPage import AdminPage
from page_object.elements.AlertElement import AlertElement
from page_object.elements.HederElement import HederElement


@pytest.mark.ui
@pytest.mark.all
def test_admin_empty_credits(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    # найти поля ввода для юзернейма и пароля
    el_user = admin_page.field_username()
    el_pwd = admin_page.field_password()
    assert el_user.text == ''
    assert el_pwd.text == ''


@pytest.mark.ui
@pytest.mark.all
def test_admin_alias_invalid_password(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    # введение данных в поля юзернейм и пароль
    el_user = admin_page.field_username()
    el_user.send_keys('fghhgg')
    el_pwd = admin_page.field_password()
    el_pwd.send_keys('5678777')
    # нажать много раз кнопку Login
    for i in range(10):
        admin_page.click_button_login()
    # дождаться алерта варнинг
    el_alert = AlertElement(driver).find_alert_warning()
    assert el_alert.text == 'Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour or reset password.\n×'


@pytest.mark.ui
@pytest.mark.all
def test_admin_logo(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    # на странице есть лого
    admin_page.admin_logo()


@pytest.mark.ui
@pytest.mark.all
def test_admin_text_forgotten_password(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    #  найти  надпись "Forgotten Password"
    el = admin_page.text_forgotten_password()
    assert el.text == "Forgotten Password"


@pytest.mark.ui
@pytest.mark.all
def test_click_btn_login_when_enpty_credits(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    # найти кнопку "логин" и кликнуть
    el = admin_page.click_button_login()
    # появится алерта варнинг
    el_alert = AlertElement(driver).find_alert_warning()
    assert el_alert.text == 'No match for Username and/or Password.\n×'


@pytest.mark.ui
@pytest.mark.all
def test_add_new_product(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    admin_page.autorization()
    admin_page.menu_catalog()
    time.sleep(2)
    admin_page.menu_products()
    admin_page.button_plus()
    product_name = admin_page.field_product_name()
    product_name.send_keys("rurutt")
    meta_title = admin_page.field_meta_title()
    meta_title.send_keys("feehhgrr")
    model = admin_page.field_model()
    model.send_keys("fhjhhgff")
    admin_page.save()
    el_alert = AlertElement(driver).find_alert_success()
    assert el_alert.text == "Success: You have modified products!\n×"


@pytest.mark.ui
@pytest.mark.check
def test_delete_product(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    admin_page.autorization()
    admin_page.menu_catalog()
    time.sleep(2)
    admin_page.menu_products()
    product_name_search = admin_page.field_product_name_search()
    time.sleep(2)
    product_name_search.send_keys("rurutt")
    admin_page.click_filter()
    admin_page.click_checkbox_element_for_delete()
    time.sleep(3)
    admin_page.click_tresh()
    driver.switch_to.alert.accept()
    el_alert = AlertElement(driver).find_alert_success()
    assert el_alert.text == "Success: You have modified products!\n×"
