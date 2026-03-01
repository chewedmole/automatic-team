class Arbre:
    """
    Une structure de donnees hierarchique.
    Chaque arbre possede des sous-arbres dont la parité est inferieur de 1.
        cle - noeud d'un arbre
        branches:list - un tableau de branches d'un arbre    
    """
    def __init__ (self, cle):
        self.cle = cle
        self.branches = []

    def ajout_branche(self, br):
        """
        Methode qui permet de rajouter un element/une branche
        Entree:
            br - un element a ajouter 
        """
        self.branches.append(br)

    def getCle(self):
        return self.cle
    
    def setCle(self, cle):
        self.cle = cle
    
    def getBranches(self) -> list:
        return self.branches

    
def generer_arb_possiblites(arb, cas:list):
    """
    Fonction recursive qui cree un arbre de tous les combinaisons de cas possibles.
    On reduit la liste des cas possibles quand nous avons fini de construire une branche
    TODO: resoudre le probleme de generation(la regle d'au-dessus)

    Exemple:
        racine
        |---1
        |     \ 2
        |         \ 3
        |     \ 3   
        |         \ 2
        |---2
        |     \ 1
        |         \ 3
        |     \ 3   
        |         \ 1
        ----3
              \ 1
                  \ 2
              \ 2
                  \ 1
    
    """
    if len(cas) == 1: #le cas d'arret quand nous avons utilise tous les cas possibles
        arb.ajout_branche(Arbre(cas[0]))
    else:
        for i in range(len(cas)):
            if cas[i] not in arb.getBranches():
                arb.ajout_branche(Arbre(cas[i]))
            generer_arb_possiblites(arb.getBranches()[i], cas[1:])

def afficher_arbre(arb):
    """
    Fonction recursive qui permet d'afficher tous le noeuds d'un arbre passe en parametres
    """
    if len(arb.getBranches()) == 0:
        print(arb.getCle())
        print('-----') #separateur des branches pour une meilleure lecture
    else:
        print(arb.getCle())
        for br in arb.getBranches():
            afficher_arbre(br)
        
#Jeu de tests
ARB = Arbre('racine')
generer_arb_possiblites(ARB, [1,2,3])
afficher_arbre(ARB)



    



