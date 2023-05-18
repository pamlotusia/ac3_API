from flask import Flask, request, json

app = Flask(__name__)


@app.route('/aula/', methods=["GET"])
def home():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = request.get(api_url)
    return response.json()


@app.route('/aula', methods=["POST"])
def cadastrar():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    enviar = {"userId": 1, "title": "Buy milk", "completed": False}
    response = request.post(api_url, json=enviar)
    return response.json()


# @app.route('/v1/tipo', methods=["DELETE"])
# def home():
#     api_url = "https://jsonplaceholder.typicode.com/todos/1"
#     response = request.delete(api_url)
#     return response.json()


if __name__ == '__main__':
    app.run(debug=True)
