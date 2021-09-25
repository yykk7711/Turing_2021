import logging
import json
import random

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/fixedrace', methods=['POST'])

def evaluateFixedrace():
    data = request.get_data(as_text = True)
    logging.info("data sent for evaluation {}".format(data))

    l = data.split(",")
    random.shuffle(l)

    result = l[0]
    for i in range(1,10):
        result += ','
        result += l[i]

    logging.info("My result :{}".format(result))
    logging.info(json.dumps(result))
    return result

