import sqlite3 as sq

def store(rows):
    conn = sq.connect("data/data.db")
    cur = conn.cursor()

    cur.execute("drop table if exists indicators")
    cur.execute("create table indicators (country text, indicator text, year integer, value real)")
    cur.executemany("insert into indicators values (?, ?, ?, ?)", rows)

    conn.commit()
    conn.close()

