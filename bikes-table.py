import sqlite3

connect = sqlite3.connect('products.db')

cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS bikes (
               id INT PRIMARY KEY, 
               brand VARCHAR, 
               model VARCHAR, 
               cost DECIMAL, 
               count INT) ''')

cursor.execute('''INSERT INTO bikes (
               id,
               brand,
               model,
               cost)
               VALUES (
               1,
               "Genesis",
               "Fugio 10"
               1499.99)''')

cursor.execute('''INSERT INTO bikes (
               id,
               brand,
               model,
               cost)
               VALUES (
               2,
               "Genesis",
               "Croix de Fer 20"
               1799.99)''')

cursor.execute('''INSERT INTO bikes (
               id,
               brand,
               model,
               cost)
               VALUES (
               3,
               "Genesis",
               "Croix de Fer 10"
               1299.99)''')