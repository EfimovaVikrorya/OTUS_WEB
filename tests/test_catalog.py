
from page_object.CatalogPage import CatalogPage


def test_catalog_brand_name(driver):
    catalog_page = CatalogPage(driver)
    CatalogPage(driver).open_page()
    el = CatalogPage(driver).brend()
    assert el.text == 'Brand Apple'


def test_catalog_brand_items(driver):
    catalog_page = CatalogPage(driver)
    CatalogPage(driver).open_page()
    # количество элементов на странице
    el = CatalogPage(driver).element_on_the_page()
    assert len(el) == 10


def test_catalog_sort(driver):
    catalog_page = CatalogPage(driver)
    CatalogPage(driver).open_page()
    # выпадающий список сортировки
    el = CatalogPage(driver).dropdown_of_sort()
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
    catalog_page = CatalogPage(driver)
    CatalogPage(driver).open_page()
    #  выпадающий список количества на странице
    el = CatalogPage(driver).dropdown_of_limit()
    assert (el.text == '                                          15\n' +
            '                                                        25\n' +
            '                                                        50\n' +
            '                                                        75\n' +
            '                                                        100\n' +
            '                                        \n' +
            '            ')


def test_catalog_compare(driver):
    catalog_page = CatalogPage(driver)
    CatalogPage(driver).open_page()
    #   клик по надписи Продкуты для сравнения
    CatalogPage(driver).product_compare()
    # надпись после перехода
    el_cont = CatalogPage(driver).product_comparison()
    assert el_cont.text == "Product Comparison\nYou have not chosen any products to compare.\nContinue"
