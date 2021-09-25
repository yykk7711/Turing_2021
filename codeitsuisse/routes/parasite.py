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
            visited = [[False for col in range(maxCol)] for row in range(maxRow)]
            visited[row][col] = True

            prev = [[None for col in range(maxCol)] for row in range(maxRow)]
            reach = False

            while len(q) > 0:
                row, col = q.pop(0)

                # append to q for horizontal and vertical spread
                if row - 1 in range(0, maxRow):
                    if (l[row - 1][col] == 1 or l[row - 1][col] == 3) and visited[row - 1][col] == False:
                        q.append((row - 1, col))
                        visited[row - 1][col] = True
                        prev[row - 1][col] = (row, col)
                if col - 1 in range(0, maxCol):
                    if (l[row][col - 1] == 1 or l[row][col - 1] == 3) and visited[row][col - 1] == False:
                        q.append((row, col - 1))
                        visited[row][col - 1] = True
                        prev[row][col - 1] = (row, col)
                if col + 1 in range(0, maxCol):
                    if (l[row][col + 1] == 1 or l[row][col + 1] == 3) and visited[row][col + 1] == False:
                        q.append((row, col + 1))
                        visited[row][col + 1] = True
                        prev[row][col + 1] = (row, col)
                if row + 1 in range(0, maxRow):
                    if (l[row + 1][col] == 1 or l[row + 1][col] == 3) and visited[row + 1][col] == False:
                        q.append((row + 1, col))
                        visited[row + 1][col] = True
                        prev[row + 1][col] = (row, col)

                if infected in q:
                    reach = True
                    break
            temp = infected
            row, col = indiv.split(',')
            row, col = int(row), int(col)

            if prev[temp[0]][temp[1]] == None:
                p1[indiv] = -1
                continue
            counter = 0
            while temp != (row, col):
                temp = prev[temp[0]][temp[1]]
                counter += 1
            p1[indiv] = counter
        output[room["room"] - 1]["p1"] = p1

        # p2
        healthy = []
        for row in range(len(l)):
            for col in range(len(l[0])):
                if l[row][col] == 1:
                    healthy.append((row, col))
        p2 = -1
        for indiv in healthy:
            row, col = indiv

            q = [(row, col)]
            visited = [[False for col in range(maxCol)] for row in range(maxRow)]
            visited[row][col] = True

            prev = [[None for col in range(maxCol)] for row in range(maxRow)]
            reach = False

            while len(q) > 0:
                row, col = q.pop(0)

                # append to q for horizontal and vertical spread
                if row - 1 in range(0, maxRow):
                    if (l[row - 1][col] == 1 or l[row - 1][col] == 3) and visited[row - 1][col] == False:
                        q.append((row - 1, col))
                        visited[row - 1][col] = True
                        prev[row - 1][col] = (row, col)
                if col - 1 in range(0, maxCol):
                    if (l[row][col - 1] == 1 or l[row][col - 1] == 3) and visited[row][col - 1] == False:
                        q.append((row, col - 1))
                        visited[row][col - 1] = True
                        prev[row][col - 1] = (row, col)
                if col + 1 in range(0, maxCol):
                    if (l[row][col + 1] == 1 or l[row][col + 1] == 3) and visited[row][col + 1] == False:
                        q.append((row, col + 1))
                        visited[row][col + 1] = True
                        prev[row][col + 1] = (row, col)
                if row + 1 in range(0, maxRow):
                    if (l[row + 1][col] == 1 or l[row + 1][col] == 3) and visited[row + 1][col] == False:
                        q.append((row + 1, col))
                        visited[row + 1][col] = True
                        prev[row + 1][col] = (row, col)

                if infected in q:
                    reach = True
                    break
            temp = infected
            row, col = indiv

            if prev[temp[0]][temp[1]] == None:
                p2 = -1
                break

            counter = 0
            while temp != (row, col):
                temp = prev[temp[0]][temp[1]]
                counter += 1
            if counter > p2:
                p2 = counter
        output[room["room"] - 1]["p2"] = p2

        # p3
        p3 = -1
        for indiv in healthy:
            row, col = indiv

            q = [(row, col)]
            visited = [[False for col in range(maxCol)] for row in range(maxRow)]
            visited[row][col] = True

            prev = [[None for col in range(maxCol)] for row in range(maxRow)]
            reach = False

            while len(q) > 0:
                row, col = q.pop(0)

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i != j and row + i in range(0, maxRow) and col + j in range(0, maxCol):
                            if (l[row + i][col + j] == 1 or l[row + i][col + j] == 3) and visited[row + i][col + j] == False:
                                q.append(row + i, col + j)
                                visited[row + i][col + j] = True
                                prev[row + i][col + j] = (row, col)

                if infected in q:
                    reach = True
                    break
            temp = infected
            row, col = indiv

            if prev[temp[0]][temp[1]] == None:
                p3 = -1
                break

            counter = 0
            while temp != (row, col):
                temp = prev[temp[0]][temp[1]]
                counter += 1
            if counter > p3:
                p3 = counter
        output[room["room"] - 1]["p3"] = p3



    return output


@app.route('/parasite', methods=['POST'])
def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")

    result = solve(inputValue)

    logging.info("My result :{}".format(result))
    return json.dumps(result)
