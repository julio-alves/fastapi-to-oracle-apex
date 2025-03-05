from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

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

# Endpoint com paginação
@app.get("/produtos", response_model=List[Produto])
def listar_produtos(skip: int = Query(0, alias="pagina", ge=0), limit: int = Query(10, alias="tamanho", ge=1, le=100)):
    """
    Retorna uma lista paginada de produtos.
    - `pagina`: Índice inicial dos resultados (default=0)
    - `tamanho`: Número de itens por página (default=10, máximo=100)
    """
    return produtos_db[skip: skip + limit]

# Para rodar no Render
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
