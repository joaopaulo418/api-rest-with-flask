from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

#200: Requisição bem-sucedida, tudo funcionou como esperado.
#400: Erro nos dados enviados pelo cliente (ex: campos inválidos ou ausentes).
#500: Falha interna no servidor durante o processamento da requisição.

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user and save their data to a JSON file."""
    try:
        # Get request data
        data = request.get_json()
        # Verify CNPJ length
        if len(data['cnpj']) != 14:
            return jsonify({'message': 'CNPJ deve ter 14 caracteres'}), 400
        # Acessando diretório de dados
        data_dir = os.path.join(os.getcwd(), 'data')
        #Verifica se o diretório existe, caso não exista, cria o diretório com o primeiro id = 1
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            next_id = 1
        else:
            # Check if CNPJ already exists
            for filename in os.listdir(data_dir):
                if filename.endswith('.json'):
                    file_path = os.path.join(data_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        existing_data = json.load(f)
                        if existing_data.get('cnpj') == data['cnpj']:
                            return jsonify({'message': 'CNPJ já cadastrado'}), 400

            # Lista contendo todos os ids existentes
            existing_ids = []
            # Percorre todos os arquivos do diretório com seus respectivos nomes ['1.json', '2.json', etc...]
            for filename in os.listdir(data_dir):
                # Verifica se o arquivo termina com .json
                if filename.endswith('.json'):
                    # Converte o nome do arquivo para um número inteiro
                    file_id = int(filename.replace('.json', ''))
                    # Adiciona o id encontrado na lista de ids existentes
                    existing_ids.append(file_id)
            # Se a lista de ids existentes não estiver vazia, encontra o maior id e incrementa em 1
            if existing_ids:
                next_id = max(existing_ids) + 1
            # Caso a lista de ids existentes esteja vazia, o primeiro id será 1
            else:
                next_id = 1
        # Add the generated ID to the request data
        data['id_user'] = next_id
        # Salva os dados do usuário em um arquivo JSON
        filename = os.path.join(os.getcwd(), 'data', f'{next_id}.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': 'Usuário criado com sucesso!'}), 200
    except Exception:
        return jsonify({'message': 'Erro interno do servidor.'}), 500


@app.route('/users', methods=['GET'])
def get_users():
    """Return a list of all users from the data directory."""
    try:
        users = []
        data_dir = os.path.join(os.getcwd(), 'data')
        # Read all JSON files in the data directory
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(data_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    user_data = json.load(f)
                    users.append(user_data)
        return jsonify(users), 200
    except Exception:
        return jsonify({'message': 'Erro interno do servidor.'}), 500


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Return the user data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data')
        filename = os.path.join(data_dir, f'{user_id}.json')
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                user_data = json.load(f)
            return jsonify(user_data), 200
        else:
            return jsonify({'message': f'Usuário com ID {user_id} não encontrado'}), 400
    except Exception:
        return jsonify({'message': 'Erro interno do servidor.'}), 500


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
