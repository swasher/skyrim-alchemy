import os
from flask import Flask
from flask import current_app
from flask import jsonify
from flask import send_file
from whitenoise import WhiteNoise


app = Flask(__name__, static_folder='../dist/static')
app.wsgi_app = WhiteNoise(app.wsgi_app, root='../dist/static/')



from .config import Config
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from .models import Effect, Ingredient


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
    # s = os.getenv("SECRET_KEY")
    # return f'Hello! flask_env={s}'
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    # vuejs_html = '/app/dist/index.html'
    return send_file(entry)
