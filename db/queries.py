create_products_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT NOT NULL,
        price INTEGER,
        description TEXT
    )
"""

insert_product = "INSERT INTO products (name_product, price, description) VALUES (?, ?, ?)"

select_product = 'SELECT name_product, price, description FROM products'

create_films_table = """
    CREATE TABLE IF NOT EXISTS films (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_film TEXT NOT NULL,
        genre TEXT NOT NULL,
        review INTEGER NOT NULL
    )
"""

insert_film = "INSERT INTO films (name_film, genre, review) VALUES (?, ?, ?)"

select_film = 'SELECT name_film, genre, review FROM films'