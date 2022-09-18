from ssqaapitest.src.dao.products_dao import ProductsDAO
from ssqaapitest.src.dao.coupons import CouponsDAO
from ssqaapitest.src.helpers.orders_helper import OrdersHelper
from ssqaapitest.src.helpers.customers_helper import CustomerHelper
from ssqaapitest.src.helpers.coupon_helper import CouponHelper

import pytest
import pdb


@pytest.fixture(scope='module')
def my_orders_smoke_setup():
    # get a product from db
    product_dao = ProductsDAO()
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    order_helper = OrdersHelper()
    info = {'product_id': product_id,
            'order_helper': order_helper}

    return info


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid48
def test_create_paid_order_guest_user(my_orders_smoke_setup):
    order_helper = my_orders_smoke_setup['order_helper']

    customer_id = 0
    product_id = my_orders_smoke_setup['product_id']

    # make the call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)
    pdb.set_trace()


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(my_orders_smoke_setup):
    # create helper objects
    order_helper = my_orders_smoke_setup['order_helper']
    customer_helper = CustomerHelper()

    # make the call
    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']
    product_id = my_orders_smoke_setup['product_id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
        "customer_id": customer_id
    }
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.smoke
@pytest.mark.orders
@pytest.mark.tcid62
def test_create_order_with_50_discount_coupon(my_orders_smoke_setup):
    coupon_helper = CouponHelper()
    coupon_dao = CouponsDAO()
    order_helper = my_orders_smoke_setup['order_helper']
    product_id = my_orders_smoke_setup['product_id']

    # get random coupon id
    coupon_id = coupon_dao.get_random_coupon()

    # retrieve coupon
    coupon_api_info = coupon_helper.call_retrieve_coupon(coupon_id[0]['ID'])

    # make the call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]
    }
    order_json = order_helper.create_order(additional_args=info)
    order_id = order_json['id']

    # update an order with discount
    coupon_info = [
        {
            "id": coupon_api_info['id'],
            "code": coupon_api_info['code'],
        }
    ]
    payload = {"coupon_lines": coupon_info}
    order_helper = OrdersHelper()
    rs_api = order_helper.call_update_an_order(order_id, payload)
    pdb.set_trace()
