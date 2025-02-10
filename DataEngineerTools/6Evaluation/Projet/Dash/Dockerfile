FROM python:3.10-slim

# Installer des outils système de base : procps (pour ps, top, etc.) et netcat (pour vérifier la disponibilité d'un port)
RUN apt-get update && apt-get install -y --no-install-recommends procps netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Mettre à jour pip et installer les dépendances Python
RUN pip install --upgrade pip setuptools wheel

# Définir le répertoire de travail et installer les dépendances Python
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'ensemble du code de l'application dans le conteneur
COPY . /app

# Exposer le port de l'application Dash
EXPOSE 8050

# Commande d'exécution :
# La commande inline attend que le service MongoDB (db) soit accessible sur le port 27017 avant de lancer l'application.
CMD sh -c "while ! nc -z db 27017; do echo 'Waiting for MongoDB...'; sleep 1; done; echo 'MongoDB is up'; python app.py"
