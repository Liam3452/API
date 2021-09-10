from flask import*
import json
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {'page':'home', 'message':'active home page','timestamp':time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))
    data_set = {'page':'request', 'message': f'got request from {user_query}','timestamp':time.time()}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(port = 7777)
