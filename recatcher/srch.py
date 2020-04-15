from flask import (
    Blueprint, request
)
from recatcher.db import get_db

# Blueprints in flask are ways to interact with requests.

bp = Blueprint('srch', __name__)

@bp.route('/', methods = ['GET', 'POST'])
def mainScreen():
    return "Hello there! Here we'll have a search engine."