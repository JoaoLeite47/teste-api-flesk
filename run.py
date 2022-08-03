from flask import Flask, jsonify, request
import json
app = Flask(__name__)  # create a new instance of the Flask class


@app.route('/')  # route decorator
def hello():  # function decorator
    return "Hello World!"


@app.route('/<int:id>')  # route decorator
def hello_id(id):  # function decorator
    # jsonify converts a Python object into a JSON string
    return jsonify({'O id é': id})


@app.route('/<string:name>')  # route decorator
def hello_name(name):  # function decorator
    # jsonify converts a Python object into a JSON string
    return jsonify({'O nome é': name})


# route decorator with  post method
@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 1
        return jsonify({'Soma': total})


if __name__ == '__main__':  # if this file is run directly
    app.run()  # run the app
