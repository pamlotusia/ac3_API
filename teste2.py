from flask import Flask, jsonify
import json
import requests
import mysql.connector

app = Flask(__name__)

bancoDeDados = mysql.connector.connect(host="localhost",user="root",password="password",database="db_Alunos")

#http://127.0.0.1:5000/v1/cliente
@app.route('/v1/cliente', methods=["GET"])
def listar():
    selectAllSql = f"select * from tb_aluno"
    cursor = bancoDeDados.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    if resultado is None:
        api_url = "http://127.0.0.1:5000/v1/api/externa"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = None

    return jsonify(retornaApi)

if __name__ == '__main__':
    app.run(port=5001)