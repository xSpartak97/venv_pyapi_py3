from woocommerce import API

wcapi = API(
    url="http://localhost:8888/coolsite2",
    consumer_key="ck_c0f44eb9487cbc8332097277f2925b76621743e1",
    consumer_secret="cs_f30496fde4076be29b4f7d11404bf06a82f1908f",
    wp_api=True,
    version="wc/v3"
)

r = wcapi.get("products")

import pprint
pprint.pprint(r.json())