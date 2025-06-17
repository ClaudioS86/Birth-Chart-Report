FROM python:3.9-slim

# Installa build tools + git
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    build-essential \
    libc-dev \
 && rm -rf /var/lib/apt/lists/*
 
# Installa unzip e copia astrolog binario già pronto
RUN apt-get update && apt-get install -y wget tar && \
    wget https://astrolog-distro.s3.eu-west-1.amazonaws.com/astrolog-linux64.tar.gz && \
    tar -xzf astrolog-linux64.tar.gz && \
    mv astrolog /usr/local/bin/astrolog && \
    chmod +x /usr/local/bin/astrolog
    
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
