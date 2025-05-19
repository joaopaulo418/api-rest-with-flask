# 🧠 Study Project: User Management API

This is a personal project aimed at studying and practicing the main methods of a REST API using Flask. The application simulates a user management system, allowing you to **create, update, remove and query data** in a simple and organized way.

---

## 🚀 Features

- ✅ Add new users (`POST`)
- 🔍 Get all users (`GET`) 
- 🔎 Get a specific user (`GET`)
- ✏️ **Fully** update user information (`PUT`)
- 🛠️ **Partially** update user information (`PATCH`)
- 🗑️ Remove a user (`DELETE`)

---

## 🐍 Technologies Used

| Technology | Version | Note                        |
|------------|---------|----------------------------|
| Python     | 3.12.3  | Main language              |
| Flask      | 3.0.2   | Web framework              |
| json       | native  | Built-in Python module     |
| os         | native  | Built-in Python module     |

> ⚠️ The `json` and `os` modules come with Python and **do not need to be installed** via pip.

---

## 🛡️ Business Rules

- The **`cnpj`** field is used as a **unique identifier** for users during registration.
- It is not possible to register two users with the same `cnpj`.
- Basic validations are performed to ensure data integrity.

---

## 📡 HTTP Methods Used

| Method | Purpose                              |
|--------|--------------------------------------|
| `GET`  | Fetch one or all users               |
| `POST` | Create a new user                    |
| `DELETE` | Remove an existing user            |
| `PUT`  | Update **all data**                  |
| `PATCH`| Update **partial data**              |

---

## 🔀 API Routes

The API base route is `/user`. Individual user manipulation is done by including the `id` at the end of the route:

| Method | Route           | Description                               |
|--------|-----------------|------------------------------------------|
| `POST` | `/user`         | Creates a new user                       |
| `GET`  | `/user`         | Returns **all users**                    |
| `GET`  | `/user/<id>`    | Returns a **specific user** by ID        |
| `PUT`  | `/user/<id>`    | **Completely** updates a user            |
| `PATCH`| `/user/<id>`    | **Partially** updates a user             |
| `DELETE`| `/user/<id>`   | Removes a user from the system           |

---

## 🗂️ Expected JSON Structure

```json
{
  "name_user": "João",
  "name_enterprise": "Empresa X",
  "cnpj": "12345678000100",
  "area_of_activity": "Tecnologia",
  "email": "joao@exemplo.com",
  "password": "987123"
}
