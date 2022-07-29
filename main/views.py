import logging

from flask import Blueprint, render_template, request
from json import JSONDecodeError
from functions import get_posts_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search():
    search_key = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = get_posts_by_word(search_key)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return 'файл не найден'
    except JSONDecodeError:
        return 'Невалидный файл'
    return render_template('post_list.html', query=search_key, posts=posts)