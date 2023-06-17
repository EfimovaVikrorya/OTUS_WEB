import allure
import pytest
import requests
import conftest


@pytest.mark.api
@pytest.mark.all
def test_currency(api_token, config):
    r = requests.post(f"{config['base_url']}api/currency",
                      params={"api_token": api_token}, data={"currency": "USD"})
    assert r.status_code == 200


@pytest.mark.api
@pytest.mark.all
def test_add_to_cart_one_product(api_token, config):
    add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
                                params={"api_token": api_token}, data={"product_id": "43", "quantity": "1"})
    assert add_to_cart.status_code == 200
    list_in_cart = requests.post(f"{config['base_url']}api/cart/products",
                                 params={"api_token": api_token}, data={})
    assert list_in_cart.status_code == 200
    row = list_in_cart.json()
    assert row['products'][0]['product_id'] == '43'
    assert row['products'][0]['quantity'] == '1'


@pytest.mark.api
@pytest.mark.all
def test_add_to_cart_double(api_token, config):
    add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
                                params={"api_token": api_token}, data={"product_id": "31", "quantity": "1"})
    assert add_to_cart.status_code == 200
    add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
                                params={"api_token": api_token}, data={"product_id": "31", "quantity": "1"})
    assert add_to_cart.status_code == 200
    list_in_cart = requests.post(f"{config['base_url']}api/cart/products",
                                 params={"api_token": api_token}, data={})
    assert list_in_cart.status_code == 200
    row = list_in_cart.json()
    assert row['products'][0]['product_id'] == '31'
    assert row['products'][0]['quantity'] == '2'


@pytest.mark.api
@pytest.mark.all
def test_delete_product(api_token, config):
    add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
                                params={"api_token": api_token}, data={"product_id": "44", "quantity": "1"})
    assert add_to_cart.status_code == 200
    list_in_cart = requests.post(f"{config['base_url']}api/cart/products",
                                 params={"api_token": api_token}, data={})
    assert list_in_cart.status_code == 200
    row = list_in_cart.json()
    cart_id = row['products'][0]['cart_id']
    remove_cart = requests.post(f"{config['base_url']}api/cart/remove",
                                params={"api_token": api_token}, data={"key": cart_id})
    assert remove_cart.status_code == 200
    list_in_cart_after_remove = requests.post(f"{config['base_url']}api/cart/products",
                                              params={"api_token": api_token}, data={})
    assert list_in_cart_after_remove.status_code == 200
    row1 = list_in_cart_after_remove.json()
    assert len(row1['products']) == 0


@pytest.mark.api
@pytest.mark.all
def test_add_to_cart_invalid_quantity(api_token, config):
    add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
                                params={"api_token": api_token}, data={"product_id": "43", "quantity": "1000"})
    assert add_to_cart.status_code == 200
    list_in_cart = requests.post(f"{config['base_url']}api/cart/products",
                                 params={"api_token": api_token}, data={})
    assert list_in_cart.status_code == 200
    row = list_in_cart.json()
    print(row)
    assert row['error'] == {
        'stock': 'Products marked with *** are not available in the desired quantity or not in stock!'}
    list_in_cart_1 = requests.post(f"{config['base_url']}api/cart/products",
                                   params={"api_token": api_token}, data={})
    assert list_in_cart_1.status_code == 200
    row1 = list_in_cart_1.json()
    cart_id = row1['products'][0]['cart_id']
    remove_cart = requests.post(f"{config['base_url']}api/cart/remove",
                                params={"api_token": api_token}, data={"key": cart_id})
    assert remove_cart.status_code == 200


# @pytest.mark.api
# def test_add_to_cart_two_products(api_token, config):
#     add_to_cart_1= requests.post(f"{config['base_url']}api/cart/add",
#         params={"api_token":api_token},data={"product_id":"48", "quantity":"1"})
#     assert add_to_cart_1.status_code == 200
#     add_to_cart_2= requests.post(f"{config['base_url']}api/cart/add",
#         params={"api_token":api_token},data={"product_id":"31", "quantity":"1"})
#     assert add_to_cart_2.status_code == 200
#     list_in_cart = requests.post(f"{config['base_url']}api/cart/products",
#         params={"api_token":api_token},data={})
#     assert list_in_cart.status_code == 200
#     row = list_in_cart.json()
#     print(row)
#     assert len(row['products']) == 2
#     # r = requests.post(f"{config['base_url']}api/cart/remove",
#     #                   params={"api_token": api_token}, data={"key": "1"})
#     # assert r.status_code == 200


@pytest.mark.api
@pytest.mark.all
def test_edit_quantity(api_token, config):
    add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
                                params={"api_token": api_token}, data={"product_id": "48", "quantity": "1000"})
    assert add_to_cart.status_code == 200
    list_in_cart = requests.post(f"{config['base_url']}api/cart/products",
                                 params={"api_token": api_token}, data={})
    assert list_in_cart.status_code == 200
    row = list_in_cart.json()
    cart_id = row['products'][0]['cart_id']
    edit_cart = requests.post(f"{config['base_url']}api/cart/edit",
                              params={"api_token": api_token}, data={"key": cart_id, "quantity": "10"})
    assert edit_cart.status_code == 200
    list_in_cart_1 = requests.post(f"{config['base_url']}api/cart/products",
                                   params={"api_token": api_token}, data={})
    assert list_in_cart_1.status_code == 200
    result = list_in_cart_1.json()
    assert result['products'][0]['product_id'] == '48'
    assert result['products'][0]['quantity'] == '10'


