import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])

def evaluate_decoder():
    data = request.get_json()
    # logging.info("data sent for evaluation {}".format(data))
    logging.info(data.get("possible_values"))
    logging.info(data.get("num_slots"))
    logging.info(data.get("history"))


    # logging.info("My result :{}".format("HI"))
    # ["c", "v", "s", "y", "s"]
    # ["a", "b", "d", "e", "f"] 1
    # drop a,d
    # ALL : ['g', 'x', 'w', 'm', 'a', 'e', 'b']
    # no b
    ans = {"answer" : ['a', 'g', 'x', 'a', 'w']}

    return json.dumps(ans)
