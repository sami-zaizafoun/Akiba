"""!
    Ce module s'occupe de l'initialisation du jeu en mode d'interface graphique.
"""

#ZAIZAFOUN Sami
#Groupe 1B, L1 INFORMATIQUE

from tkinter import *
from Akiba_console import *
from math import *
import os

"""!
VARIABLES GLOBALES
"""

t= 0 #Tour joueur
n= 7 #Taille de la grille
cercles=75 #Dimension d'une cercle
x0= 5 #Coordonnées x du point en haut à gauche
y0= 5 #Coordonnées y du point en haut à gauche
x2= 0
y2= 0

dico={"R":"red","B":"white","N":"black"}  #dictionnaire couleurs des boules

"""!
Les fonctions:
"""

def dessineGrille(g):

    """!
    Cette fonction sert à dessiner la grille.
    """
    
    can.delete(ALL)
    for i in range(n+1):
        can.create_line(x0+cercles*i, y0,x0+cercles*i,y0 + n*cercles,fill="black")
        can.create_line(x0, y0+cercles*i,x0+n*cercles ,y0+cercles*i,fill="black")

def creeBoules(g):

    """!
    Cette fonction sert à créer et afficher les boules.
    """
    
    for i in range(n):
        for j in range(n):
            x=g[i][j]
            if x!="*":
                can.create_oval(x0 +cercles*j+10,y0+cercles*i+10,x0 +cercles*(j+1)-10,y0+cercles*(i+1)-10,fill=dico.get(x))

def contour(l, c):

    """!
    Cette fonction sert à dessiner autour d'une boules choisie.

    l --> ligne
    
    c --> colonne
    """
    
    x= g[l][c]
    can.create_oval(x0 +cercles*c+10,y0+cercles*l+10,x0 +cercles*(c+1)-10,y0+cercles*(l+1)-10,outline="blue")    
            
def on_click(event):

    """!
    Cette fonction sert à marquer la boule sur laquelle le joueur a cliqué(selon le tour).
    """
    
    global t,x2,y2
    x=int((event.y-x0)/cercles)
    y=int((event.x-y0)/cercles)
    if t==0:
        x2=x
        y2=y
        if verif_tour(j, x2, y2, g):
            contour(x2,y2)
            t+=1
    else:
        y=y2-y
        x=x2-x
        t=0
        jeu(x2,y2,[-x,-y])

def jeu(l, c, d):

    """!
    Cette fonction sert à defenir les parametre des directions. Ensuite, elle verifie les conditions du jeu.

    Une fois que le tour du joueur est terminé, elle met à jour le nombre des boules dans la grille et le score des joueurs.

    En fin, une fois la condition du gagne est réalisée, le jeu affiche un message en précisant quel joueur a gangné.

    l --> ligne
    
    c --> colonne
    
    d --> diretion
    """
    
    global j, nb_noir, nb_blanc, nb_rouge, point_j1, point_j2

    ############ defenir les parametre des directions ############
    if d==[-1,0]:
        d="h"
    elif d==[1,0]:
        d="b"
    elif d==[0,-1]:
        d="g"
    elif d==[0,1]:
        d="d"

    ############ Verifier les conditions du jeu ############
        
    if verif_tour(j, l, c, g):
        if sortieBoule(j, l, c, d, g):
            mouvements(g, l, c, d)
            nb_noir, nb_blanc, nb_rouge, point_j1, point_j2= score(j,nb_noir, nb_blanc, nb_rouge, point_j1, point_j2, g)
            if j==1:
                j=2
            else:
                j=1
    dessineGrille(g)
    creeBoules(g)
    fin= finJeu(j, nb_noir, nb_blanc, point_j1, point_j2)

    ############ Modifier le nombre des boules dans la grille et le score/ empecher le joueur de changer les parametre manuellement ###############
    num_b.config(state=NORMAL)
    num_b.delete("1.0", END)
    num_b.insert(END, nb_blanc)
    num_b.config(state=DISABLED)

    num_n.config(state=NORMAL)
    num_n.delete("1.0", END)
    num_n.insert(END, nb_noir)
    num_n.config(state=DISABLED)

    num_r.config(state=NORMAL)
    num_r.delete("1.0", END)
    num_r.insert(END, nb_rouge)
    num_r.config(state=DISABLED)

    p1.config(state=NORMAL)
    p1.delete("1.0", END)
    p1.insert(END, point_j1)
    p1.config(state=DISABLED)
    
    p2.config(state=NORMAL)
    p2.delete("1.0", END)
    p2.insert(END, point_j2)
    p2.config(state=DISABLED)

    msg.config(state=NORMAL)
    msg.delete("1.0", END)
    msg.insert(END, "C'est au joueur "+str(j))
    msg.config(state=DISABLED)
    ################################################################################################################################################

    ############ imprimer un message en fonction du gagne ############
    if fin==1:
        msg.config(state=NORMAL)
        msg.delete("1.0", END)
        msg.insert(END, "Partie terminée. Le joueur 1 a gagné la partie.")
        msg.config(state=DISABLED)
    elif fin==2:
        msg.config(state=NORMAL)
        msg.delete("1.0", END)
        msg.insert(END, "Partie terminée. Le joueur 2 a gagné la partie.")
        msg.config(state=DISABLED)
        
