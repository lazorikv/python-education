import pytest
from unittesting.main import Product, Shop


@pytest.fixture
def init_prod():
    return Product('name1', 34.5, 5)


@pytest.fixture(name='init_empty_shop')
def init_shop_wout_products():
    return Shop(products=None)


@pytest.fixture(name='init_shop')
def init_shop_with_product():
    return Shop(products=[Product('name1', 43.5, 5), Product('name2', 43.5, 5),
                          Product('name3', 43.5, 5), Product('name4', 43.5, 5),
                          Product('name5', 43.5, 5), Product('name6', 43.5, 5)])

