from itertools import count
import sqlite3
conn = sqlite3.connect('data.db')

c = conn.cursor()

c.execute('''CREATE TABLE data(id INTEGER PRIMARY KEY, distance INTEGER, warning_count INTEGER, bright TEXT)''')
