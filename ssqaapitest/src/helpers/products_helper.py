from ssqaapitest.src.utilities.requestsUtility import RequestsUtility
from ssqaapitest.src.utilities.wooAPIUtility import WooAPIUtility
import logging as logger


class ProductsHelper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.woo_helper = WooAPIUtility()

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"/wp-json/wc/v3/products/{product_id}")

    def call_create_product(self, payload):
        return self.requests_utility.post('/wp-json/wc/v3/products', payload=payload, expected_status_code=201)

    def call_list_products(self, payload=None):

        max_pages = 1000
        all_products = []
        for i in range(1, max_pages + 1):
            logger.debug(f"List products page number: {i}")

            if not 'per_page' in payload.keys():
                payload['per_page'] = 100

            # add tge current page number to the call
            payload['page'] = i
            rs_api = self.requests_utility.get('/wp-json/wc/v3/products', payload=payload)

            # if there is not response then stop the loop b/c there are no more products
            if not rs_api:
                break
            else:
                all_products.extend(rs_api)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages. ")

        return all_products

    def call_update_the_product(self, product_id, payload):
        return self.woo_helper.put(f"products/{product_id}", params=payload)

    def call_retrieve_the_product(self, product_id):
        return self.woo_helper.get(f"products/{product_id}")
