# Fichier pour tester le code. Une sorte de "sandbox" pour notre groupe NSI.
import atelier as Atelier
import equipe as Equipe
import tournoi as Tournoi
import arbre as Arbre

arb = Arbre("E1")
arb.setGauche(Arbre("A1"))
arb.sag.setGauche(Arbre("A2"))
arb.sag.setDroit(Arbre("E2"))

arb.afficher_arbre_infixe()


lst_equipes=[]
lst_ateliers=[]

E1 = Equipe("E1", [])
E2 = Equipe("E2", [])
E3 = Equipe("E3", [])

A1 = Atelier(nom = "A1")
A2 = Atelier(nom = "A2")
A3 = Atelier(nom = "A3")

lst_equipes=[E1, E2, E3]
lst_ateliers=[A1, A2, A3]

for arb in Arbre.generation(lst_equipes, lst_ateliers):
    arb.afficher_arbre_infixe()
    print("----------")

def generation_combinaison(cas:list, n:int)->list:
    """
    Fonction qui crée une liste de listes de toutes les combinaisons possibles

    Paramètres:
        cas - une liste de toutes les possibilités
        n - le nombre de combinaisons à générer
    """
    tab = []
    #première génération de tableau
    for i in range(n):
        ligne = File() #l'enregistrement du tableau
        for c in cas:
            ligne.enfiler(c)
        tab.append(ligne)

    #tri de cas de sorte qu'il ne se répètent pas
    for i in range(1,len(tab)):
        #on compare l'abre précédent avec le prohain
        for j in range(len(tab[i].L)):
            if tab[i].L[j] == tab[i-1].L[j]:
                temp = tab[i].defiler()
                tab[i].enfiler(temp)

    return tab
    
liste = generation_combinaison([1,2,3], 3)

for elt in liste:
    print(elt.L)
