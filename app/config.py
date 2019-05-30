import os
from app import app
# from dotenv import load_dotenv


class Config(object):
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')

    # dotenv_path = os.path.join(APP_DIR, '.env')
    # load_dotenv(dotenv_path)
    # load_dotenv()

    FLASK_ENV = os.getenv('FLASK_ENV')
    FLASK_ADMIN_SWATCH = os.getenv('FLASK_ADMIN_SWATCH')
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')

    if not os.path.exists(DIST_DIR):
        raise Exception(
            f'DIST_DIR not found: {DIST_DIR}')


app.config.from_object('app.config.Config')
