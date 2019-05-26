from app import app
from peewee import *
from playhouse.db_url import connect

database_proxy = DatabaseProxy()

class Effect(Model):
    name = CharField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        database = database_proxy  # This model uses the "people.db" database.


class Ingredient(Model):
    name = CharField(unique=True)
    effect1 = ForeignKeyField(Effect)
    effect2 = ForeignKeyField(Effect)
    effect3 = ForeignKeyField(Effect)
    effect4 = ForeignKeyField(Effect)

    class Meta:
        database = database_proxy  # This model uses the "people.db" database.


# Based on configuration, use a different database.
FLASK_ENV = app.config['FLASK_ENV']
if FLASK_ENV == 'development':
    database = SqliteDatabase('base.db')
elif FLASK_ENV == 'production':
    # connect to heroku POSTGRES
    database = connect(app.config['DATABASE_URL'])
else:
    raise Exception('No FLASK_ENV environment during db init.')


# Configure our proxy to use the db we specified in config.
database_proxy.initialize(database)


def initialize_db():
    database_proxy.connect()
    database_proxy.create_tables([Effect], safe=True)
    database_proxy.create_tables([Ingredient], safe=True)
    database_proxy.close()
initialize_db()
