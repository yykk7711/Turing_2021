import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)


@app.route('/asteroid', methods=['POST'])

def asteroid_solve(d):

    ls = d['test_cases']
    ans = []

    for s in ls:

        board = dict()

        for i,v in enumerate(s):
            left = i-1
            right = i+1
            score = 0
            print(i, v)

            if i != 0 and i != len(s)-1:
                if s[left] == v and v == s[right]:
                    score = 1

                    while s[left] == s[right]:
                        length = 2

                        left_head = left
                        right_head = right

                        while left_head != 0 and s[left_head-1] == s[left_head]:
                            left_head -= 1
                            length += 1
                        else:
                            left = left_head-1

                        while right_head != len(s)-1 and s[right_head+1] == s[right_head]:
                            right_head += 1
                            length += 1
                        else:
                            right = right_head+1

                        print("length is", length)
                        if length >= 10:
                            score += length*2
                        elif length >= 7:
                            score += length*1.5
                        else:
                            score += length


                        if right > len(s)-1 or left < 0:
                            break

                        print(score)
                        print()

                print(i, score)
                board[i] = int(score)

        king = [pair for pair in list(board.items()) if pair[1] == max(board.values())][0]

        to_add = {"input":s,"score":king[1],"origin":king[0]}
        ans.append(to_add)

    return ans

def evaluate():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("test_cases")

    result = asteroid_solve(inputValue)

    logging.info("My result :{}".format(result))
    return json.dumps(result)
