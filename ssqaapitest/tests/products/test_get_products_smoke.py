import pytest
from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.products_helper import ProductsHelper

pytestmark = [pytest.mark.products, pytest.mark.smoke]


@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestsUtility()
    rs_api = req_helper.get('products')

    assert rs_api, f"Response of list all products is empty."


@pytest.mark.tcid25
def test_get_product_by_id():
    # get existing product from db
    prod_dao = ProductsDAO()
    existing_prod = prod_dao.get_random_product_from_db()
    existing_prod_id = existing_prod[0]['ID']
    db_name = existing_prod[0]['post_title']

    # call the api
    product_helper = ProductsHelper()
    product_api_info = product_helper.get_product_by_id(existing_prod_id)

    api_name = product_api_info['name']

    # verify the response
    assert db_name == api_name, f"Get product by id returned wrong product. Id: {existing_prod_id}" \
                                f"Db name: {db_name}, Apo name: {api_name}"