def new():
    
    """!
    Cette fonction sert à commencer une nouvelle partie et à remetre les parametre par défaut.
    """
    
    global  g, j,nb_noir, nb_blanc, nb_rouge, point_j1, point_j2
    global num_b, num_n, num_r, p1, p2, msg

    g= [["N","N","*","*","*","B","B"],
    ["N","N","*","R","*","B","B"],
    ["*","*","R","R","R","*","*"],
    ["*","R","R","R","R","R","*"],
    ["*","*","R","R","R","*","*"],
    ["B","B","*","R","*","N","N"],
    ["B","B","*","*","*","N","N"]]

    nb_blanc, nb_noir, nb_rouge= 8, 8, 13
    num_b.config(state=NORMAL)
    num_n.config(state=NORMAL)
    num_r.config(state=NORMAL)
    num_b.delete("1.0", END)
    num_n.delete("1.0", END)
    num_r.delete("1.0", END)
    num_b.insert(END, nb_blanc)
    num_n.insert(END, nb_noir)
    num_r.insert(END, nb_rouge)
    num_b.config(state=DISABLED)
    num_n.config(state=DISABLED)
    num_r.config(state=DISABLED)

    point_j1, point_j2= 0, 0
    p1.config(state=NORMAL)
    p2.config(state=NORMAL)
    p1.delete("1.0", END)
    p2.delete("1.0", END)
    p1.insert(END, point_j1)
    p2.insert(END, point_j2)
    p1.config(state=NORMAL)
    p2.config(state=NORMAL)

    msg.config(state=NORMAL)
    msg.delete("1.0", END)
    msg.insert(END, "C'est au joueur 1")
    msg.config(state=DISABLED)

    ############ Lancer la partie ############
    
    j= initJeu()
    dessineGrille(g)
    creeBoules(g)

def monquitter():
    """!
    Cette fonction sert à fermer la fenêtre.
    """

    dessin.quit()
    dessin.destroy()

"""!          
Les widgets TK
"""

def main():

    """!
    Cette fonction sert à créer la fenêtre principale et à définir tous les boutons et les entrées.
    """
    global num_b, num_n, num_r, p1, p2, msg, can, dessin
    dessin=Tk()
    dessin.title("Jeu d'Akiba. Par: Sami Zaizafoun")
    Label(dessin,text="Jeu d'Akiba",font=("Ubuntu",20,"bold")).pack()

    ############ defenir le Canvas et ces parametres ############
    can= Canvas(dessin,height=532,width=532,bg="brown")
    can.pack(side=LEFT)
    can.bind("<Button-1>", on_click)
    #############################################################

    ############ defenir les bouton "Nouvelle Partie" et "Quitter" ############
    bdem=Button(dessin,text="Nouvelle Partie",command=new,font=("Ubuntu",20,"bold"))
    bdem.pack(side=TOP)

    bq=Button(dessin,text="Quitter",command=monquitter,font=("Ubuntu",20,"bold"))
    bq.pack(side=BOTTOM)
    ###################################################################

    cadre= Frame(dessin, bd=10)
    cadre.pack(fill=BOTH, expand=YES, side=RIGHT)

    Label(cadre, text="",font=("Ubuntu",14,"bold")).grid(row=0, column=0, sticky=W)

    ######################## Creation de l'affichage des scores/ nombre de boules ########################
    Label(cadre, text="Nombre des boules blanches: ",font=("Ubuntu",14,"bold")).grid(row=1, column=0, sticky=W)
    num_b = Text(cadre, height=1, width=1,font=("Ubuntu",14))
    num_b.grid(row=1, column=1)
    num_b.insert(END, nb_blanc)
    num_b.config(state=DISABLED)

    Label(cadre, text="Nombre des boules noires: ",font=("Ubuntu",14,"bold")).grid(row=2, column=0, sticky=W)
    num_n = Text(cadre, height=1, width=1,font=("Ubuntu",14))
    num_n.grid(row=2, column=1)
    num_n.insert(END, nb_noir)
    num_n.config(state=DISABLED)

    Label(cadre, text="Nombre des boules rouges: ",font=("Ubuntu",14,"bold")).grid(row=3, column=0, sticky=W)
    num_r = Text(cadre, height=1, width=2,font=("Ubuntu",14))
    num_r.grid(row=3, column=1)
    num_r.insert(END, nb_rouge)
    num_r.config(state=DISABLED)

    Label(cadre, text="",font=("Ubuntu",14,"bold")).grid(row=4, column=0, sticky=W)

    Label(cadre, text="Boules rouge obtenues par joueur 1: ",font=("Ubuntu",14,"bold")).grid(row=5, column=0, sticky=W)
    p1 = Text(cadre, height=1, width=1,font=("Ubuntu",14))
    p1.grid(row=5, column=1)
    p1.insert(END, point_j1)
    p1.config(state=DISABLED)

    Label(cadre, text="Boules rouge obtenues par joueur 2: ",font=("Ubuntu",14,"bold")).grid(row=6, column=0, sticky=W)
    p2 = Text(cadre, height=1, width=1,font=("Ubuntu",14))
    p2.grid(row=6, column=1)
    p2.insert(END, point_j2)
    p2.config(state=DISABLED)

    Label(cadre, text="").grid(row=7, column=0, sticky=W)

    msg=Text(cadre, height=2, width=30,font=("Ubuntu",20))
    msg.grid(row=8, column=0)
    msg.config(state=DISABLED)
    ########################################################################################################

    dessin.mainloop()
