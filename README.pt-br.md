# 🧠 Projeto de Estudo: API de Gerenciamento de Usuários

Este é um projeto pessoal com o objetivo de estudar e praticar os principais métodos de uma API REST usando Flask. A aplicação simula um sistema de gerenciamento de usuários, permitindo **criar, atualizar, remover e consultar dados** de forma simples e organizada.

---

## 🚀 Funcionalidades

- ✅ Adicionar novos usuários (`POST`)
- 🔍 Obter todos os usuários (`GET`)
- 🔎 Obter um usuário específico (`GET`)
- ✏️ Atualizar **totalmente** as informações de um usuário (`PUT`)
- 🛠️ Atualizar **parcialmente** as informações de um usuário (`PATCH`)
- 🗑️ Remover um usuário (`DELETE`)

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

## 🛡️ Regra de negócio

- O campo **`cnpj`** é utilizado como **identificador único** dos usuários no momento do cadastro.
- Não é possível cadastrar dois usuários com o mesmo `cnpj`.
- Validações básicas são feitas para garantir integridade nos dados recebidos.

---

## 📡 Métodos HTTP utilizados

| Método | Finalidade                           |
|--------|--------------------------------------|
| `GET`  | Buscar um ou todos os usuários       |
| `POST` | Criar um novo usuário                |
| `DELETE` | Remover um usuário existente       |
| `PUT`  | Atualizar **todos os dados**         |
| `PATCH`| Atualizar **dados parciais**         |

---

## 🔀 Rotas da API

A base da API é a rota `/user`. A manipulação de usuários individuais é feita através da inclusão do `id` ao final da rota:

| Método | Rota            | Descrição                                |
|--------|------------------|--------------------------------------------|
| `POST` | `/user`          | Cria um novo usuário                       |
| `GET`  | `/user`          | Retorna **todos os usuários**             |
| `GET`  | `/user/<id>`     | Retorna um **usuário específico** pelo ID |
| `PUT`  | `/user/<id>`     | Atualiza **completamente** um usuário     |
| `PATCH`| `/user/<id>`     | Atualiza **parcialmente** um usuário      |
| `DELETE`| `/user/<id>`    | Remove um usuário do sistema              |

---

## 🗂️ Estrutura esperada do JSON

```json
{
  "name_user": "João",
  "name_enterprise": "Empresa X",
  "cnpj": "12345678000100",
  "area_of_activity": "Tecnologia",
  "email": "joao@exemplo.com",
  "password": "987123"
}
