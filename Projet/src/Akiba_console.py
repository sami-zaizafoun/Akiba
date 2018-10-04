"""!
    Ce module s'occupe de l'initialisation du jeu en mode console.
"""

#ZAIZAFOUN Sami
#Groupe 1B, L1 INFORMATIQUE


"""!
VARIABLES GLOBALES
"""

g= [["N","N","*","*","*","B","B"],
    ["N","N","*","R","*","B","B"],
    ["*","*","R","R","R","*","*"],
    ["*","R","R","R","R","R","*"],
    ["*","*","R","R","R","*","*"],
    ["B","B","*","R","*","N","N"],
    ["B","B","*","*","*","N","N"]]

nb_noir= 8  #Nombre des boules noirs
nb_blanc= 8  #Nombre des boules blanches
nb_rouge= 13  #Nombre des boules rouges
point_j1= 0  #Score du joueur 2
point_j2= 0  #Score du joueur 2

"""!
Valeurs de la colonne pour le déplacement
"""
colonne= ["   ", "0", "1", "2", "3", "4", "5", "6"]


"""!
Les fonctions:
"""

def creeGrille():
    
    """!
    Fonction qui sert à créer la grille.
    """
    
    res=[0]*7
    for i in range(7):
        res[i]= ["*"]*7            
    return res
    print (res[i]," ",end="\n")
   
            
def affichage(g):

    """!
    Fonction d'affichage qui sert à afficher le tour de joueur, les scores et la grille 
    """
    
    ########### Affichage des nombres de boules/score ###########
    
    print("\nBoules blanches:",nb_blanc)
    print("Boules noires:",nb_noir)
    print("Boules rouges:",nb_rouge,"\n")
    
    print("\nJoueur 1 a",point_j1,"boule(s) rouge")
    print("Joueur 2 a",point_j2,"boule(s) rouge")

    #############################################################
    
    print()

    ########### Affichage de la grille et bar de colonne ###########
    
    for i in colonne:
        print(i, end="  ")
    print()
    print("   -----------------------  ")
    for i, line in enumerate(g):
        print(i,"| ", "  ".join(line), " |",i)
    print("   -----------------------  ")
    for i in colonne:
        print(i, end="  ")
    print("\n")
    
    ################################################################

def verif_tour(j, l, c, g):

    """!
    Cette fonction sert à verifier si le joueur joue ces boules et pas ceux de l'adversaire.

    j --> joueur (1 ou 2)
    
    l --> ligne choisi par le joueur(0-->6)
    
    c --> colonne choisi par le joueur(0-->6)
    
    g --> la grille,
    """

        ########### Definir que le joueur 1 est "B" et joueur 2 est "N" ###########
    ########### verifier si le joueur joue bien ces boules(return vrai si bon) ###########
    if j==1 : 
        p="B"
    else : 
        p="N"
    if g[l][c]!=p:
        print("\n","C'est le tour du joueur ", str(j), "\n")
        return False
    return True

def verif_choix(l, c, d):

    """!
    Cette fonction sert à verifier si le joueur rentre des cordonnées valide.
    
     l --> ligne choisi par le joueur(0-->6)
     
     c --> colonne choisi par le joueur(0-->6)
     
     d --> direction choisi par le joueur(h, b, d, g)
    """
    
    orient= ["h","H","b","B","d","D","g","G"]
    if (l<0 or l>6) or (c<0 or c>6) or d not in orient:
        print("\n","Choisissez une entrez valide\n")
        return False
    return True
        
def choix_boule(g, j):
    
    """!
    Cette fonction sert à saisir les cordonées et verifier si les entrées sont valides.
    """
    
    print("Joueur ", str(j),"\n")
    l= int(input("Choisissez une ligne (0-->6): "))
    c= int(input("Choisissez une colonne (0-->6): "))
    d= input("Choisissez une direction(Haut: h, Bas: b, Droite: d , Gauche: g): ")
    ver_choix= verif_choix(l, c, d)
    if ver_choix:
        ver_tour= verif_tour(j, l, c, g)
        if ver_tour:
            if sortieBoule(j, l, c, d, g):
                mouvements(g, l, c, d)
            else:
                choix_boule(g, j)
        else:
            choix_boule(g, j)
    else:
        choix_boule(g, j)
        
