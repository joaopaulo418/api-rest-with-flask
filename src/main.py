from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user and save their data to a JSON file."""
    try:
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['name_user', 'name_enterprise', 'cnpj', 'area_of_activity', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Dados incompletos'}), 400
        # Verify CNPJ length
        if len(data['cnpj']) != 14:
            return jsonify({'message': 'CNPJ deve ter 14 caracteres'}), 400
        # Accessing data directory
        data_dir = os.path.join(os.getcwd(), 'data')
        # Check if directory exists, if not create it with first id = 1
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

            # List containing all existing ids
            existing_ids = []
            # Loop through all files in directory with their names ['1.json', '2.json', etc...]
            for filename in os.listdir(data_dir):
                # Check if file ends with .json
                if filename.endswith('.json'):
                    # Convert filename to integer
                    file_id = int(filename.replace('.json', ''))
                    # Add found id to list of existing ids
                    existing_ids.append(file_id)
            # If list of existing ids is not empty, find highest id and increment by 1
            if existing_ids:
                next_id = max(existing_ids) + 1
            # If list of existing ids is empty, first id will be 1
            else:
                next_id = 1
        # Add the generated ID to the request data
        data['id_user'] = next_id
        # Save user data to JSON file
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


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        data_dir = os.path.join(os.getcwd(), 'data')
        filename = os.path.join(data_dir, f'{user_id}.json')
        if not os.path.exists(filename):
            return jsonify({'message': f'Usuário com ID {user_id} não encontrado'}), 400
        os.remove(filename)
        return jsonify({'message': f'Usuário com ID {user_id} deletado com sucesso'}), 200
    except Exception:
        return jsonify({'message': 'Erro interno do servidor.'}), 500


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_full_user(user_id):
    """Update all user data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data')
        filename = os.path.join(data_dir, f'{user_id}.json')
        # Check if user exists
        if not os.path.exists(filename):
            return jsonify({'message': f'Usuário com ID {user_id} não encontrado'}), 400
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['name_user', 'name_enterprise', 'cnpj', 'area_of_activity', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Dados incompletos'}), 400
        # Preserve the user_id
        data['id_user'] = user_id
        # Write updated data
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': f'Usuário com ID {user_id} atualizado com sucesso'}), 200
    except Exception:
        return jsonify({'message': 'Erro interno do servidor.'}), 500


@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_password(user_id):
    """Update any user data field for a given user ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data')
        filename = os.path.join(data_dir, f'{user_id}.json')
        # Check if user exists
        if not os.path.exists(filename):
            return jsonify({'message': f'Usuário com ID {user_id} não encontrado'}), 400
        # Get request data
        data = request.get_json()
        # Validate that at least one field is present to update
        if not data:
            return jsonify({'message': 'Nenhum dado fornecido para atualização'}), 400
        # Read current user data
        with open(filename, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
        # Update the provided fields
        for field in data:
            if field in user_data:
                user_data[field] = data[field]
        # Write updated data back
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': f'Dados do usuário com ID {user_id} atualizados com sucesso'}), 200
    except Exception:
        return jsonify({'message': 'Erro interno do servidor.'}), 500


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
