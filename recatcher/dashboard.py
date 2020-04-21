from flask import (
    Blueprint, request, render_template, make_response
)
from recatcher.db import get_db

# Blueprints in flask are ways to interact with requests.

bp = Blueprint('dashboard', __name__)


@bp.route('/', methods = ['GET'])
def mainScreen():
    if request.authorization and request.authorization.username == 'bc_operator' and request.authorization.password == 'SNTHVRS':
        db = get_db()
        alerts = db.execute(
            'SELECT id, manage_url, memo, src_ip, channel, time'
            ' FROM alert WHERE id'
            ' ORDER BY id DESC'
            ' LIMIT 10'
        ).fetchall()
        return render_template('dashboard/dashboard.html', alerts = alerts)
    return make_response("I'm sorry Dave, I'm afraid I can't do that.", 401, {'WWw-Authenticate' : 'Basic realm="Login Rquired"'})