def mouvements(g, l, c, d):

    """!
    Cette fonction sert à appeler la fonction qui correspond a la direction choisie.

    j --> joueur (1 ou 2)
    
    l --> ligne choisi par le joueur(0-->6)
    
    c --> colonne choisi par le joueur(0-->6)
    
    g --> la grille,
    """    
    if d == "h":
        g=haut(g, l, c, d)
    if d == "b":
        g=bas(g, l, c, d)
    if d == "g":
        g=gauche(g, l, c, d)
    if d == "d":
        g=droite(g, l, c, d)


def sortieBoule(j, l, c, d, g):

    """!
    Cette fonction sert à verifier les boules qui sortent de la grille et à empêcher le joueur de sortir ses propres boules.

    x0, y1 ---> cordonnees (haut, bas , gauche, droite)
    """
    
    verif= [l,c]
    if d=="h":
        x0=-1
        y1=0
    elif d=="b":
        x0=1
        y1=0
    elif d=="g":
        x0=0
        y1=-1
    elif d=="d":
        x0=0
        y1=1
	
    while 1:
        if verif[0] not in range(7):
            verif[0]-=x0
            verif[1]-=y1
            break
        elif verif[1] not in range(7):
            verif[0]-=x0
            verif[1]-=y1
            break
        elif g[verif[0]][verif[1]]=="*":
            return True
        else:
            verif[0]+=x0
            verif[1]+=y1
    if verif_tour(j, verif[0], verif[1], g):
        print("\n","Choisissez une entrez valide\n")
        return False
    return True

def score(j, nb_noir, nb_blanc, nb_rouge, point_j1, point_j2, g):

    """!
    Cette fonction sert à compter le nombre des boules restantent dans la grille.
    """
    
    rouge = 0
    blanc= 0
    noir= 0
    for i in g:
        for k in i:
            if k=="R":
                rouge+=1
            elif k=="B":
                blanc+= 1
            elif k=="N":
                noir+= 1
                
    nb_blanc= blanc
    nb_noir= noir    
    if rouge!= nb_rouge:
        if j==1:
            point_j1+=1
            print(point_j1)
        elif j==2:
            point_j2+=1
            
        nb_rouge-=1
        
    elif blanc!= nb_blanc:
        nb_blanc-=1

    elif noir!= nb_noir:
        nb_noir-=1
        
    return nb_noir, nb_blanc, nb_rouge, point_j1, point_j2

#### Defenir les fonction de mouvements:

def haut(g, l, c, d):
    
    """!
    Cette fonction permet le mouvement vers le haut.

    l --> ligne choisi par le joueur(0-->6).
    
    c --> colonne choisi par le joueur(0-->6).
    
    d --> direction choisi par le joueur(h, b, d, g).
    
    g --> la grille
    """
    
    l_o= l ##ligne d'origine
    if l== 6:
        while l!=0 and g[l][c]!= "*":
            l-= 1
        l_n= l ##nouvelle ligne
        
        for i in range(l_n, l_o):
            g[i][c]= g[i+1][c]
        g[l_o][c]= "*"
    elif g[l+1][c]== "*":
        while l!= 0 and g[l][c]!= "*":
            l-= 1
        l_n= l
        
        for i in range(l_n, l_o):
            g[i][c]= g[i+1][c]
        g[l_o][c]= "*"
    return g
    
