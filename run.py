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


@app.route('/soma', methods=['POST'])  # route decorator with  post method
def soma():  # function decorator
    # make a request to receive data in json format
    dados = json.loads(request.data)
    total = sum(dados['valores'])  # sum the values of the array
    # jsonify converts a Python object into a JSON string
    return jsonify({'Soma': total})


if __name__ == '__main__':  # if this file is run directly
    app.run()  # run the app
