# This piece of (probably shitty) code catches the request.
# CanaryTokens alerts should lead to this particular place.

from flask import (
    Blueprint, flash, g, render_template, redirect, request, url_for
)
from flask import Request
from recatcher.db import get_db

bp = Blueprint('trap', __name__)

@bp.route('/trap', methods=["GET", "POST"])
def postJsonHanlder():
    content = request.json
    print (content)

    memo = request.json['memo']
    manage_url = request.json['manage_url']
    # src_ip = request.json['src_ip']
    # src_data = request.json['windows_desktopini_access_hostname']
    channel = request.json['channel']
    time = request.json['time']

    db = get_db()
    db.execute(
        'INSERT INTO alert (memo, time, manage_url, channel)'
        'VALUES (?, ?, ?, ?)',
        ([memo, time, manage_url, channel,])
    )
    db.commit()

    # return 'Alert succesfully parsed into the databse.'
    return content
