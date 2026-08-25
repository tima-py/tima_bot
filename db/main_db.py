import aiosqlite
from db import queries

path_db = 'db/bot.db'
path_films_db = 'db/films.db'

async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_products_table)
        await conn.execute(queries.create_table_products_detail)
        await conn.commit()
    print('БД подключена!')

async def create_table():
    async with aiosqlite.connect(path_films_db) as conn:
        await conn.execute(queries.create_films_table)
        await conn.execute(queries.create_table_films_detail)
        await conn.commit()
    print('БД подключена!')

async def add_film_db(name_film, genre, film_id):
    async with aiosqlite.connect(path_films_db) as conn:
        conn.execute(queries.insert_film, (name_film, genre, film_id))
        conn.commit()

async def add_film_detail_db(description, film_id, review):
    async with aiosqlite.connect(path_films_db) as conn:
        conn.execute(queries.insert_film_detail, (description, film_id, review))
        conn.commit()

async def get_film_db():
    async with aiosqlite.connect(path_films_db) as conn:
        cursor = await conn.execute(queries.select_film)
        films = await cursor.fetchall()
    return films

async def add_product_db(name_product, price, product_id, photo_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_product, (name_product, price, product_id, photo_id))
        await conn.commit()


async def add_product_detail_db(product_id, category, description):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.insert_product_detail, (description, product_id, category))
        await conn.commit()


async def get_product_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.select_product)
        products = await cursor.fetchall()
    return products

async def update_product_db(field, value, product_id):
    if field in ('name_product', "price"):
        table = 'products'
    elif field in ('description', 'category'):
        table = 'products_detail'
    else: 
        return

    query = queries.update_product.format(table=table, field=field)

    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(query, (value, product_id))
        await conn.commit()

async def delete_product_db(product_id):
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.delete_product, (product_id, ))
        await conn.execute(queries.delete_product_detail, (product_id, ))
        await conn.commit()

async def delete_all_products_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.delete_all_products_detail)
        await conn.execute(queries.delete_all_products)
        await conn.commit()

# import sqlite3
# from db import queries

# path_db = 'db/sqlite3.db'
# path_films_db = 'db/films.db'


# async def init_db():
#     conn = sqlite3.connect(database=path_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.create_products_table)
#     cursor.execute(queries.create_table_products_detail)
#     print('DB подключена!')
#     conn.commit()
#     conn.close()

# async def create_table():
#     conn = sqlite3.connect(database=path_films_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.create_films_table)
#     cursor.execute(queries.create_table_films_detail)
#     print('DB подключена!')
#     conn.commit()
#     conn.close()

# async def add_film_db(name_film, genre, film_id):
#     conn = sqlite3.connect(path_films_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.insert_film, (name_film, genre, film_id))
#     conn.commit()
#     conn.close()

# async def add_film_detail_db(description, film_id, review):
#     conn = sqlite3.connect(path_films_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.insert_film_detail, (description, film_id, review))
#     conn.commit()
#     conn.close()

# async def get_film_db():
#     conn = sqlite3.connect(path_films_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.select_film)
#     films = cursor.fetchall()
#     conn.close()
#     return films

# async def add_product_db(name_product, price, product_id):
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.insert_product, (name_product, price, product_id))
#     conn.commit()
#     conn.close()

# async def add_product_detail_db(description, product_id, category):
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.insert_product_detail, (description, product_id, category))
#     conn.commit()
#     conn.close()

# async def get_product_db():
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     cursor.execute(queries.select_product)
#     products = cursor.fetchall()
#     conn.close()
#     return products