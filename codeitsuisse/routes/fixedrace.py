import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])

def evaluateFixedrace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")

    l = inputValue.split(',')
    l = random.shuffle(l)

    s = l[0]
    for i in range(1, 10):
        s += ','
        s += l[i]
    result = s

    logging.info("My result :{}".format(result))
    logging.info(json.dumps(result))
    return json.dumps(result)
