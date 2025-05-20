import json
import os
from flask import Flask, request, jsonify
# pylint: disable=C0301, C0114, W0718, C0114, C0116

app = Flask(__name__)

@app.route('/enterprises', methods=['POST'])
def create_enterprise():
    """Create a new enterprise and save their data to a JSON file."""
    try:
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['cnpj', 'name_enterprise', 'area_of_activity']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Dados incompletos'}), 400
        # Verify CNPJ length
        if len(data['cnpj']) != 14:
            return jsonify({'message': 'CNPJ deve ter 14 caracteres'}), 400
        # Accessing data directory
        data_dir = os.path.join(os.getcwd(), 'data', 'enterprises')
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
        data['id_enterprise'] = next_id
        # Save user data to JSON file
        filename = os.path.join(os.getcwd(), 'data', 'enterprises', f'{next_id}.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': 'Empresa criada com sucesso!',
                        'id_enterprise': next_id}), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user and save their data to a JSON file."""
    try:
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['name_user', 'id_enterprise', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Dados incompletos'}), 400
        # Accessing data directory
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        # Check if enterprise exists
        enterprise_dir = os.path.join(os.getcwd(), 'data', 'enterprises')
        enterprise_file = os.path.join(enterprise_dir, f"{data['id_enterprise']}.json")
        if not os.path.exists(enterprise_file):
            return jsonify({'message': 'Empresa não encontrada. Cadastre sua empresa primeiro.'}), 400
        # Check if directory exists, if not create it with first id = 1
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            next_id = 1
        else:
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
        filename = os.path.join(os.getcwd(), 'data', 'users', f'{next_id}.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': 'Usuário criado com sucesso!',
                        'id_user': data['id_user']}), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """Return a list of all users from the data directory."""
    try:
        users = []
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        # Read all JSON files in the data directory
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(data_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    user_data = json.load(f)
                    users.append(user_data)
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Return the user data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        filename = os.path.join(data_dir, f'{user_id}.json')
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                user_data = json.load(f)
            return jsonify(user_data), 200
        return jsonify({'message': f'Usuário com ID {user_id} não encontrado'}), 400
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/enterprises', methods=['GET'])
def get_enterprises():
    """Return a list of all enterprises from the data directory."""
    try:
        enterprises = []
        data_dir = os.path.join(os.getcwd(), 'data', 'enterprises')
        # Read all JSON files in the data directory
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(data_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    enterprise_data = json.load(f)
                    enterprises.append(enterprise_data)
        return jsonify(enterprises), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/enterprises/<int:enterprise_id>', methods=['GET'])
def get_enterprise(enterprise_id):
    """Return the enterprise data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'enterprises')
        filename = os.path.join(data_dir, f'{enterprise_id}.json')
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                enterprise_data = json.load(f)
            return jsonify(enterprise_data), 200
        return jsonify({'message': f'Empresa com ID {enterprise_id} não encontrada'}), 400
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        filename = os.path.join(data_dir, f'{user_id}.json')
        if not os.path.exists(filename):
            return jsonify({'message': f'Usuário com ID {user_id} não encontrado'}), 400
        os.remove(filename)
        return jsonify({'message': f'Usuário com ID {user_id} deletado com sucesso'}), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/enterprises/<int:enterprise_id>', methods=['DELETE'])
def delete_enterprise(enterprise_id):
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'enterprises')
        filename = os.path.join(data_dir, f'{enterprise_id}.json')
        if not os.path.exists(filename):
            return jsonify({'message': f'Empresa com ID {enterprise_id} não encontrada'}), 400
        os.remove(filename)
        # Remove all users associated with this enterprise
        users_dir = os.path.join(os.getcwd(), 'data', 'users')
        for user_file in os.listdir(users_dir):
            if user_file.endswith('.json'):
                user_path = os.path.join(users_dir, user_file)
                with open(user_path, 'r', encoding='utf-8') as f:
                    user_data = json.load(f)
                    if user_data['id_enterprise'] == enterprise_id:
                        os.remove(user_path)
        return jsonify({'message': f'Empresa e usuários associados com ID {enterprise_id} deletados com sucesso'}), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_full_user(user_id):
    """Update all user data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        filename = os.path.join(data_dir, f'{user_id}.json')
        # Check if user exists
        if not os.path.exists(filename):
            return jsonify({'message': f'Usuário com ID {user_id} não encontrado'}), 400
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['name_user', 'id_enterprise', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Dados incompletos'}), 400
        # Preserve the user_id
        data['id_user'] = user_id
        # Write updated data
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': f'Usuário com ID {user_id} atualizado com sucesso'}), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_any_field_user(user_id):
    """Update any user data field for a given user ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
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
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/enterprises/<int:enterprise_id>', methods=['PUT'])
def update_full_enterprise(enterprise_id):
    """Update all enterprise data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'enterprises')
        filename = os.path.join(data_dir, f'{enterprise_id}.json')
        # Check if enterprise exists
        if not os.path.exists(filename):
            return jsonify({'message': f'Empresa com ID {enterprise_id} não encontrada'}), 400
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['name_enterprise', 'cnpj', 'area_of_activity']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Dados incompletos'}), 400
        # Preserve the enterprise_id
        data['id_enterprise'] = enterprise_id
        # Write updated data
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': f'Empresa com ID {enterprise_id} atualizada com sucesso'}), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

@app.route('/enterprises/<int:enterprise_id>', methods=['PATCH'])
def update_any_field_enterprise(enterprise_id):
    """Update any enterprise data field for a given enterprise ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'enterprises')
        filename = os.path.join(data_dir, f'{enterprise_id}.json')
        # Check if enterprise exists
        if not os.path.exists(filename):
            return jsonify({'message': f'Empresa com ID {enterprise_id} não encontrada'}), 400
        # Get request data
        data = request.get_json()
        # Validate that at least one field is present to update
        if not data:
            return jsonify({'message': 'Nenhum dado fornecido para atualização'}), 400
        # Read current enterprise data
        with open(filename, 'r', encoding='utf-8') as f:
            enterprise_data = json.load(f)
        # Update the provided fields
        for field in data:
            if field in enterprise_data:
                enterprise_data[field] = data[field]
        # Write updated data back
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(enterprise_data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': f'Dados da empresa com ID {enterprise_id} atualizados com sucesso'}), 200
    except Exception as e:
        return jsonify({'message': 'Erro interno do servidor.',
                        'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
