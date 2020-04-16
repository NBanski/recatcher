from flask import (
    Blueprint, g, render_template, request, url_for
)
from recatcher.db import get_db

bp = Blueprint('search', __name__)

@bp.route('/search', methods=("GET", "POST"))
def serachEngine():
    return "WIP."