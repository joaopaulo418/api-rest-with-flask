import os
import json
from flask import request, jsonify


def create_company():
    """Create a new company and save their data to a JSON file."""
    try:
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['cnpj', 'name', 'area_of_activity']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Incomplete data',
                            'error': 'Missing required fields'}), 400
        # Verify CNPJ length
        if len(data['cnpj']) != 14:
            return jsonify({'message': 'CNPJ must be 14 characters long',
                            'error': 'Invalid CNPJ length'}), 400
        # Accessing data directory
        data_dir = os.path.join(os.getcwd(), 'data', 'companies')
        # Check if directory is empty, if so initialize next_id as 1
        if not os.listdir(data_dir):
            next_id = 1
        else:
            # Check if CNPJ already exists
            for filename in os.listdir(data_dir):
                if filename.endswith('.json'):
                    file_path = os.path.join(data_dir, filename)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        existing_data = json.load(f)
                        if existing_data.get('cnpj') == data['cnpj']:
                            return jsonify({'message': 'CNPJ already exists',
                                            'error': 'CNPJ already exists'}), 400

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
        data['company_id'] = next_id
        # Save user data to JSON file
        filename = os.path.join(os.getcwd(), 'data', 'companies', f'{next_id}.json')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': 'Company created successfully!',
                        'company_id': next_id}), 200
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


def get_companies():
    """Return a list of all companies from the data directory."""
    try:
        companies = []
        data_dir = os.path.join(os.getcwd(), 'data', 'companies')
        # Read all JSON files in the data directory
        for filename in os.listdir(data_dir):
            if filename.endswith('.json'):
                file_path = os.path.join(data_dir, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    company_data = json.load(f)
                    companies.append(company_data)
        return jsonify(companies), 200
    except FileNotFoundError:
        return jsonify({'message': 'Companies not found',
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


def get_company(company_id):
    """Return the company data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'companies')
        filename = os.path.join(data_dir, f'{company_id}.json')
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                company_data = json.load(f)
            return jsonify(company_data), 200
        return jsonify({'message': f'Company with ID {company_id} not found',
                        'error': 'Company not found'}), 400
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


def delete_company(company_id):
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'companies')
        filename = os.path.join(data_dir, f'{company_id}.json')
        if not os.path.exists(filename):
            return jsonify({'message': f'Company with ID {company_id} not found',
                            'error': 'Company not found'}), 400
        os.remove(filename)
        # Remove all users associated with this company
        users_dir = os.path.join(os.getcwd(), 'data', 'users')
        for user_file in os.listdir(users_dir):
            if user_file.endswith('.json'):
                user_path = os.path.join(users_dir, user_file)
                with open(user_path, 'r', encoding='utf-8') as f:
                    user_data = json.load(f)
                    if user_data['company_id'] == company_id:
                        os.remove(user_path)
        return jsonify({'message': f'Empresa e usuários associados com ID {company_id} deletados com sucesso'}), 200
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


def update_full_company(company_id):
    """Update all company data for a given ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'companies')
        filename = os.path.join(data_dir, f'{company_id}.json')
        # Check if company exists
        if not os.path.exists(filename):
            return jsonify({'message': f'Company with ID {company_id} not found',
                            'error': 'Company not found'}), 400
        # Get request data
        data = request.get_json()
        # Validate required fields are present in the request data
        required_fields = ['name', 'cnpj', 'area_of_activity']
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Incomplete data',
                            'error': 'Missing required fields'}), 400
        # Verify CNPJ length
        if len(data['cnpj']) != 14:
            return jsonify({'message': 'CNPJ must be 14 characters long',
                            'error': 'Invalid CNPJ length'}), 400
        # Preserve the company_id
        data['company_id'] = company_id
        # Write updated data
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': f'Company with ID {company_id} updated successfully'}), 200
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


def update_any_field_company(company_id):
    """Update any company data field for a given company ID."""
    try:
        data_dir = os.path.join(os.getcwd(), 'data', 'companies')
        filename = os.path.join(data_dir, f'{company_id}.json')
        # Check if company exists
        if not os.path.exists(filename):
            return jsonify({'message': f'Company with ID {company_id} not found',
                            'error': 'Company not found'}), 400
        # Get request data
        data = request.get_json()
        if "cnpj" in data:
            # Verify CNPJ length
            if len(data['cnpj']) != 14:
                return jsonify({'message': 'CNPJ must be 14 characters long',
                                'error': 'Invalid CNPJ length'}), 400
        # Validate that at least one field is present to update
        if not data:
            return jsonify({'message': 'No data provided for update',
                            'error': 'Missing update data'}), 400
        # Read current company data
        with open(filename, 'r', encoding='utf-8') as f:
            company_data = json.load(f)
        # Update the provided fields
        for field in data:
            if field in company_data:
                company_data[field] = data[field]
        # Write updated data back
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(company_data, f, indent=4, ensure_ascii=False)
        return jsonify({'message': f'Company with ID {company_id} updated successfully'}), 200
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
