#deuxieme type d'arbres
class Arbre:
    def __init__(self, cle, sous_arbs: list):
        self.cle = cle
        self.sous_arbs = sous_arbs

    def ajouterSousBranche(self, branche):
        self.sous_arbs.append(Arbre(branche))

    def getNiveau(self)->list:
        #fonction qui retourne tous les sous-arbres
        return self.sous_arbs
    
    def estFeuille(self)->bool:
        return len(self.sous_arbs) == 0
        

def generation_arbre_combinaison(elems:list, arb):
