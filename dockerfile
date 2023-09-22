# Use a imagem base do Python
FROM python:3.8-slim

# Configurar variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY 0fcb89b2a2d0e096a566e836eb3644ea
ENV ALGORITHM HS256
ENV EXPIRES_IN_MIN 3000

# Configurar diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para o contêiner
COPY ./requirements.txt /app/requirements.txt

# Instalar as dependências do projeto
RUN pip install -r requirements.txt

# Copiar o restante dos arquivos do aplicativo para o contêiner
COPY . /app

# Expor a porta em que o aplicativo FastAPI estará em execução (por padrão, 8000)
EXPOSE 8000

# Comando para iniciar o aplicativo FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]