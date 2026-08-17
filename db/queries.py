# Если добавить запись только в первую таблицу а во вторую не добавлять 
# то запись не появится из-за того что там INNER JOIN 
# а он показывает только те строки, где совпадение есть в обеих таблицах.

create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT NOT NULL,
        price INTEGER,
        product_id INTEGER NOT NULL
    )
"""

insert_product = "INSERT INTO products (name_product, price, product_id) VALUES (?, ?, ?)"

select_product = 'SELECT name_product, price, product_id FROM products'

create_films_table = """
    CREATE TABLE IF NOT EXISTS films (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_film TEXT NOT NULL,
        genre TEXT NOT NULL,
        film_id INTEGER NOT NULL      
    )
"""

insert_film = "INSERT INTO films (name_film, genre, film_id) VALUES (?, ?, ?)"

select_film = """
    SELECT f.name_film, f.genre, f.film_id, fd.description, fd.review
    FROM films AS f
    INNER JOIN films_detail AS fd ON f.film_id = fd.film_id
"""

create_table_films_detail = """
    CREATE TABLE IF NOT EXISTS films_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        film_id INTEGER NOT NULL,
        review INTEGER NOT NULL
    )
"""
insert_film_detail = 'INSERT INTO films_detail (description, film_id, review) VALUES (?, ?, ?)'

create_table_products_detail = """
    CREATE TABLE IF NOT EXISTS products_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        product_id INTEGER NOT NULL,
        category TEXT
    )
"""
insert_product_detail = 'INSERT INTO products_detail (description, product_id, category) VALUES (?, ?, ?)'