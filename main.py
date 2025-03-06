from fastapi import FastAPI, Query, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Dict, Any
import random
import math

app = FastAPI()

# Inicializando o sistema de autenticação
security = HTTPBasic()

# Usuário e senha simples para autenticação
USER_DB = {"admin": "senha123"}  # Usuário "admin" com senha "senha123"

# Modelo de Produto
class Produto(BaseModel):
    ID: int
    CODIGO: str
    DESCRICAO: str
    PRECO_PADRAO: float
    CATEGORIA: str
    STATUS: str
    QT_ESTOQUE: int
    COR: str

# Lista de categorias e cores para dados aleatórios
CATEGORIAS = ["Eletrônicos", "Informática", "Eletrodomésticos", "Móveis", "Brinquedos"]
CORES = ["Preto", "Branco", "Azul", "Vermelho", "Cinza", "Verde", "Amarelo"]
STATUS_LIST = ["A", "I"]  # A = Ativo, I = Inativo

# Gerando 1000 registros aleatórios
produtos_db = [
    {
        "ID": i,
        "CODIGO": f"PROD{i:04d}",
        "DESCRICAO": f"Produto {i}",
        "PRECO_PADRAO": round(random.uniform(10, 5000), 2),
        "CATEGORIA": random.choice(CATEGORIAS),
        "STATUS": random.choice(STATUS_LIST),
        "QT_ESTOQUE": random.randint(0, 100),
        "COR": random.choice(CORES)
    }
    for i in range(1, 1001)
]

# Configuração fixa da paginação
TAMANHO_PAGINA = 10

# Função de verificação de autenticação
def verificar_autenticacao(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = USER_DB.get(credentials.username)
    if not correct_username or correct_username != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha inválidos",
            headers={"WWW-Authenticate": "Basic"},
        )

# Endpoint público: Retorna lista de produtos com paginação
@app.get("/produtos", response_model=Dict[str, Any])
def listar_produtos(pagina: int = Query(1, ge=1)):
    """
    Retorna uma lista paginada de produtos.
    - `pagina`: Número da página (começa em 1)
    """
    total_produtos = len(produtos_db)
    total_paginas = math.ceil(total_produtos / TAMANHO_PAGINA)

    start = (pagina - 1) * TAMANHO_PAGINA
    end = start + TAMANHO_PAGINA

    return {
        "pagina_atual": pagina,
        "total_paginas": total_paginas,
        "dados": produtos_db[start:end]
    }

# Endpoint com autenticação básica: Exemplo de consulta de produtos protegida
@app.get("/produtos-seguro", response_model=Dict[str, Any])
def listar_produtos_segurado(
    pagina: int = Query(1, ge=1),
    credentials: HTTPBasicCredentials = Depends(verificar_autenticacao)
):
    """
    Retorna uma lista paginada de produtos, mas este endpoint está protegido por autenticação básica.
    - `pagina`: Número da página (começa em 1)
    """
    total_produtos = len(produtos_db)
    total_paginas = math.ceil(total_produtos / TAMANHO_PAGINA)

    start = (pagina - 1) * TAMANHO_PAGINA
    end = start + TAMANHO_PAGINA

    return {
        "pagina_atual": pagina,
        "total_paginas": total_paginas,
        "dados": produtos_db[start:end]
    }

# Para rodar no Render
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
