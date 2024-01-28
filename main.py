import pyautogui
import time
import random

def lire_coordonnees_fichier(nom_fichier):
    coordonnees = []
    with open(nom_fichier, "r") as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            x, y = map(int, ligne.strip().split(','))
            coordonnees.append((x, y))
    return coordonnees

def effectuer_clics(coordonnees, nb_sbc: int):
    pyautogui.hotkey('alt', 'tab') 
    time.sleep(1) 

    for i in range(int(nb_sbc)):
        pyautogui.click(930, 301)
        time.sleep(1.5)

        for x, y in coordonnees:
            if (x,y) in [(975,709)]:
                print(f"Nombre de SBC terminé : {i}")
                time.sleep(2)
            if (x,y) in [(987,633)]:
                time.sleep(2)
            pyautogui.click(x, y)
            random_delay() 

def random_delay():
    time.sleep(random.uniform(0.4, 1.2))

if __name__ == "__main__":
    nom_fichier = "coord.csv"
    coordonnees = lire_coordonnees_fichier(nom_fichier)

    if coordonnees:
        print(f"Coordonnées lues depuis {nom_fichier}: {coordonnees}")
        nb_sbc = input("Nombre de SBC à completer : ")

        print("")
        print(r"----- A LIRE :  Conditions d'utilisation ------")
        print(r"1 : Votre navigateur doit être sur la page des SBC favoris avec uniquement le défi 'Team of the Year Crafting upgrade'.")
        print(r"2 : Le navigateur utilisé pour les tests est Firefox. (Aucune garentie de fonctionnement sur les autres navigateurs.)")
        print(r"3 : Votre navigateur doit être à 70% d'affichage. (Indicateur en haut à droite de la bare d'adresse.) (Ctrl+scroll down pour dézoomer. )")
        
        time.sleep(5)
        input("Appuyez sur Enter pour commencer ...")

        effectuer_clics(coordonnees, nb_sbc)
        print("Clics effectués avec succès.")
    else:
        print(f"Aucune coordonnée n'a été lue depuis {nom_fichier}.")
