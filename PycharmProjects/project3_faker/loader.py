import psycopg

from config import DB_URL
from create_table import CREATE_TABLE_QUERIES

INSERTS = {
    "brand": "INSERT INTO brand (brand_name, country, created_at, created_by) VALUES (%s, %s, %s, %s)",
    "category": "INSERT INTO category (category_name, parent_category_id, level, created_at, created_by) VALUES (%s, %s, %s, %s, %s)",
    "seller": "INSERT INTO seller (seller_name, join_date, seller_type, rating, country, created_at, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    "customer": "INSERT INTO customer (customer_name, email, phone, gender, address, city, created_at, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    "product": "INSERT INTO product (product_name, category_id, brand_id, seller_id, price, stock_qty, rating, created_at, is_active, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "promotion": "INSERT INTO promotion (promotion_name, promotion_type, discount_type, discount_value, start_date, end_date, created_at, created_by) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
    "promotion_product": "INSERT INTO promotion_product (promotion_id, product_id, created_at, created_by) VALUES (%s, %s, %s, %s)",
}


def load_all(data: dict):
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            for query in CREATE_TABLE_QUERIES:
                cur.execute(query)

        for table, sql in INSERTS.items():
            with conn.cursor() as cur:
                cur.executemany(sql, data[table])
            print(f"Đã nạp {table}: {len(data[table]):,} dòng")