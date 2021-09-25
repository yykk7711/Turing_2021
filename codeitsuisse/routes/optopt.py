import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/optopt', methods=['POST'])

def evaluate_optopt():
    data = request.get_json()
    
    options = data.get("options")
    view = data.get("view")

    logging.info(options)
    logging.info(view)

    return json.dumps("HI")
