# 🧠 Study Project: User Management API

This is a personal project aimed at studying and practicing the main methods of a REST API using Flask. The application simulates a user and company management system, allowing you to **create, update, remove and query data** in a simple and organized way.

---

## 🚀 Features

- ✅ Add new users and companies (`POST`)
- 🔍 Get all users and companies (`GET`)
- 🔎 Get a specific user or company (`GET`) 
- ✏️ **Fully** update user or company information (`PUT`)
- 🛠️ **Partially** update user or company information (`PATCH`)
- 🗑️ Remove a user or company (when removing a company, all associated users will be removed) (`DELETE`)

---

## 🐍 Technologies Used

| Technology | Version | Note                       |
|------------|---------|----------------------------|
| Python     | 3.12.3  | Main language             |
| Flask      | 3.0.2   | Web framework             |
| json       | native  | Built-in Python module     |
| os         | native  | Built-in Python module     |

> ⚠️ The `json` and `os` modules come with Python and **do not need to be installed** via pip.

---

## 🛡️ Business Rules

- The **`cnpj`** field is used as a **unique identifier** for companies during registration.
- It is not possible to register two companies with the same `cnpj`.
- Basic validations are performed to ensure the integrity of received data.

---

## 📡 HTTP Methods Used

| Method  | Purpose                                    |
|---------|-------------------------------------------|
| `GET`   | Fetch one or all users or companies       |
| `POST`  | Create a new user or company              |
| `DELETE`| Remove an existing user or company        |
| `PUT`   | Update **all data** of a user or company  |
| `PATCH` | Update **partial data** of a user or company|

---

## 🔀 API Routes

### `/users` Route

| Method   | Route           | Description                               |
|----------|-----------------|------------------------------------------|
| `POST`   | `/users`        | Creates a new user                       |
| `GET`    | `/users`        | Returns **all users**                    |
| `GET`    | `/users/<id>`   | Returns a **specific user** by ID        |
| `PUT`    | `/users/<id>`   | **Completely** updates a user            |
| `PATCH`  | `/users/<id>`   | **Partially** updates a user             |
| `DELETE` | `/users/<id>`   | Removes a user from the system           |

### `/enterprises` Route

| Method   | Route              | Description                               |
|----------|-------------------|------------------------------------------|
| `POST`   | `/enterprises`    | Creates a new company                     |
| `GET`    | `/enterprises`    | Returns **all companies**                 |
| `GET`    | `/enterprises/<id>` | Returns a **specific company** by ID    |
| `PUT`    | `/enterprises/<id>` | **Completely** updates a company        |
| `PATCH`  | `/enterprises/<id>` | **Partially** updates a company         |
| `DELETE` | `/enterprises/<id>` | Removes a company from the system       |
---

## 🗂️ Expected JSON Structure

### User:
```json
{
  "name_user": "João",
  "id_enterprise": 5,
  "email": "joao@exemplo.com",
  "password": "987123"
}
```
### Enterprise
```json
{
  "cnpj": "12345678000100",
  "name_enterprise": "Empresa X",
  "area_of_activity": "Tecnologia",
}
```
