from ssqaapitest.src.helpers.orders_helper import OrdersHelper
from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.helpers.products_helper import ProductsHelper
from ssqaapitest.src.helpers.coupon_helper import CouponHelper
from ssqaapitest.src.utilities.genericUtilities import random_code_coupon
import pytest
import pdb


@pytest.fixture(scope='module')
def my_setup_teardown():
    # hard code create 50% coupon
    data = {
        "code": f"{random_code_coupon()}50off",
        "discount_type": "percent",
        "amount": "50",
        "individual_use": True,
        "exclude_sale_items": True,
    }
    create_coupon = CouponHelper().call_create_coupon(data)
    coupon_code = data['code']
    discount_pct = data['amount']

    # get a random product for order from db
    db_product = ProductsDAO().get_random_product_from_db(1)
    product_id = db_product[0]["ID"]
    # get product by id from API
    rand_product = ProductsHelper().get_product_by_id(product_id)

    info = dict()
    info['order_helper'] = OrdersHelper()
    info['coupon_code'] = coupon_code
    info['discount_pct'] = discount_pct
    info['product_id'] = rand_product['id']
    info['product_price'] = rand_product['price']

    return info


@pytest.mark.tcid60
def test_apply_valid_coupon_to_order(my_setup_teardown):
    # create payload and make call to create order
    order_helper = OrdersHelper()

    order_payload_addition = {
        "line_items": [{"product_id": my_setup_teardown['product_id'], "quantity": 1}],
        "coupon_lines": [{"code": my_setup_teardown['coupon_code']}],
        "shipping_lines": [{"method_id": "flat_rate", "method_title": "Flat Rate", "total": "0.00"}]
    }

    rs_order = order_helper.create_order(additional_args=order_payload_addition)

    # calculate expected total price based on coupon and product price
    expected_total = float(my_setup_teardown['product_price']) * (float(my_setup_teardown['discount_pct'])/100)

    # get total from order response and verify
    total = round(float(rs_order['total']), 1)
    expected_total = round(expected_total, 1)

    assert total == expected_total, f"Order total is not reduced after applying 50% coupon. Expected cost: {expected_total}, Actual: {total}"