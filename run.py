from flask import Flask, jsonify
app = Flask(__name__)  # create a new instance of the Flask class


@app.route('/')  # route decorator
def hello():  # function decorator
    return "Hello World!"


@app.route('/<int:id>') # route decorator
def hello_id(id): # function decorator
    return jsonify({'O id é': id}) # jsonify converts a Python object into a JSON string


if __name__ == '__main__':  # if this file is run directly
    app.run()  # run the app
