from ssqaapitest.src.utilities.dbUtility import DBUtility
import random


class CouponsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_coupon_by_id(self, coupon_id):

        sql = f"SELECT * FROM coolsite2.wp_posts WHERE ID = '{coupon_id}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_coupon(self, qty=1):

        sql = f"SELECT * FROM coolsite2.wp_posts where post_type = 'shop_coupon';"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))