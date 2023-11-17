from flask import Flask, jsonify

import mysql.connector

app = Flask(__name__)

db_config = {
    "host":"localhost",
    "user": "root",
    "password": "mysqladmin102030",
    "database": "login"
}

@app.route("/")
def home():
    return "Bem vindo a minha api"

@app.route("/buscar_usuarios",methods=['GET'])
def buscar_usuarios():
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    lista_usuarios = cursor.fetchall()
    conexao.close()
    return jsonify({"users": lista_usuarios})

if __name__ == "__main__":
    app.run(debug=True)