import mysql.connector
from flask import Flask 

app = Flask(__name__)

con = mysql.connector.connect(
    host='localhost', database='ac3', user='root', password='password') 


@app.route('/funcionarios/buscar', methods=['GET'])
def buscar():
    cursor = con.cursor()
    cursor.execute('SELECT * FROM funcionarios')
    resultado = cursor.fetchall()
    return resultado


@app.route('/funcionario/registrar', methods=['POST'])
def registrar():
    cursor = con.cursor()
    sql = "INSERT INTO funcionarios (nome, sobrenome,funcao) VALUES (%s, %s, %s)"
    valores = ("Maria", "Lima", "ADM")
    valores2 = ("Pedro", "Silva", "Estagio") # para testar com mais valores
    cursor.execute(sql, valores)
    cursor.execute(sql, valores2) 
    con.commit()
    cursor.execute('SELECT * FROM funcionarios') # para testar se o Post funcionou
    resultado = cursor.fetchall()
    return resultado


@app.route('/funcionario/deletar', methods=['DELETE'])
def deletar():
    cursor = con.cursor()
    sql = "DELETE FROM funcionarios WHERE nome = 'Pedro'"
    cursor.execute(sql)
    con.commit()
    cursor.execute('SELECT * FROM funcionarios') # para testar se o Delete funcionou
    resultado = cursor.fetchall()
    return resultado


if __name__ == '__main__':
    app.run(debug=True)
