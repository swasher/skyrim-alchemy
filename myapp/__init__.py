import os
from flask import Flask
from flask import current_app
from flask import jsonify
from flask import send_file
from flask_cors import CORS
from peewee import *
from playhouse.shortcuts import model_to_dict




app = Flask(__name__, static_folder='../dist/static')
CORS(app)

from .config import Config

import myapp.admin
import myapp.views

