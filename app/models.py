from app import app
from peewee import *
from playhouse.flask_utils import FlaskDB

db_wrapper = FlaskDB(app)


class Effect(db_wrapper.Model):
    name = CharField(unique=True)

    def __str__(self):
        return self.name


class Ingredient(db_wrapper.Model):
    name = CharField(unique=True)
    effect1 = ForeignKeyField(Effect, backref='effect1')
    effect2 = ForeignKeyField(Effect, backref='effect2')
    effect3 = ForeignKeyField(Effect, backref='effect3')
    effect4 = ForeignKeyField(Effect, backref='effect4')


def initialize_db():
    with db_wrapper.database as db:
        db.create_tables([Effect, Ingredient], safe=True)
initialize_db()
