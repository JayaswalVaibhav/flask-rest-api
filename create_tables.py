"""not in use because sql alchemy is used to create tables"""
# import sqlite3
#
# connection = sqlite3.connect('data.db')
#
# cursor = connection.cursor()
#
# # int is normal integer but if we want to auto increment we use INTEGER in sqlite
# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)
#
# create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
# cursor.execute(create_table)
#
#
# connection.commit()
#
# connection.close()
