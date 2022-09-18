from ssqaapitest.src.helpers.orders_helper import OrdersHelper
from ssqaapitest.src.utilities.wooAPIUtility import WooAPIUtility
from ssqaapitest.src.utilities.genericUtilities import generate_random_name_product
import pytest
import pdb


@pytest.mark.orders
@pytest.mark.regression
@pytest.mark.parametrize("new_status",
                         [pytest.param('on-hold', marks=pytest.mark.tcid55),
                          pytest.param('failed', marks=pytest.mark.tcid56),
                          pytest.param('refunded', marks=pytest.mark.tcid57)
                          ])
def test_update_order_status(new_status):

    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    # get the current status of the order
    cur_status = order_json['status']
    assert cur_status != new_status, f"Current status of order is already {new_status}." \
                                     f"Unable to run test."

    # update the status
    order_id = order_json['id']
    payload = {"status": new_status}
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)

    # verify the new order status is what was updated
    assert new_order_info['status'] == new_status, f"Updated order status to '{new_status}'," \
                                                   f"but order is still '{new_order_info['status']}'"


@pytest.mark.orders
@pytest.mark.regression
@pytest.mark.tcid58
def test_update_order_status_to_random_string():
    new_status = 'abcdefg'

    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update the status
    payload = {"status": new_status}
    rs_api = WooAPIUtility().put(f'orders/{order_id}', params=payload, expected_status_code=400)
    assert rs_api['code'] == 'rest_invalid_param', "Update order status to random string did not have" \
                                                   "correct code in repsonse. Expected 'rest_invalid_param'" \
                                                   f"Actual: {rs_api['code']}"
    assert rs_api['message'] == 'Invalid parameter(s): status', "Update order status to random string did not have" \
                                                   "correct message in repsonse. Expected 'Invalid parameter(s)'" \
                                                   f"Actual: {rs_api['message']}"


@pytest.mark.tcid59
def test_update_order_customer_note():
    # create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    rand_string = generate_random_name_product(30)
    payload = {"customer_note": rand_string}
    order_helper.call_update_an_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_an_order(order_id)
    assert new_order_info['customer_note'] == rand_string, f"Update order`s 'customer_note' field" \
                                                           f"failed. Expected: {rand_string}, Actual: {new_order_info['customer_note']}"


