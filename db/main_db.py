import sqlite3
from db import queries

path_db = 'db/sqlite3.db'
path_films_db = 'db/films.db'


async def init_db():
    conn = sqlite3.connect(database=path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_products_table)
    print('DB подключена!')
    conn.commit()
    conn.close()

async def create_table():
    conn = sqlite3.connect(database=path_films_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_films_table)
    print('DB подключена!')
    conn.commit()
    conn.close()

async def add_film_db(name_film, genre, review):
    conn = sqlite3.connect(path_films_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_film, (name_film, genre, review))
    conn.commit()
    conn.close()


async def get_film_db():
    conn = sqlite3.connect(path_films_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_film)
    films = cursor.fetchall()
    conn.close()
    return films

async def add_product_db(name_product, price, description):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_product, (name_product, price, description))
    conn.commit()
    conn.close()


async def get_product_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_product)
    products = cursor.fetchall()
    conn.close()
    return products