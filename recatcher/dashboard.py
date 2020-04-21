from flask import (
    Blueprint, request, render_template,
)
from recatcher.db import get_db

# Blueprints in flask are ways to interact with requests.

bp = Blueprint('dashboard', __name__)


@bp.route('/', methods = ['GET'])
def mainScreen():
    db = get_db()
    alerts = db.execute(
        'SELECT id, manage_url, memo, src_ip, channel, time'
        ' FROM alert WHERE id'
        ' ORDER BY id DESC'
        ' LIMIT 10'
    ).fetchall()
    return render_template('dashboard/dashboard.html', alerts = alerts)