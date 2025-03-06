FROM python:3.11

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copia dos arquivos do projeto para o container
COPY . /app

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Porta que será usada pelo FastAPI
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
