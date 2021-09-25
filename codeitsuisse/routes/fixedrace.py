import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/square', methods=['POST'])

def evaluateFixedrace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")

    l = inputValue.split(',')
    result = random.shuffle(l)

    logging.info("My result :{}".format(result))
    logging.info(json.dumps(result))
    return json.dumps(result)
