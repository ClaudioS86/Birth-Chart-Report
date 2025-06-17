FROM python:3.9-slim

# Installa build tools + git
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    build-essential \
    libc-dev \
 && rm -rf /var/lib/apt/lists/*
 
RUN apt-get update && apt-get install -y gcc make && \
    git clone https://github.com/andrmoel/astrolog.git && \
    cd astrolog/source && make && \
    cp astrolog /usr/local/bin/astrolog && \
    chmod +x /usr/local/bin/astrolog
    
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
