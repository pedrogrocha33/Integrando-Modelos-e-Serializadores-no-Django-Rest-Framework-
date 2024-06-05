FROM python:3.8-slim

# Instala as dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Define o diretório de trabalho
WORKDIR /opt/pysetup

# Copia os arquivos de dependências
COPY poetry.lock pyproject.toml ./

# Instala as dependências do Python
RUN poetry install --no-dev --no-root

# Copia o restante dos arquivos do aplicativo
COPY app

# Expõe a porta 8000
EXPOSE 8000

# Comando para rodar o aplicativo
CMD ["poetry", "run", "uvicorn", "bookstore.main:app", "--host", "0.0.0.0", "--port", "8000"]
