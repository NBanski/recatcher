# This piece of (probably shitty) code catches the request.
# CanaryTokens alerts should lead to this particular place.

from flask import (
    request, Blueprint
)
from recatcher.db import get_db

bp = Blueprint('trap', __name__)

@bp.route('/trap', methods=["POST"])
def postJsonHanlder():
    content = request.get_json()
    print(content)

    memo = request.json['memo']
    manage_url = request.json['manage_url']
    channel = request.json['channel']
    time = request.json['time']
    additional_data = request.json['additional_data']
    src_ip = additional_data['src_ip']

    db = get_db()
    db.execute(
        'INSERT INTO alert (memo, time, manage_url, channel, src_ip)'
        'VALUES (?, ?, ?, ?, ?)',
        ([memo, time, manage_url, channel, src_ip])
    )
    db.commit()

    print("\nValues saved in the database:\n" + memo, manage_url, channel, time, src_ip)

    return 'Alert succesfully parsed into the databse.'