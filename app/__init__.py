import os
from flask import Flask
from flask import current_app
from flask import jsonify
from flask import send_file
from flask import redirect
from flask_cors import CORS
from peewee import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__, static_folder='../dist/static')
CORS(app)
from .config import Config

from app.models import Effect, Ingredient
from app.models import db_wrapper

# admin -----------------------
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

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
    query = Ingredient.select().order_by('name') #.dicts()
    # answer = jsonify({'ingredients': list(query)})
    answer = toJSON(query)
    return answer


@app.route('/get_by_effect/<string:effect>', methods=['GET'])
def get_by_effect(effect):
    """
    Return all ingredients, which contain 'effect'
    :param effect:
    :return:
    """
    query = Ingredient.select().where(
        (Ingredient.effect1 == effect) |
        (Ingredient.effect2 == effect) |
        (Ingredient.effect3 == effect) |
        (Ingredient.effect4 == effect)
    ).dicts()
    # answer = toJSON(query)
    answer = jsonify(query)
    return answer


@app.route('/get_by_ingredient/<string:ingredient>', methods=['GET'])
def get_by_ingredient(ingredient):
    """
    Return all ingredients with at least one matching effect with input ingredient
    :param effect:
    :return:
    """
    answer = []
    return answer




from playhouse.dataset import DataSet
@app.route('/export')
def exporting():
    db = DataSet(app.config['DATABASE'])
    db.freeze(Effect.select(), format='csv', filename='effects.csv')
    db.freeze(Ingredient.select(), format='csv', filename='ingredients.csv')
    return redirect('/admin')



@app.route('/import')
def importing():
    db = DataSet(app.config['DATABASE'])
    table = db['effect']
    table.thaw(filename='effects.csv', format='csv')
    table = db['ingredient']
    table.thaw(filename='ingredients.csv', format='csv')
    return redirect('/admin')


@app.route('/')
def index():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)

