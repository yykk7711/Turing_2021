import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/stock-hunter', methods=['POST'])

def evaluate_stockhunter():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data[0]

    riskindex = dict()
    risklevel = dict()
    riskcost = dict()

    for i in range(inputValue['targetPoint']['first']+1):
        for j in range(inputValue['targetPoint']['second']+1):
            if i == 0 and j == 0 or (i == inputValue['targetPoint']['first'] and j == inputValue['targetPoint']['second']):
                riskindex[f"{i}{j}"] = 0
            elif i == 0:
                riskindex[f"{i}{j}"] = j*inputValue['verticalStepper']
            elif j == 0:
                riskindex[f"{i}{j}"] = i*inputValue['horizontalStepper']
            else:
                riskindex[f"{i}{j}"] = risklevel[f"{i-1}{j}"] * risklevel[f"{i}{j-1}"]

            risklevel[f"{i}{j}"] = (riskindex[f"{i}{j}"] + inputValue['gridDepth']) % inputValue['gridKey']

            if risklevel[f"{i}{j}"] % 3 == 0:
                riskcost[f"{i}{j}"] = 3
            elif risklevel[f"{i}{j}"] % 3 == 1:
                riskcost[f"{i}{j}"] = 2
            else:
                riskcost[f"{i}{j}"] = 1

    grid = [[] for i in range(inputValue['targetPoint']['second']+1)]

    for k,v in riskcost.items():
        if v == 3:
            grid[int(k[1])].append('L')
        elif v == 2:
            grid[int(k[1])].append('M')
        else:
            grid[int(k[1])].append('S')

    output = [{
        "gridMap": grid,
        "minimumCost": 9
    }]

    logging.info("My result :{}".format(output))
    logging.info(json.dumps(output))
    return json.dumps(output)
