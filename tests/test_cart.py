from page_object.CartPage import CartPage
from page_object.elements.AlertElement import AlertElement
from page_object.elements.HederElement import HederElement
import time


def test_cart_text_description(driver):
    cart_page = CartPage(driver)
    cart_page.open_page()
    # описание продукта
    el = cart_page.descrirtion()
    assert el.text == 'iPhone is a revolutionary new mobile phone that allows you to make a call by ' \
                      'simply tapping a name or number in your address book, a favorites list, or a ' \
                      'call log. It also automatically syncs all your contacts from a PC, Mac, or ' \
                      'Internet service. And it lets you select and listen to voicemail messages in ' \
                      'whatever order you want just like email.'


def test_cart_alert_success(driver):
    cart_page = CartPage(driver)
    cart_page.open_page()
    #  добавление в корзину
    cart_page.add_to_cart()
    # появление успешного алерта
    alert = AlertElement(driver).find_alert_success()
    assert alert.text == "Success: You have added iPhone to your shopping cart!\n×"


def test_cart_item_in_sopping_cart(driver):
    cart_page = CartPage(driver)
    cart_page.open_page()
    # добавление в корзину
    cart_page.add_to_cart()
    time.sleep(3)
    # отображение в корзине сверху
    btn_item = HederElement(driver).items_in_cart()
    assert btn_item.text == '1 item(s) - $123.20'


def test_cart_item_reset(driver):
    cart_page = CartPage(driver)
    cart_page.open_page()
    # добавление продукта в корзину
    cart_page.add_to_cart()
    time.sleep(3)
    # отображение в корзине сверху
    btn_item = HederElement(driver).items_in_cart()
    assert btn_item.text == '1 item(s) - $123.20'
    btn_item.click()
    #  удаление продукта
    btn_delete = cart_page.delete_from_cart()
    time.sleep(3)
    # отображение в корзине сверху
    btn_item = HederElement(driver).items_in_cart()
    assert btn_item.text == '0 item(s) - $0.00'


def test_cart_rating(driver):
    cart_page = CartPage(driver)
    cart_page.open_page()
    # рейтинг
    el = cart_page.rating()
    assert el.text == '0 reviews / Write a review\nTweet\nShare'
