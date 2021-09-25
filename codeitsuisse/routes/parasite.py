import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def solve(inputValue):
    output = [{} for _ in range(len(inputValue))]
    for room in inputValue:
        l = room["grid"]

        target = room["interestedIndividuals"]
        p1 = {}

        infected = None
        for i in range(len(l)):
            if 3 in l[i]:
                infected = i, l[i].index(3)

        maxRow = len(l)
        maxCol = len(l[0])

        for indiv in target:
            row, col = indiv.split(',')
            row, col = int(row), int(col)

            if l[row][col] != 1:
                p1[indiv] = -1
                continue

            q = [(row, col)]
            t = 0
            visited = [[False for col in range(maxCol)] for row in range(maxRow)]
            reach = False

            while len(q) > 0:
                row, col = q.pop(0)
                visited[row][col] = True

                # append to q for horizontal and vertical spread
                if row - 1 in range(0, maxRow):
                    if (l[row - 1][col] == 1 or l[row - 1][col] == 3) and visited[row - 1][col] == False:
                        q.append((row - 1, col))
                if col - 1 in range(0, maxCol):
                    if (l[row][col - 1] == 1 or l[row][col - 1] == 3) and visited[row][col - 1] == False:
                        q.append((row, col - 1))
                if col + 1 in range(0, maxCol):
                    if (l[row][col + 1] == 1 or l[row][col + 1] == 3) and visited[row][col + 1] == False:
                        q.append((row, col + 1))
                if row + 1 in range(0, maxRow):
                    if (l[row + 1][col] == 1 or l[row + 1][col] == 3) and visited[row + 1][col] == False:
                        q.append((row + 1, col))
                t += 1

                if infected in q:
                    reach = True
                    break
            if reach:
                p1[indiv] = t
            else:
                p1[indiv] = -1
        output[room["room"] - 1]["p1"] = p1
    return output


@app.route('/square', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")

    result = solve(inputValue)

    logging.info("My result :{}".format(result))
    return json.dumps(result)
