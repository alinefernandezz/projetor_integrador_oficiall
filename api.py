#API para Longin

from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

from dash import mainPy  # Importando o CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS

# Configuração do banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'adm123',
    'database': 'bd_medidor'
}

# Rota para verificar o usuário
@app.route('/verificar_usuario', methods=['POST'])
def verificar_usuario():
    dados = request.json
    email = dados.get('email')
    senha = dados.get('senha')

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM usuario WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha))
        usuario = cursor.fetchone()

        return jsonify({
            "mensagem": "Usuário autenticado com sucesso!" if usuario else "Email ou senha incorretos.",
            "usuario": usuario
        }), 200 if usuario else 401

    except Exception as e:
        return jsonify({"mensagem": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
    mainPy()
