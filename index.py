from flask import Flask, request
from json import dumps
 
app = Flask(__name__)
 
@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"
 
@app.route('/event', methods=['POST'])
def display_json():
    json_list = request.get_json()
    for data in json_list:
        dumped = dumps(data)
        print(dumped)
    return ""


 
if __name__ == '__main__':
    app.run()
