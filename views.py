from flask import Blueprint, request, render_template, redirect, url_for
from controllers import shorten_url, get_original_url
from logger import Logger

app_views = Blueprint('app_views', __name__)
logger = Logger()

@app_views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = shorten_url(original_url)
        logger.notify(f'Shortened URL: {original_url} to {short_code}')
        return render_template('shortened.html', short_code=short_code)
    
    return render_template('index.html')


@app_views.route('/<short_code>')
def redirect_to_url(short_code):
    original_url = get_original_url(short_code)
    if original_url:
        logger.notify(f'Redirecting from {short_code} to {original_url}')
        return redirect(original_url)
    logger.notify(f'URL not found for short code: {short_code}')
    return render_template('not_found.html'), 404