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
    # 19:18
    # 's', 'k', 'f', 'e', 'l', 't', 'a'
    ans = {"answer" : ["a", "s", "k", "f", "e"]}

    return json.dumps(ans)
