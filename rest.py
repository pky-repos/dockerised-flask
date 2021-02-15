
from flask import Flask, request
import json
import functools

app = Flask(__name__)

"""
flask route handler function for /sum
"""
@app.route("/sum",  methods = ['POST'])
def post():
    req_body = request.get_json()
    if 'data' in req_body:
        lis = req_body['data']

        # Input Integer count check
        if len(lis) < 3 or len(lis) > 3:
            return json.dumps({'status': 400, 'error': 'Exactly 3 numbers are required'}), 400, {'ContentType':'application/json'} 

        a, b, c = lis[:]

        # Allow only integers
        for x in lis:
            if type(x) != int:
                return json.dumps({'status': 400, 'error': 'All inputs must be numeric'}), 400, {'ContentType':'application/json'} 

        # Typecast string to integer
        lis = [int(n) for n  in lis]

        # Input integers acceptable value filtering
        lis2 = [0 if 13 <= x <= 19 and x not in [15, 16] else x for x in lis]

        # Add filtered list integers
        s = functools.reduce(lambda x, y: x + y, lis2)
        return json.dumps({'status': 200, 'result': s}), 200, {'ContentType':'application/json'} 

    else:
        return json.dumps({'status': 400, 'error': 'Invalid input'}), 400, {'ContentType':'application/json'} 


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)