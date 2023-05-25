from flask import Flask
import requests
import json

app = Flask(__name__)


@app.route('/teste1', methods=["GET"])
def home():
    api_url = "http://localhost:5000/tipo"
    response = requests.get(api_url)
    return response.json()


@app.route('/tipo1/post', methods=["POST"])
def cadastrar():
    api_url = "http://localhost:5000/tipo/v1"
    enviar = {"userId": 1, "title": "Buy milk", "completed": True}
    response = requests.post(api_url, json=enviar)
    return response.json()


@app.route('/teste1/delete', methods=["DELETE"])
def apagar():
    api_url = "http://127.0.0.1:5000/tipo/v1"
    response = requests.delete(api_url)
    return response.json()

# pip install requests - comando no terminal
# https://www.treinaweb.com.br/blog/consumindo-apis-com-python-parte-1


if __name__ == '__main__':
    app.run(debug=True, port=5001)
