import os
import json
import re
from flask import request, jsonify


def create_user():
    """Create a new user and save their data to a JSON file."""
    try:
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['name', 'company_id', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Incomplete data',
                            'error': 'Missing required fields'}), 400
        # Check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
            return jsonify({'message': 'Invalid email',
                            'error': 'Invalid email'}), 400
        # Accessing data directory
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        # Check if company exists
        company_dir = os.path.join(os.getcwd(), 'data', 'companies')
        company_file = os.path.join(company_dir, f"{data['company_id']}.json")
        if not os.path.exists(company_file):
            return jsonify({'message': 'Please register your company first',
                            'error': 'Company not found'}), 400
        # Check if directory is empty, if so initialize next_id as 1
        if not os.listdir(data_dir):
            next_id = 1
        else:
            # List containing all existing ids
            existing_ids = []
            # Loop through all files in directory with their names ['1.json', '2.json', etc...]
            for filename in os.listdir(data_dir):
                # Check if file ends with .json
                if not filename.endswith('.json'):
                    continue
                # Convert filename to integer
                file_id = int(filename.replace('.json', ''))
                # Add found id to list of existing ids
                existing_ids.append(file_id)
            # If list of existing ids is not empty, find highest id and increment by 1 and if list of existing ids is empty, first id will be 1
            next_id = max(existing_ids) + 1 if existing_ids else 1
        # Add the generated ID to the request data
        data['id_user'] = next_id
        # Save user data to JSON file
        filename = os.path.join(os.getcwd(), 'data', 'users', f'{next_id}.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': 'User created successfully!',
                        'id_user': data['id_user']}), 200
    except FileNotFoundError:
        return jsonify({'message': 'File not found',
                        'error': 'FileNotFoundError'}), 500
    except json.JSONDecodeError:
        return jsonify({'message': 'Error processing JSON file',
                        'error': 'json.JSONDecodeError'}), 500
    except PermissionError:
        return jsonify({'message': 'Permission denied to access files',
                        'error': 'PermissionError'}), 500
    except OSError:
        return jsonify({'message': 'Error manipulating system files',
                        'error': 'OSError'}), 500
    except Exception as e:
        return jsonify({'message': 'Internal server error',
                        'error': str(e)}), 500


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
    except FileNotFoundError:
        return jsonify({'message': 'Users not found',
                        'error': 'FileNotFoundError'}), 500
    except json.JSONDecodeError:
        return jsonify({'message': 'Error processing JSON file',
                        'error': 'json.JSONDecodeError'}), 500
    except PermissionError:
        return jsonify({'message': 'Permission denied to access files',
                        'error': 'PermissionError'}), 500
    except OSError:
        return jsonify({'message': 'Error manipulating system files',
                        'error': 'OSError'}), 500
    except Exception as e:
        return jsonify({'message': 'Internal server error',
                        'error': str(e)}), 500


def get_user(user_id):
    """Return the user data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        filename = os.path.join(data_dir, f'{user_id}.json')
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                user_data = json.load(f)
            return jsonify(user_data), 200
        return jsonify({'message': f'User with ID {user_id} not found',
                        'error': 'User not found'}), 400
    except FileNotFoundError:
        return jsonify({'message': 'File not found',
                        'error': 'FileNotFoundError'}), 500
    except json.JSONDecodeError:
        return jsonify({'message': 'Error processing JSON file',
                        'error': 'json.JSONDecodeError'}), 500
    except PermissionError:
        return jsonify({'message': 'Permission denied to access files',
                        'error': 'PermissionError'}), 500
    except OSError:
        return jsonify({'message': 'Error manipulating system files',
                        'error': 'OSError'}), 500
    except Exception as e:
        return jsonify({'message': 'Internal server error',
                        'error': str(e)}), 500


def delete_user(user_id):
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        filename = os.path.join(data_dir, f'{user_id}.json')
        if not os.path.exists(filename):
            return jsonify({'message': f'User with ID {user_id} not found',
                            'error': 'User not found'}), 400
        os.remove(filename)
        return jsonify({'message': f'User with ID {user_id} deleted successfully'}), 200
    except FileNotFoundError:
        return jsonify({'message': 'File not found',
                        'error': 'FileNotFoundError'}), 500
    except PermissionError:
        return jsonify({'message': 'Permission denied to access files',
                        'error': 'PermissionError'}), 500
    except OSError:
        return jsonify({'message': 'Error manipulating system files',
                        'error': 'OSError'}), 500
    except Exception as e:
        return jsonify({'message': 'Internal server error',
                        'error': str(e)}), 500


def update_full_user(user_id):
    """Update all user data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        filename = os.path.join(data_dir, f'{user_id}.json')
        # Check if user exists
        if not os.path.exists(filename):
            return jsonify({'message': f'User with ID {user_id} not found',
                            'error': 'User not found'}), 400
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['name', 'company_id', 'email', 'password']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Incomplete data',
                            'error': 'Missing required fields'}), 400
        # Check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
            return jsonify({'message': 'Invalid email',
                            'error': 'Invalid email'}), 400
        # Preserve the user_id
        data['id_user'] = user_id
        # Write updated data
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': f'User with ID {user_id} updated successfully'}), 200
    except FileNotFoundError:
        return jsonify({'message': 'File not found',
                        'error': 'FileNotFoundError'}), 500
    except json.JSONDecodeError:
        return jsonify({'message': 'Error processing JSON file',
                        'error': 'json.JSONDecodeError'}), 500
    except PermissionError:
        return jsonify({'message': 'Permission denied to access files',
                        'error': 'PermissionError'}), 500
    except OSError:
        return jsonify({'message': 'Error manipulating system files',
                        'error': 'OSError'}), 500
    except Exception as e:
        return jsonify({'message': 'Internal server error',
                        'error': str(e)}), 500


def update_any_field_user(user_id):
    """Update any user data field for a given user ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'users')
        filename = os.path.join(data_dir, f'{user_id}.json')
        # Check if user exists
        if not os.path.exists(filename):
            return jsonify({'message': f'User with ID {user_id} not found',
                            'error': 'User not found'}), 400
        # Get request data
        data = request.get_json()
        # Validate that at least one field is present to update
        if not data:
            return jsonify({'message': 'No data provided for update',
                            'error': 'Missing update data'}), 400
        if "email" in data:
            # Check if email is valid
            if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
                return jsonify({'message': 'Invalid email',
                                'error': 'Invalid email'}), 400
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
        return jsonify({'message': f'User with ID {user_id} updated successfully'}), 200
    except FileNotFoundError:
        return jsonify({'message': 'File not found',
                        'error': 'FileNotFoundError'}), 500
    except json.JSONDecodeError:
        return jsonify({'message': 'Error processing JSON file',
                        'error': 'json.JSONDecodeError'}), 500
    except PermissionError:
        return jsonify({'message': 'Permission denied to access files',
                        'error': 'PermissionError'}), 500
    except OSError:
        return jsonify({'message': 'Error manipulating system files',
                        'error': 'OSError'}), 500
    except Exception as e:
        return jsonify({'message': 'Internal server error',
                        'error': str(e)}), 500
