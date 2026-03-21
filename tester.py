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

    dec_file = 0 #décalage de l'enfilement
    for i in range(0,len(tab)):
        for _ in range(dec_file):
            temp = tab[i].defiler()
            tab[i].enfiler(temp)
        dec_file += 1
            
    
    
    return tab

def generation_combinaison_repetition(cas:list, n:int, kelems:int)->list:
    """
    Fonction qui crée une liste de liste de combinaisons de k-uplets possibles
    

    Parameters
    ----------
    cas : list
        une liste de toutes les possibilités
    n : int
        le nombre de combinaisons à générer
    kelems : int
        le nombre des éléments à conserver

    """
    combi = generation_combinaison(cas, n)
    tab = []
    
    for _ in range(len(combi)):
        tab.append([])
        
            
    for i in range(len(tab)):
        for j in range(kelems): #conservation des nombres
            tab[i].append(combi[i].L[j])
            
    return tab
    

    
