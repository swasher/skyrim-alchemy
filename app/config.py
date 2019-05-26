"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os
from app import app
from dotenv import load_dotenv




tw_consumer_key = os.getenv('TWITTER_CONSUMER_KEY')


class Config(object):
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')


    # APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
    # dotenv_path = os.path.join(APP_DIR, '.env')
    # load_dotenv(dotenv_path)
    load_dotenv()

    print(os.getenv('A'))

    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.getenv('FLASK_SECRET')
    DATABASE_URL = os.getenv('DATABASE_URL')

    # print(APP_ROOT)
    print(APP_DIR)
    print(ROOT_DIR)

    if not os.path.exists(DIST_DIR):
        raise Exception(
            'DIST_DIR not found: {}'.format(DIST_DIR))

app.config.from_object('app.config.Config')
