FROM python:3.9-slim

# Installa build tools + git
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    build-essential \
    libc-dev \
 && rm -rf /var/lib/apt/lists/*
 
RUN apt-get update && apt-get install -y wget unzip gcc make && \
    wget https://mirror.slitaz.org/astrolog/astsrc.zip && \
    unzip astsrc.zip && cd astrolog && \
    make && \
    cp astrolog /usr/local/bin/astrolog && \
    chmod +x /usr/local/bin/astrolog
    
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