def bas(g, l, c, d):

    """!
    Cette fonction permet le mouvement vers le bas.

    l --> ligne choisi par le joueur(0-->6).
    
    c --> colonne choisi par le joueur(0-->6).
    
    d --> direction choisi par le joueur(h, b, d, g).
    
    g --> la grille
    """
    
    l_o= l ##ligne d'origine
    if l== 0:
        while l!=6 and g[l][c]!= "*":
            l+= 1
        l_n= l ##nouvelle ligne
        
        for i in range(l_n, l_o,-1):
            g[i][c]= g[i-1][c]
        g[l_o][c]= "*"
        
    elif g[l-1][c]== "*":
        while l!= 6 and g[l][c]!= "*":
            l+= 1
        l_n= l
        
        for i in range(l_n, l_o,-1):
            g[i][c]= g[i-1][c]
        g[l_o][c]= "*"
    return g
    
def gauche(g, l, c, d):

    """!
    Cette fonction permet le mouvement vers la gauche.

    l --> ligne choisi par le joueur(0-->6).
    
    c --> colonne choisi par le joueur(0-->6).
    
    d --> direction choisi par le joueur(h, b, d, g).
    
    g --> la grille
    """
    
    c_o= c ##colonne d'origine
    if c== 6:
        while c!=0 and g[l][c]!= "*":
            c-= 1
        c_n= c ##nouvelle ligne
        
        for i in range(c_n, c_o):
            g[l][i]= g[l][i+1]
        g[l][c_o]= "*"
    elif g[l][c+1]== "*":
        while c!= 0 and g[l][c]!= "*":
            c-= 1
        c_n= c
        
        for i in range(c_n, c_o):
            g[l][i]= g[l][i+1]
        g[l][c_o]= "*"
    return g
    
def droite(g, l, c, d):

    """!
    Cette fonction permet le mouvement vers la droite.

    l --> ligne choisi par le joueur(0-->6).
    
    c --> colonne choisi par le joueur(0-->6).
    
    d --> direction choisi par le joueur(h, b, d, g).
    
    g --> la grille
    """
    
    c_o= c ##colonne d'origine
    if c== 0:
        while c!=6 and g[l][c]!= "*":
            c+= 1
        c_n= c ##nouvelle ligne
        
        for i in range(c_n, c_o, -1):
            g[l][i]= g[l][i-1]
        g[l][c_o]= "*"
    elif g[l][c-1]== "*":
        while c!= 6 and g[l][c]!= "*":
            c+= 1
        c_n= c
        
        for i in range(c_n, c_o, -1):
            g[l][i]= g[l][i-1]
        g[l][c_o]= "*"
    return g

##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################

def finJeu(j, nb_noir, nb_blanc, point_j1, point_j2):

    """!
    Cette fonction permet la mise en place des régles de fin de jeu.
    """
    
    if nb_noir== 0 or point_j1== 6:
        return 1
    
    elif nb_blanc== 0 or point_j2== 6:
        return 2
    
    else:
        return 0

def initJeu():

    """!
    Cette fonction permet de créer la grille et defenir le premier joueur.
    """
    
    creeGrille()
    j=1
    return j

def lancer_jeu():

    """!
    Cette fonction est la fonction principale pour lancer le jeu.

    Elle sert à arreter le jeu quand les regles de fin sont réalisées et aussi à change le joueur à la fin de chaque tour.
    """
    
    global nb_noir, nb_blanc, nb_rouge, point_j1, point_j2
    j= initJeu()
    point_j1, point_j2= 0, 0
    affichage(g)
    x=0
    while x==0:
        choix_boule(g, j)
        nb_noir, nb_blanc, nb_rouge, point_j1, point_j2= score(j,nb_noir, nb_blanc, nb_rouge, point_j1, point_j2, g)
        fin= finJeu(j, nb_noir, nb_blanc, point_j1, point_j2)
        affichage(g)

        ########### arreter le jeu quand les regles de fin sont réalisées ###########
        
        if fin is 1:
            print("Joueur 1 a gagné")
            break
        if fin is 2:
            print("Joueur 2 a gagné")
            break
        
        ########### changement de joueur a chaque tour ###########
        if j==1:
            j=2
        else:
            j=1
