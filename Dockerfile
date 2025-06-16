FROM python:3.9-slim

# Installa build tools + git
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    build-essential \
    libc-dev \
 && rm -rf /var/lib/apt/lists/*
 
# Installa Astrolog da una repo pubblica GitHub (senza login)
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gcc \
    make && \
    wget https://github.com/andrmoel/astrolog/archive/refs/heads/master.zip && \
    unzip master.zip && \
    cd astrolog-master/source && \
    make && \
    cp astrolog /usr/local/bin/
    
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
