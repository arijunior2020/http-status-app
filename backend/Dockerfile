FROM python:3.9-slim

WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do backend
COPY . .

CMD ["python", "app.py"]

