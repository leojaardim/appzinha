# Use a imagem base do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da aplicação para o container
COPY app.py /app
COPY templates /app/templates

# Instala as dependências
RUN pip install --no-cache-dir Flask

# Define a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Expõe a porta que o Flask usará
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
