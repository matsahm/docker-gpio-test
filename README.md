# docker-gpio-test
Docker Container um GPIO-Kontakte zu testen.

## Software-Voraussetzungen
- Raspberry Pi OS

## Hardware-Voraussetzungen
2 LEDs anschließen:
- GPIO 12/16 → Vorwiderstand (abhängig von der LED)
- Vorwiderstand → Anode der LED (+, längeres Beinchen)
- Kathode der LED (-, kürzeres Beinchen) → GND vom Raspberry Pi

2 Taster anchließen:
- GPIO 1/7 → Taster
- Taster → GND vom Raspberry Pi

## Docker installieren
curl -fsSL https://get.Docker.com -o get-Docker.sh
sudo sh get-Docker.sh
sudo usermod -aG docker $USER
newgrp docker

## Ausführen
Im Vordergrund: `docker compose up`
Im Hintergrund: `docker compose up -d`
