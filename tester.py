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
