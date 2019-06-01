import os
from flask import Flask
from flask import current_app
from flask import jsonify
from flask import send_file
from flask_cors import CORS
from peewee import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__, static_folder='../dist/static')

# enable CORS
CORS(app)

from .config import Config
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from .models import Effect, Ingredient


# admin -----------------------
app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
admin = Admin(app, name='Skyrim Alchemy', template_mode='bootstrap3')
admin.add_view(ModelView(Effect))
admin.add_view(ModelView(Ingredient))
# admin -----------------------


def toJSON(obj):
    obj = [model_to_dict(t, recurse=True) for t in obj]
    return jsonify({'ingredients': list(obj)})

@app.route('/ingredients', methods=['GET'])
def main():
    query = Ingredient.select() #.dicts()

    # answer = jsonify({'ingredients': list(query)})
    answer = toJSON(query)
    return answer


@app.route('/get_by_effect/<string:effect>', methods=['GET'])
def get_by_effect(effect):
    query = Ingredient.select().where(
        (Ingredient.effect1 == effect) |
        (Ingredient.effect2 == effect) |
        (Ingredient.effect3 == effect) |
        (Ingredient.effect4 == effect)
    ).dicts()
    # answer = toJSON(query)
    answer = jsonify(query)
    return answer


@app.route('/')
def index():
    # s = os.getenv("SECRET_KEY")
    # g = current_app.config['FLASK_ADMIN_SWATCH']
    # return f'Hello! flask_env={g}'
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    # vuejs_html = '/app/dist/index.html'
    return send_file(entry)
