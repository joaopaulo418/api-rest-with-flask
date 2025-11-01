from flask import Flask
from routes.companies import create_company, get_companies, get_company, delete_company, update_full_company, update_any_field_company
from routes.users import create_user, get_users, get_user, delete_user, update_full_user, update_any_field_user

# pylint: disable=C0301, C0114, W0718, C0114, C0116

app = Flask(__name__)

@app.route('/companies', methods=['POST'])
def create_company():
    return create_company()

@app.route('/users', methods=['POST'])
def create_user():
    return create_user()

@app.route('/users', methods=['GET'])
def get_users():
    return get_users()

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return get_user(user_id)

@app.route('/companies', methods=['GET'])
def get_companies():
    return get_companies()

@app.route('/companies/<int:company_id>', methods=['GET'])
def get_company(company_id):
    return get_company(company_id)

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user(user_id)

@app.route('/companies/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    return delete_company(company_id)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_full_user(user_id):
    return update_full_user(user_id)

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_any_field_user(user_id):
    return update_any_field_user(user_id)

@app.route('/companies/<int:company_id>', methods=['PUT'])
def update_full_company(company_id):
    return update_full_company(company_id)

@app.route('/companies/<int:company_id>', methods=['PATCH'])
def update_any_field_company(company_id):
    return update_any_field_company(company_id)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
