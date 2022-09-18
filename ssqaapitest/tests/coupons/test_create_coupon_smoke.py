from ssqaapitest.src.helpers.coupon_helper import CouponHelper
from ssqaapitest.src.utilities.genericUtilities import random_code_coupon
from ssqaapitest.src.dao.coupons import CouponsDAO
from ssqaapitest.src.utilities.wooAPIUtility import WooAPIUtility
import pytest
import logging as logger
import pdb


@pytest.mark.smoke
@pytest.mark.coupon
@pytest.mark.parametrize("discount_type",
                         [pytest.param('percent', marks=pytest.mark.tcid37),
                          pytest.param('fixed_cart', marks=pytest.mark.tcid38),
                          pytest.param('fixed_product', marks=pytest.mark.tcid39)
                          ])
def test_create_coupon(discount_type):
    coupon_obj = CouponHelper()
    coupon_dao = CouponsDAO()

    logger.info("TEST: Create new coupon.")

    # prepare data for coupon
    payload = {
        "code": f"{random_code_coupon()}_50off",
        "discount_type": f"{discount_type}",
        "amount": "50",
        "individual_use": True,
        "exclude_sale_items": True,
        "minimum_amount": "10.00"
    }

    # make the call
    coupon_api_info = coupon_obj.call_create_coupon(payload)

    # verify discount type in the response
    assert payload["discount_type"] == coupon_api_info["discount_type"], f"Create coupon 'discount_type' isn`t matched." \
                                                                         f"Actual: {coupon_api_info['discount_type']}," \
                                                                         f"Expected: {payload['discount_type']}"

    id_in_api = coupon_api_info['id']

    # verify coupon is created in DB
    coupon_db = coupon_dao.get_coupon_by_id(id_in_api)

    id_in_db = coupon_db[0]['ID']
    assert id_in_api == id_in_db, f'Create coupon response "id" not same as "ID" in database.'


@pytest.mark.smoke
@pytest.mark.coupon
@pytest.mark.tcid40
def test_create_invalid_coupon():
    discount_type = 'abcdefg'

    logger.info("TEST: Create new coupon.")

    # prepare data for coupon
    payload = {
        "code": f"{random_code_coupon()}_50off",
        "discount_type": f"{discount_type}",
        "amount": "50",
        "individual_use": True,
        "exclude_sale_items": True,
        "minimum_amount": "10.00"
    }

    # make the call
    rs_api = WooAPIUtility().post('coupons', params=payload, expected_status_code=400)

    assert rs_api['message'] == 'Invalid parameter(s): discount_type', "Random discount type did not have correct message" \
                                                                       "in response. Expected: percent, fixed_cart, or fixed_product'" \
                                                                       f"Actual: {rs_api['message']}"

