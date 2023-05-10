import sqlite3


class Database:
    def __init__(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Urls
                          (longurl TEXT, shorturl TEXT)""")
        conn.commit()


def insert(url, short_url):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO Urls (longurl,shorturl) values (?,?)", (url, short_url))
    conn.commit()
    c.close()
    conn.close()
    return ""


def get_url(short_url):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT longurl FROM Urls WHERE shorturl=?", (short_url,))
    long_url = c.fetchone()
    conn.close()
    if long_url:
        return long_url[0]
    else:
        return None