@pytest.mark.api
@pytest.mark.all
def test_add_shipping_address(api_token, config):
    add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
                                params={"api_token": api_token}, data={"product_id": "48", "quantity": "1"})
    assert add_to_cart.status_code == 200
    add_shipping_address = requests.post(f"{config['base_url']}api/shipping/address",
                                         params={"api_token": api_token},
                                         data={"firstname": "Ivan", "lastname": "Ivanov", "address_1": "Lenina st",
                                               "city": "Tula", "postcode": "101233", "country_id": "RUS",
                                               "zone_id": "KGD"})
    assert add_shipping_address.status_code == 200
    row = add_shipping_address.json()
    assert row == {'success': 'Success: Shipping address has been set!'}


# @pytest.mark.api
# def test_add_shipping_method(api_token, config):
#     add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
#                                 params={"api_token": api_token}, data={"product_id": "48", "quantity": "1"})
#     assert add_to_cart.status_code == 200
#     add_shipping_address = requests.post(f"{config['base_url']}api/shipping/address",
#                                          params={"api_token": api_token},
#                                          data={"firstname": "Ivan", "lastname": "Ivanov", "address_1": "Lenina st",
#                                                "city": "Tula", "postcode": "101233", "country_id": "RUS",
#                                                "zone_id": "KGD"})
#     assert add_shipping_address.status_code == 200
#     row = add_shipping_address.json()
#     assert row == {'success': 'Success: Shipping address has been set!'}
#     add_shipping_method = requests.post(f"{config['base_url']}api/shipping/method",
#                                          params={"api_token": api_token},
#                                          data={"shipping_method": "pickup.pickup"})
#     assert add_shipping_method.status_code == 200
#     row1 = add_shipping_method.json()


@pytest.mark.api
@pytest.mark.all
def test_get_shipping_methods(api_token, config):
    get_methods = requests.post(f"{config['base_url']}api/shipping/methods",
                                params={"api_token": api_token})
    assert get_methods.status_code == 200
    row = get_methods.json()
    print(row)


# @pytest.mark.api
# def test_add_new_order(api_token, config):
#     add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
#                                 params={"api_token": api_token}, data={"product_id": "48", "quantity": "1"})
#     assert add_to_cart.status_code == 200
#     add_shipping_address= requests.post(f"{config['base_url']}api/shipping/address",
#         params={"api_token":api_token},data={"firstname":"Ivan", "lastname":"Ivanov","address_1":"Lenina st", "city":"Tula","postcode":"101233","country_id":"RUS", "zone_id":"KGD"})
#     assert add_shipping_address.status_code == 200
#     row = add_shipping_address.json()
#     add_shipping_method = requests.post(f"{config['base_url']}api/shipping/method",
#                                         params={"api_token": api_token},
#                                         data={"shipping_method": "flat"})
#     assert add_shipping_method.status_code == 200
#     assert row == {'success': 'Success: Shipping address has been set!'}
#     add_new_order = requests.post(f"{config['base_url']}api/order/add",
#                                 params={"api_token": api_token})
#     assert add_new_order.status_code == 200
#     print(add_new_order.json())


# @pytest.mark.api
# def test_edit_order(api_token, config):
#     add_to_cart = requests.post(f"{config['base_url']}api/cart/add",
#                                 params={"api_token": api_token}, data={"product_id": "48", "quantity": "1000"})
#     assert add_to_cart.status_code == 200
#     add_shipping_address = requests.post(f"{config['base_url']}api/shipping/address",
#                                          params={"api_token": api_token},
#                                          data={"firstname": "Ivan", "lastname": "Ivanov", "address_1": "Lenina st",
#                                                "city": "Tula", "postcode": "101233", "country_id": "RUS",
#                                                "zone_id": "KGD"})
#     assert add_shipping_address.status_code == 200
#     row = add_shipping_address.json()
#     assert row == {'success': 'Success: Shipping address has been set!'}
#     add_new_order = requests.post(f"{config['base_url']}api/order/add",
#                                      params={"api_token": api_token})
#     assert add_new_order.status_code == 200
#     assert row == {'success': 'Success: Shipping address has been set!'}
#     edit_order = requests.post(f"{config['base_url']}api/order/edit",
#                                   params={"api_token": api_token})
#     assert edit_order.status_code == 200
#     print(edit_order.json())

@allure.title('Customer for session with {firstname}, {lastname}, {email}, {telephone}')
@pytest.mark.parametrize('firstname',['ewtwtete','12345'])
@pytest.mark.parametrize('lastname' , ['shfgrdc','12344'])
@pytest.mark.parametrize('email',['rr@ddd.com','rr12d@dd.com'])
@pytest.mark.parametrize('telephone', ['+122344','223445'])
@pytest.mark.api
@pytest.mark.all
def test_customer_for_session(api_token, config, firstname,lastname,email,telephone ):
    customer_for_session = requests.post(f"{config['base_url']}api/customer",
                                         params={"api_token": api_token},
                                         data={"firstname": firstname, "lastname": lastname, "email": email,
                                               "telephone": telephone})
    assert customer_for_session.status_code == 200
    row = customer_for_session.json()
    assert row == {'success': 'You have successfully modified customers'}
