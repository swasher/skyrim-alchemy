from myapp import app
import os
from flask import current_app
from flask import jsonify
from flask import send_file
from playhouse.shortcuts import model_to_dict

from .models import Effect, Ingredient


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
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
