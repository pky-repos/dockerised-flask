
from flask import Flask, request
import json
import functools


app = Flask(__name__)

@app.route("/",  methods = ['POST'])
def getSum():
    req_body = request.get_json()
    if 'data' in req_body:
        lis = req_body['data']

        print("lis", lis)
        if len(lis) < 3 or len(lis) > 3:
            return json.dumps({'success':False, 'message': 'Exactly 3 numbers are required'}), 400, {'ContentType':'application/json'} 

        a, b, c = lis[:]

        for x in lis:
            if not str(x).isnumeric():
                return json.dumps({'success':False, 'message': 'All inputs must be numeric'}), 400, {'ContentType':'application/json'} 

        lis = [int(n) for n  in lis]

        lis2 = [0 if 13 <= x <= 19 and x not in [15, 16] else x for x in lis]

        s = functools.reduce(lambda x, y: x + y, lis2)
        return json.dumps({'success':True, 'result': s}), 200, {'ContentType':'application/json'} 

    else:
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'} 


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)