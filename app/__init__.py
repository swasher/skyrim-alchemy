import os
from flask import Flask
from flask import jsonify
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from .models import Effect, Ingredient

app = Flask(__name__)

# admin ------------------------
app.config['FLASK_ADMIN_SWATCH'] = os.getenv("FLASK_ADMIN_SWATCH")
admin = Admin(app, name='Skyrim Alchemy', template_mode='bootstrap3')
admin.add_view(ModelView(Effect))
admin.add_view(ModelView(Ingredient))
# admin -----------------------


@app.route('/ingredients', methods=['GET'])
def main():
    query = Ingredient.select().dicts()
    name = "Swasher"
    # return render_template('index.html', d=d)
    return jsonify({'ingredients': list(query)})


@app.route('/')
def index():
    s = os.getenv("SECRET_KEY")
    return f'Hello! flask_env={s}'
