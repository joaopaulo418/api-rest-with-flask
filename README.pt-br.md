# 🧠 Projeto de Estudo: API de Gerenciamento de Usuários

Este é um projeto pessoal com o objetivo de estudar e praticar os principais métodos de uma API REST usando Flask. A aplicação simula um sistema de gerenciamento de usuários e empresas, permitindo **criar, atualizar, remover e consultar dados** de forma simples e organizada.

---

## 🚀 Funcionalidades

- ✅ Adicionar novos usuários e empresas (`POST`)
- 🔍 Obter todos os usuários e empresas (`GET`)
- 🔎 Obter um usuário ou empresa específica (`GET`)
- ✏️ Atualizar **totalmente** as informações de um usuário ou empresa (`PUT`)
- 🛠️ Atualizar **parcialmente** as informações de um usuário ou empresa (`PATCH`)
- 🗑️ Remover um usuário ou empresa (ao remover uma empresa, todos os usuários associados a ela serão removidos) (`DELETE`)

---

## 🐍 Tecnologias utilizadas

| Tecnologia | Versão | Observação                  |
|------------|--------|-----------------------------|
| Python     | 3.12.3 | Linguagem principal          |
| Flask      | 3.0.2  | Framework web                |
| json       | nativo | Módulo embutido no Python    |
| os         | nativo | Módulo embutido no Python    |

> ⚠️ Os módulos `json` e `os` já vêm com o Python e **não precisam ser instalados** via pip.

---

## 🛡️ Regras de negócio

- O campo **`cnpj`** é utilizado como **identificador único** das empresas no momento do cadastro.
- Não é possível cadastrar duas empresas com o mesmo `cnpj`.
- Validações básicas são feitas para garantir a integridade dos dados recebidos.

---

## 📡 Métodos HTTP utilizados

| Método | Finalidade|
|--------|-----------|
| `GET`  | Buscar um ou todos os usuários ou empresas|
| `POST` | Criar um novo usuário ou empresa|
| `DELETE` | Remover um usuário ou empresa existente|
| `PUT`  | Atualizar **todos os dados** de um usuário ou empresa|
| `PATCH`| Atualizar **dados parciais** de um usuário ou empresa|

---

## 🔀 Rotas da API

### Rota `/users`

| Método | Rota            | Descrição                                |
|--------|------------------|--------------------------------------------|
| `POST` | `/users`          | Cria um novo usuário                       |
| `GET`  | `/users`          | Retorna **todos os usuários**             |
| `GET`  | `/users/<id>`     | Retorna um **usuário específico** pelo ID |
| `PUT`  | `/users/<id>`     | Atualiza **completamente** um usuário     |
| `PATCH`| `/users/<id>`     | Atualiza **parcialmente** um usuário      |
| `DELETE`| `/users/<id>`    | Remove um usuário do sistema              |

### Rota `/enterprises`

| Método | Rota            | Descrição                                |
|--------|------------------|--------------------------------------------|
| `POST` | `/enterprises`          | Cria uma nova empresa                      |
| `GET`  | `/enterprises`          | Retorna **todas as empresas**             |
| `GET`  | `/enterprises/<id>`     | Retorna uma **empresa específica** pelo ID |
| `PUT`  | `/enterprises/<id>`     | Atualiza **completamente** uma empresa    |
| `PATCH`| `/enterprises/<id>`     | Atualiza **parcialmente** uma empresa     |
| `DELETE`| `/enterprises/<id>`    | Remove uma empresa do sistema            |
---

## 🗂️ Estrutura esperada do JSON

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