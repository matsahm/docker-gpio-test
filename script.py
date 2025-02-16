import RPi.GPIO as GPIO
import signal
import sys
import time

# GPIO-Pins
LED1 = 12
LED2 = 16
BUTTON1 = 1
BUTTON2 = 7

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED Status speichern
led_states = {LED1: False, LED2: False}

# Callback-Funktionen für Taster
def toggle_led(led, button):
    if GPIO.input(button) == GPIO.LOW:  # Prüfen, ob noch gedrückt
        led_states[led] = not led_states[led]
        GPIO.output(led, led_states[led])

# Event-Erkennung für Taster
GPIO.add_event_detect(BUTTON1, GPIO.FALLING, callback=lambda channel: toggle_led(LED1, BUTTON1), bouncetime=50)
GPIO.add_event_detect(BUTTON2, GPIO.FALLING, callback=lambda channel: toggle_led(LED2, BUTTON2), bouncetime=50)

# Cleanup-Funktion für sicheres Beenden
def cleanup(signum, frame):
    print("\nBeenden... GPIO Cleanup")
    GPIO.cleanup()
    sys.exit(0)

# Signal-Handler für SIGINT (Strg+C) und SIGTERM
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

# Endlosschleife
print("Taster drücken, um LEDs zu schalten. Beenden mit Strg+C.")
while True:
    time.sleep(1)  # Idle
