__author__ = 'f'
#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Read Catalog

import requests
import json
import time

from datetime import datetime
from pyes import *


def update_catalog(prodUrl):
    product_url = requests.get(prodUrl)
    product_list = product_url.json()
    product_url.close()
    return product_list


def clear_ES_catalog(conn):
    try:
        conn.indices.delete_index("productindex")
    except Exception, e:
        logging.exception(e)
        pass
    time.sleep(5)
    conn.indices.create_index("productindex")
    time.sleep(5)
    mappings = {u'properties': {u'suggest': {'type': "completion",
                          'index_analyzer': 'simple',
                          'search_analyzer': 'simple'}}}
    conn.indices.put_mapping("test-type", mappings, "productindex")


def update_ES(conn, product_list):
    ts = time.time()
    for product in product_list['products']:
        product['timestamp'] = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        conn.index(product, "productindex", "test-type", int(product['productId']))


if __name__ == '__main__':
    # conn = ES('52.25.166.127:9200')
    #conn = ES('localhost:9200')
    conn=ES(server=[('http', 'localhost', 9200)])
    clear_ES_catalog(conn)
    product_list = update_catalog('http://test.decirc.com/slim-api/product/catalog')
    print product_list
    update_ES(conn, product_list)