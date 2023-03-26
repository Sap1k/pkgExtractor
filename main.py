import json
import sqlite3

import requests


# Function to connect to DB and properly handle exceptions
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)
        conn = None
    finally:
        return conn


con = create_connection("entitlement.db")
c = con.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name LIKE 'entitlement_%' ORDER BY name")
tables_to_check = c.fetchall()

sql_results = []

for table in tables_to_check:
    c.execute(f'SELECT JSON FROM {table[0]} WHERE Entitlement_type = 5 AND Package_subtype IS NULL')
    sql_results = sql_results + c.fetchall()

urls_to_check = []

for result in sql_results:
    json_res = json.loads(result[0])
    try:
        urls_to_check.append(json_res['entitlement_attributes'][0]['reference_package_url'])
    except KeyError:
        pass

with open('links.txt', 'w') as f:
    for url in urls_to_check:
        url_result = requests.get(url).json()
        part = 1
        for link in url_result['pieces']:
            print(link)
            f.write(f"part{part}: {link['url']}\n")
            part += 1
        f.write("========================================\n")
