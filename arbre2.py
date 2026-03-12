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
'''            
def generation_arbre_combinaison(lst_ateliers:list, lst_equipes:list):
    e = [Arbre(lst_equipes[0].getNom(), []) for i in range(len(lst_equipes))] 
    arbre = Arbre(0, e)

    for i in range(len(arbre.getNiveau())):
        arbre.sous_arbs[i].ajouterSousBranche(Arbre(lst_ateliers[i].getNom(), []))
    return arbre
'''
E1 = Equipe("E1", [])
E2 = Equipe("E2", [])
E3 = Equipe("E3", [])

A1 = Atelier(nom = "A1")
A2 = Atelier(nom = "A2")
A3 = Atelier(nom = "A3")

lst_equipes=[E1, E2, E3]
lst_ateliers=[A1, A2, A3]

print(generation_arbre_combinaison(lst_ateliers,lst_equipes))