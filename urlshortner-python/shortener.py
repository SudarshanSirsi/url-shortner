from database import Database, insert, get_url
import string
import random

database = Database()


class Shortener:
    def __init__(self):
        pass

    def shorten(self, url):
        short = self.generate_short_url()
        insert(url, short)
        short_url = f"http://127.0.0.1:5000/{short}"
        return short_url

    def generate_short_url(self):
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        while True:
            rand_letters = random.choices(letters, k=7)
            rand_letters = "".join(rand_letters)
            check_duplicate = get_url(rand_letters)
            if not check_duplicate:
                return rand_letters

    def get_url(self, short_url):
        longurl = get_url(short_url)
        return longurl
