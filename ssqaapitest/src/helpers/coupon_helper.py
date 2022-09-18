from ssqaapitest.src.utilities.wooAPIUtility import WooAPIUtility
import random

class CouponHelper(object):

    def __init__(self):
        self.woo_helper = WooAPIUtility()

    def call_create_coupon(self, payload):
        return self.woo_helper.post('coupons', params=payload, expected_status_code=201)

    def call_retrieve_coupon(self, coupon_id):
        return self.woo_helper.get(f'coupons/{coupon_id}')


