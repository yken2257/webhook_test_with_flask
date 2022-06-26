from flask import Flask, request, jsonify
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
    return jsonify({'message': 'OK'}), 201

@app.route('/parse', methods=['POST'])
def parse_email():
    print('From:', request.form['from']) 
    print('To:', request.form['to']) 
    print('Subject:', request.form['subject']) 
    print('Body:', request.form['text']) 
    print('attachment-info: ', request.form["attachment-info"])
    print("attachments: ", request.form["attachments"])

    return jsonify({'message': 'OK'}), 201
 
if __name__ == '__main__':
    app.run()
