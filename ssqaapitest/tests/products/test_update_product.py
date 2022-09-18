from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.utilities.genericUtilities import generate_random_price, generate_random_name_product

import pytest
import pdb


@pytest.mark.tcid61
def test_update_product_regular_price():
    # generating random price of the product
    new_price = generate_random_price()
    # get random product from DB
    product_dao = ProductsDAO()
    product_db_info = product_dao.get_random_product_from_db()
    existing_prod_id = product_db_info[0]['ID']

    # call the API
    product_helper = ProductsHelper()

    # update the regular price
    payload = {"regular_price": new_price}
    product_helper.call_update_the_product(existing_prod_id, payload)

    # get product price information
    new_product_info = product_helper.call_retrieve_the_product(existing_prod_id)

    # verify the new 'regular_price' updates price of the product
    assert new_price == new_product_info['price'], f"Updated order 'regular price' did not update price of the product." \
                                                   f"Expected: {new_price}, Actual: {new_product_info}"


@pytest.mark.tcid63
def test_update_on_sale_True():
    prod_helper = ProductsHelper()

    # generate some data
    payload = dict()
    payload['name'] = generate_random_name_product()
    payload['type'] = 'simple'
    payload['regular_price'] = '16.99'

    # make the call - create product
    product_rs = prod_helper.call_create_product(payload)
    prod_id = product_rs['id']

    # update the product 'on_sale'=True
    payload = {'sale_price': '14.99'}
    prod_helper.call_update_the_product(prod_id, payload)

    # get product 'sale_price' information
    product = prod_helper.call_retrieve_the_product(prod_id)

    # verify 'sale_price' updates 'on_sale' to True
    assert product['on_sale'], f"Updated 'sale_price' doesn`t updates 'on_sale'=True. " \
                               f"Expected {product['on_sale']}, Actual {product_rs['on_sale']}"


@pytest.mark.tcid64
def test_update_on_sale_False():
    prod_helper = ProductsHelper()

    # generate some data
    payload = dict()
    payload['name'] = generate_random_name_product()
    payload['type'] = 'simple'
    payload['regular_price'] = '16.99'

    # make the call - create product
    product_rs = prod_helper.call_create_product(payload)
    prod_id = product_rs['id']

    # update the product 'on_sale'=True
    payload = {'sale_price': '14.99'}
    on_sale_true = prod_helper.call_update_the_product(prod_id, payload)

    # update the product 'on_sale'=False
    payload = {'sale_price': ''}
    prod_helper.call_update_the_product(prod_id, payload)

    # get product 'sale_price' information
    product = prod_helper.call_retrieve_the_product(prod_id)
    pdb.set_trace()
    assert product['on_sale'] != on_sale_true['on_sale'], f"Update product api call response has 'True' value." \
                                                          f"Expected result {product_rs['on_sale']}, Actual {on_sale_true['on_sale']}"