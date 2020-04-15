# This piece of (probably shitty) code catches the request.
# CanaryTokens alerts should lead to this particular place.

from flask import (
    request, Blueprint
)
from recatcher.db import get_db

# Blueprints in flask are ways to interact with requests.

bp = Blueprint('trap', __name__)

@bp.route('/trap', methods=["POST"])
def postJsonHanlder():

    # Gets the JSON.
    content = request.get_json()
    print(content)

    # Extracts the keys. Additional keys might be added below.
    memo = request.json['memo']
    manage_url = request.json['manage_url']
    channel = request.json['channel']
    time = request.json['time']
    additional_data = request.json['additional_data']
    src_ip = additional_data['src_ip']

    # Opens, reads and saves into the database.
    db = get_db()
    db.execute(
        'INSERT INTO alert (memo, time, manage_url, channel, src_ip)'
        'VALUES (?, ?, ?, ?, ?)',
        ([memo, time, manage_url, channel, src_ip])
    )
    db.commit()

    # Prints server log info and returns answer to the client.
    print("\nValues saved in the database:\n" + memo, manage_url, channel, time, src_ip)
    return 'Alert succesfully parsed into the databse.'