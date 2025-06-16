FROM python:3.9-slim

# Installa build tools + git
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    build-essential \
    libc-dev \
 && rm -rf /var/lib/apt/lists/*
 
# Installa Astrolog
RUN git clone https://github.com/rswwoo/astrolog.git /astrolog && \
    cd /astrolog && make && \
    cp astrolog /usr/local/bin/astrolog
    
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
