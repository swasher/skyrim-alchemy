from app import app
from peewee import *
from playhouse.db_url import connect
from playhouse.flask_utils import FlaskDB

db_wrapper = FlaskDB(app)


class Effect(db_wrapper.Model):
    name = CharField(unique=True)

    def __str__(self):
        return self.name

    # class Meta:
    #     database = database_proxy  # This model uses the "people.db" database.


class Ingredient(db_wrapper.Model):
    name = CharField(unique=True)
    effect1 = ForeignKeyField(Effect, backref='effect1')
    effect2 = ForeignKeyField(Effect, backref='effect2')
    effect3 = ForeignKeyField(Effect, backref='effect3')
    effect4 = ForeignKeyField(Effect, backref='effect4')

    # class Meta:
    #     database = database_proxy  # This model uses the "people.db" database.



# # Based on configuration, use a different database.
# FLASK_ENV = app.config['FLASK_ENV']
# if FLASK_ENV == 'development':
#     database = SqliteDatabase('base.db')
# elif FLASK_ENV == 'production':
#     # connect to heroku POSTGRES
#     database = connect(app.config['DATABASE_URL'])
# else:
#     raise Exception('No FLASK_ENV environment during db init.')
#
#
# # Configure our proxy to use the db we specified in config.
# database_proxy.initialize(database)

# def initialize_db():
#     database_proxy.connect()
#     database_proxy.create_tables([Effect], safe=True)
#     database_proxy.create_tables([Ingredient], safe=True)
#     database_proxy.close()
# initialize_db()



# def initialize_db():
#     db_wrapper.database.connect()
#     db_wrapper.database.create_tables([Effect], safe=True)
#     db_wrapper.database.create_tables([Ingredient], safe=True)
#     db_wrapper.database.close()
# initialize_db()
#
def initialize_db():
    with db_wrapper.database as db:
        # db.connect()
        db.create_tables([Effect, Ingredient], safe=True)
        # db.close()
initialize_db()
