# 🌐 Códigos de Status HTTP

Os códigos de status HTTP são retornados pelo servidor para indicar o resultado de uma requisição. Aqui estão os principais códigos utilizados nesta API:

## ✅ Códigos de Sucesso (2xx)

- **200 (OK)**
  - ✨ Requisição bem-sucedida
  - 🎯 O servidor processou a solicitação com sucesso e retornou os dados solicitados
  - 💡 Exemplo: Criação/atualização de usuário ou empresa realizada com sucesso

## ⚠️ Códigos de Erro do Cliente (4xx)

- **400 (Bad Request)**
  - ❌ Erro nos dados enviados pelo cliente
  - 📝 A requisição contém dados inválidos ou campos obrigatórios ausentes
  - 🔍 Exemplos:
    - Campos requeridos faltando no corpo da requisição
    - CNPJ com formato inválido
    - Tentativa de criar usuário sem empresa cadastrada

## 🚫 Códigos de Erro do Servidor (5xx)

- **500 (Internal Server Error)**
  - 💥 Erro interno no servidor
  - ⚡ Ocorreu um problema durante o processamento da requisição
  - 🔧 Possíveis causas:
    - Erro ao manipular arquivos
    - Falha ao processar JSON
    - Problemas de permissão de acesso
    - Exceções não tratadas