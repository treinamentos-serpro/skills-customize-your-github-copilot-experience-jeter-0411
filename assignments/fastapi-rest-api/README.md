# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar livros usando FastAPI. Pratique rotas HTTP, validação de dados com Pydantic, operações CRUD e códigos de status HTTP.

## 📝 Tarefas

### 🛠️ Criar o app e uma rota de saúde

#### Descrição
Prepare o ambiente, execute o app fornecido e implemente uma rota que permita verificar se a API está disponível. O FastAPI também gera uma interface interativa para testar as rotas.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `python -m pip install "fastapi[standard]"`.
- Iniciar o servidor com `fastapi dev starter-code.py`.
- Implementar `GET /health`, retornando o JSON `{"status": "ok"}`.
- Permitir testar a API pela documentação interativa em `/docs`.

### 🛠️ Criar e listar livros

#### Descrição
Implemente as operações para adicionar livros à coleção em memória e consultar todos os livros cadastrados. Use os modelos Pydantic fornecidos para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para criar um livro com título e autor e atribuir a ele um ID único.
- Retornar o livro criado com status HTTP `201`.
- Implementar `GET /books` para retornar todos os livros, incluindo uma lista vazia quando não houver nenhum.
- Rejeitar título ou autor vazio e retornar os erros de validação do FastAPI.

### 🛠️ Consultar, atualizar e excluir livros

#### Descrição
Complete as operações CRUD permitindo consultar um livro por ID, atualizar seus dados e removê-lo da coleção.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` e retornar `404` quando o ID não existir.
- Implementar `PUT /books/{book_id}` para atualizar título e autor, retornando `404` para IDs inexistentes.
- Implementar `DELETE /books/{book_id}` para excluir um livro e retornar `404` para IDs inexistentes.
- Retornar status HTTP `204` ao excluir um livro com sucesso.
