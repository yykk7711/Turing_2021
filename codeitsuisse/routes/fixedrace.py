import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])

def evaluateFixedrace():
    inputValue = request.get_data()
    print(inputValue)
    logging.info("data sent for evaluation {}".format(inputValue))
    l = inputValue.split(",")
    l = random.shuffle(l)

    s = l[0]
    for i in range(1, 10):
        s += ','
        s += l[i]
    result = s

    logging.info("My result :{}".format(result))
    logging.info(json.dumps(result))
    return None
