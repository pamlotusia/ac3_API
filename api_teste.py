from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/tipo', methods=["GET"])
def home():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(api_url)
    return response.json()


@app.route('/tipo/v1', methods=["POST"])
def cadastrar():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    enviar = {"userId": 1, "title": "Buy milk", "completed": False}
    response = requests.post(api_url, json=enviar)
    return response.json()


@app.route('/v1/tipo', methods=["DELETE"])
def home():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.delete(api_url)
    return response.json()

#pip install requests - comando no terminal
#https://www.treinaweb.com.br/blog/consumindo-apis-com-python-parte-1

if __name__ == '__main__':
    app.run(debug=True)
