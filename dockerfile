FROM python:3.9

# Installiere die erforderlichen Bibliotheken
RUN pip install rpi-lgpio

# Setze das Arbeitsverzeichnis
WORKDIR /app

# Kopiere das Skript in den Container
COPY script.py /app/script.py

# Starte das Skript
CMD ["python", "/app/script.py"]
