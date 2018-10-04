"""!
Ce module est le module principale pour lancer le jeu d'akiba.

Il consiste d'une fonction menu() qui permet à l'utilisateur de choisir comment il veut jouer
"""

#ZAIZAFOUN Sami
#Groupe 1B, L1 INFORMATIQUE

from Akiba_console import *
from Akiba_tkinter import *

def menu():

    """!
    Fonction menu() permet de choisir le mode de jeu.
    
    Les choix sont:

    1. Pour jouer en mode console.

    2. Pour jouer en interface graphique.

    3. Pour quitter.
    """
    
    print(" 1. Jouer en mode console\n",
          "2. Jouer en interface graphique\n",
          "3. Quitter\n")

    choix= int(input("Choisissez une entrée: "))

    while choix<1 or choix>3:
        choix= int(input("Choisissez une entrée: "))
        
    if choix== 1:
        lancer_jeu()

    elif choix== 2:
        main()

    else:
        exit()
menu()
