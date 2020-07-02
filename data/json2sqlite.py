#!/usr/bin/env python
import os
import time
import json
import sqlite3

JSON_FILE = "nflscores.json"
DB_FILE = "nfl.db"

# read file
with open('nflscores.json', 'r') as nflscores:
    data = nflscores.read()

# parse file
request = json.loads(data)

nflscores = request["nflscores"]

for item in nflscores:
	data = (item['title'], item['scores'])

	conn = sqlite3.connect(DB_FILE)
	c = conn.cursor()
	c.execute('create table nflscores (title, scores)')
	c.execute('insert into nflscores values (?,?)', data)
	conn.commit()
	conn.close()

# conn = sqlite3.connect('./data/nfl.db')
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM nfl')
# rows = cursor.fetchall()
# data = json.dumps(rows)
# print (data)
# conn.close()