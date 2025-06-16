FROM python:3.9-slim

# Installa build tools + git
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    build-essential \
    libc-dev \
 && rm -rf /var/lib/apt/lists/*
 
# Installa astrolog da repository pubblico alternativo
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://www.astrolog.org/ftp/astrolog7.60linux.zip && \
    unzip astrolog7.60linux.zip && \
    chmod +x astrolog && \
    mv astrolog /usr/local/bin/
    
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
