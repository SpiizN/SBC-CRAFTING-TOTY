from pynput import mouse
import time
import signal
import sys

def enregistrer_coordonnees(x, y, button, pressed):
    if pressed:
        coordonnees = f"Coordonnées de clic : ({x}, {y})"
        print(coordonnees)
        
        with open("coord.csv", "a") as fichier:
            fichier.write(f"{x},{y}\n")

def arreter_script(signal, frame):
    print("Arrêt du script.")
    sys.exit(0)

# Configurer le gestionnaire de signal pour intercepter Ctrl+C
signal.signal(signal.SIGINT, arreter_script)

# Configurer le gestionnaire d'événements de la souris
listener = mouse.Listener(on_click=enregistrer_coordonnees)

# Démarrer le gestionnaire d'événements en arrière-plan
listener.start()

# Attendre que le gestionnaire d'événements se termine (ce qui n'arrivera pas dans ce script)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Intercepter Ctrl+C pour permettre un arrêt propre du script
    pass
finally:
    # Arrêter le gestionnaire d'événements
    listener.stop()
    listener.join()
