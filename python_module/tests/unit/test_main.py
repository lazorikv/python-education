import pytest

from unittesting.main import even_odd, sum_all, time_of_day, Product

import datetime
import unittest
from mock import patch, Mock


# Test even_odd
@pytest.mark.parametrize('test_arg, expected', [
    (1, 'odd'),
    (10, 'even'),
    (-4, 'even'),
    (1.0, 'odd')])
def test_even_odd(test_arg, expected):

    assert even_odd(test_arg) == expected


# Test even_odd with input argument None
def test_even_odd_none_arg():
    test_arg = None

    with pytest.raises(TypeError):
        even_odd(test_arg)


# Test sum_all_type
@pytest.mark.parametrize('test_args, expected', [([1, 2], 3),
                                                 ([-3, 5, 2], 4),
                                                 ([3], 3)])
def test_sum_all(test_args, expected):
    assert sum_all(*test_args) == expected


# Test sum_all_type with Exception
def test_sum_all_type():
    numbers = ('er', 3)
    with pytest.raises(TypeError):
        sum_all(*numbers)


# Test initialisation object
@pytest.mark.parametrize('test_args, expected',
                         [(('name_1', 34.5, 5), ('name_1', 34.5, 5)),
                          pytest.param(('name_1', 34.5, 5), ('name_1', 34.5, 5),
                                       marks=pytest.mark.xfail),
                          pytest.param(('name_1', 34.5, 5), ('name_1', 34.5, 5),
                                       marks=pytest.mark.xfail)
                          ])
def test_product_init(test_args, expected):
    product = Product(*test_args)
    assert isinstance(product.title, str) and product.title == expected[0]
    assert isinstance(product.price, float) and product.price == expected[1]
    assert isinstance(product.quantity, int) and product.quantity == expected[2]


# Test substract_products from class Product
@pytest.mark.parametrize('to_subtract, expected',
                         [(3, 2),
                          (2, 3)])
def test_subtract_products(init_prod, to_subtract, expected):
    product = init_prod
    product.subtract_quantity(to_subtract)
    assert product.quantity == expected


# Test add_product from class Product
@pytest.mark.parametrize('add, expected',
                         [(4, 9),
                          (3, 8)])
def test_add_products(init_prod, add, expected):
    product = init_prod
    product.add_quantity(add)
    assert product.quantity == expected


# Test change_price from class Product
@pytest.mark.parametrize('new_price',
                         [15, 12, 2, 5])
def test_change_price(init_prod, new_price):
    prod = init_prod
    prod.change_price(new_price)
    assert prod.price == new_price


# Test add_product from class Shop
@pytest.mark.parametrize('new_prod', [
                          ('name', 35.5, 5),
                          ('name', 75.5, 5)])
def test_add_product(init_empty_shop, new_prod):
    shop = init_empty_shop
    prod = Product(*new_prod)
    shop.add_product(prod)
    assert prod in shop.products


# Test get index from class Shop
@pytest.mark.parametrize('test_arg, expected',
                         [('name3', 2),
                          ('name5', 4)])
def test_get_index(init_shop, test_arg, expected):
    shop = init_shop
    assert shop._get_product_index(test_arg) == expected


# Test get index from class Shop for index is none
def test_get_index_none(init_shop):
    shop = init_shop
    none_name = 'None'
    assert shop._get_product_index(none_name) is None


# Test sell product from class Shop
@pytest.mark.parametrize('name, quantity, expected',
                         [('name5', 2, 87),
                          ('name3', 3, 130.5),
                          ('name4', 5, 217.5)
                          ])
def test_sell_product(init_shop, name, quantity, expected):
    shop = init_shop
    assert shop.sell_product(name, quantity) == expected
    if quantity == 5:
        with pytest.raises(TypeError):
            assert shop.products[shop._get_product_index(name)]
    else:
        with pytest.raises(ValueError):
            shop.sell_product(name, quantity + 5)


# Test sell product from class Shop
def test_sell_prod_none(init_shop):
    shop = init_shop
    none_name = 'None'
    assert shop.sell_product(none_name, 4) is None
