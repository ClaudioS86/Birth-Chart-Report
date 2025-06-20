FROM debian:bullseye-slim

# Installa dipendenze
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    unzip \
    imagemagick \
    && rm -rf /var/lib/apt/lists/*

# Crea dir per app
WORKDIR /app

# Scarica Astrolog
RUN wget https://www.astrolog.org/astrolog/astrolog7.40_linux.zip \
    && unzip astrolog7.40_linux.zip \
    && chmod +x astrolog \
    && mv astrolog /usr/local/bin/ \
    && rm astrolog7.40_linux.zip

# Copia gli script
COPY app.py .
COPY generate_chart.sh .

# Rendi eseguibile lo script
RUN chmod +x generate_chart.sh

CMD ["python3", "app.py"]
