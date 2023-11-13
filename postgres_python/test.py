import psycopg2
import requests


base_url = "https://pokeapi.co/api/v2/"
conn = psycopg2.connect(host='pg.pg4e.com',
        port='5432',
        database='pg4e_1b6b16427b',
        user='pg4e_1b6b16427b',
        password='pg4e_p_10d58a712e20a03',
        connect_timeout=3)

cur = conn.cursor()
sql = 'drop table if exists pokeapi;'
print(sql)
cur.execute(sql)
sql = 'create table if not exists pokeapi (id integer, body jsonb);'
print(sql)
cur.execute(sql)
print('connection commited')
conn.commit()
for i in range(1, 101):
    url = f"{base_url}pokemon/{i}/"
    res = requests.get(url)
    if res.status_code != 200:
        print("Something go wrong, exit")
        exit(1)
    text = res.text
    sql = 'insert into pokeapi(id, body) values(%s, %s);'
    cur.execute(sql, (i, text))
    
conn.commit()
cur.close()
