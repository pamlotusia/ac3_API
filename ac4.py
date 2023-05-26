from flask import Flask, jsonify
import json
import requests
import mysql.connector

app = Flask(__name__)

bancoDeDados = mysql.connector.connect(
    host="localhost", user="root", password="pamela22", database="ac3")


@app.route('/v1/funcionarios', methods=["GET"])
def listar():
    selectAllSql = f"select * from funcionarios"
    cursor = bancoDeDados.cursor()
    cursor.execute(selectAllSql)
    resultado = cursor.fetchall()
    if resultado is None:
        api_url = "http://127.0.0.1:5000/tipo"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = resultado

    return jsonify(retornaApi)


@app.route('/v1/funcionarios', methods=["POST"])
def cadastrar():
    cursor = bancoDeDados.cursor()
    sql = "INSERT INTO funcionarios (nome, sobrenome,funcao) VALUES (%s, %s, %s)"
    valores = ("Maria", "Lima", "ADM"), ("Marcelo", "Junior", "BD")
    cursor.execute(sql, valores)
    bancoDeDados.commit()
    resultado = cursor.fetchall()
    cursor.close()
    if resultado is None:
        api_url = "http://127.0.0.1:5000/tipo/v1"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = resultado
    
    return retornaApi


@app.route('v1/funcionarios/deletar', methods=["DELELTE"])
def deletar():
    cursor = bancoDeDados.cursor()
    sql = "DELETE FROM funcionarios WHERE nome = 'Marcelo'"
    cursor.execute(sql)
    bancoDeDados.commit()
    resultado = cursor.fetchall()
    cursor.close()
    if resultado is None:
        api_url = "http://127.0.0.1:5000/tipo/v1"
        response = requests.get(api_url)
        retornaApi = response.json()
    else:
        retornaApi = resultado

    return retornaApi
    

    

if __name__ == '__main__':
    app.run(debug=True, port=5002)
