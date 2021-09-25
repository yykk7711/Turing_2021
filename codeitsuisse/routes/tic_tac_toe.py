import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tic-tac-toe', methods=['POST'])

def evaluate_ttt():
    data = request.get_json()

    logging.info(data)

    return json.dumps("HI")
