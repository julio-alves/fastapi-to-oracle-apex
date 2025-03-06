# API FastAPI - Cadastro de Produtos

Esta API foi construída com **FastAPI** e retorna um cadastro de **1000 produtos** simulados. Inclui **paginação** para facilitar consultas.

## 🚀 Como usar?

### 📌 Executar localmente
```bash
uvicorn main:app --reload
```

### 📦 Executar com Docker

#### 1️⃣ Construir a imagem Docker
```bash
docker build -t fastapi-app .
```

#### 2️⃣ Rodar o container
```bash
docker run -d -p 8000:8000 fastapi-app
```

#### 3️⃣ Acessar a API
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **OpenAPI JSON:** [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

#### 4️⃣ Testar no terminal
```bash
curl http://localhost:8000/produtos?pagina=1
```

## 🔒 API Segura com Basic Authentication
Alguns endpoints exigem autenticação básica (Basic Auth). Use as credenciais abaixo:

- **Usuário:** `admin`
- **Senha:** `senha123`

#### Exemplo de requisição autenticada
```bash
curl -u admin:senha123 http://localhost:8000/produtos-seguro?pagina=1
```

## 🛠 Dependências
Se estiver rodando localmente, instale as dependências com:
```bash
pip install -r requirements.txt
```

## 📌 Estrutura do Projeto
```
.
├── main.py  # Código principal da API
├── Dockerfile  # Configuração do Docker
├── requirements.txt  # Lista de dependências
└── README.md  # Documentação
```

Agora sua API FastAPI pode ser executada de forma simples com **Docker**! 🚀
