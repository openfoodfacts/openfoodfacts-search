"""
Script that allows manually querying ES
"""
from __future__ import annotations

import time

from app.models.product import Product
from app.utils import connection


def manual_query():
    connection.get_connection()

    while True:
        search_term = input('Please enter search term:\n')
        start_time = time.perf_counter()
        results = Product.search().query(
            'match', product_name__autocomplete=search_term,
        ).execute()
        for result in results[:10]:
            print(result.meta.score, result.product_name)
        end_time = time.perf_counter()
        print(f'Time: {end_time - start_time} seconds')


if __name__ == '__main__':
    manual_query()
