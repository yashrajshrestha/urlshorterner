import random
import string
from models import URL, db

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(original_url):
    short_code = generate_short_code()
    new_url = URL(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()
    return short_code

def get_original_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first()
    return url.original_url if url else None