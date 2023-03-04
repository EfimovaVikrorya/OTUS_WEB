from page_object.AdminPage import AdminPage
from page_object.elements.AlertElement import AlertElement
from page_object.elements.HederElement import HederElement


def test_admin_empty_credits(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    # найти поля ввода для юзернейма и пароля
    el_user = admin_page.field_username()
    el_pwd = admin_page.field_password()
    assert el_user.text == ''
    assert el_pwd.text == ''


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


def test_admin_logo(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    # на странице есть лого
    HederElement(driver).logo()


def test_admin_text_forgotten_password(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    #  найти  надпись "Forgotten Password"
    el = admin_page.text_forgotten_password()
    assert el.text == "Forgotten Password"


def test_click_btn_login_when_enpty_credits(driver):
    admin_page = AdminPage(driver)
    admin_page.open_page()
    # найти кнопку "логин" и кликнуть
    el = admin_page.click_button_login()
    # появится алерта варнинг
    el_alert = AlertElement(driver).find_alert_warning()
    assert el_alert.text == 'No match for Username and/or Password.\n×'
