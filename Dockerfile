FROM python:3.9-slim

# Installa build tools + git
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    build-essential \
    libc-dev \
 && rm -rf /var/lib/apt/lists/*
 
# Installa Astrolog precompilato da SourceForge
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://downloads.sourceforge.net/project/astrolog/astrolog/7.40/astrolog740linux.zip && \
    unzip astrolog740linux.zip && \
    chmod +x astrolog && \
    mv astrolog /usr/local/bin/
    
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
