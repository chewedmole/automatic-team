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
        

def generation_arbre_combinaison(elems):
    e=[Arbre(elems[0], []) for i in range(len(elems))]
    arbre=Arbre(None, e)
    for j in range(1, len(elems)):
        for i in range(len(arbre.getNiveau())):
            arbre.sous_arbs[i].aujouterSousBranche(Arbre(elems[j], []))
    return arbre