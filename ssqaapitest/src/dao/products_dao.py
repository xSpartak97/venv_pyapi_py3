from ssqaapitest.src.utilities.dbUtility import DBUtility
import random


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        sql = f"SELECT * FROM coolsite2.wp_posts WHERE post_type='product';"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):
        sql = f"SELECT * FROM coolsite2.wp_posts WHERE ID = {product_id};"

        return self.db_helper.execute_select(sql)

    def get_products_created_after_give_date(self, _date):
        sql = f"SELECT * FROM coolsite2.wp_posts " \
              f"WHERE post_type = 'product' AND post_date > '{_date}';"

        return self.db_helper.execute_select(sql)