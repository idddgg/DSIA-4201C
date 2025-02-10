# Utiliser une image de base Python 3.10 slim
FROM python:3.10-slim

# Installer les outils système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    gnupg \
    unzip \
    libx11-6 \
    libx11-dev \
    libglib2.0-0 \
    libnss3 \
    libxss1 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1

# Ajouter le dépôt officiel de Google Chrome et installer google-chrome-stable
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Installer les outils de compilation essentiels
RUN apt-get update && apt-get install -y --no-install-recommends build-essential python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Télécharger et installer explicitement ChromeDriver version 132.0.6834.159
RUN wget -O /tmp/chromedriver_linux64.zip https://storage.googleapis.com/chrome-for-testing-public/132.0.6834.159/linux64/chromedriver-linux64.zip \
    && unzip -j /tmp/chromedriver_linux64.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver_linux64.zip

# Mettre à jour pip et installer les dépendances Python
RUN pip install --upgrade pip setuptools wheel

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les packages Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le conteneur
COPY . .

# Positionner le répertoire de travail sur le dossier du projet Scrapy
WORKDIR /app/bmw_scraper


