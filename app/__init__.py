from flask import Flask

flask_app = Flask(__name__)

from app import routes
from app import error_handlers