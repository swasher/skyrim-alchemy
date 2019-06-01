from myapp import app

# admin -----------------------
from .models import Effect, Ingredient
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
admin = Admin(app, name='Skyrim Alchemy', template_mode='bootstrap3')
admin.add_view(ModelView(Effect))
admin.add_view(ModelView(Ingredient))


# admin -----------------------
