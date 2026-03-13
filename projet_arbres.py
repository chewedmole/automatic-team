# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 10:22:57 2026

@author: cariou.manon
"""
import arbre as Arbre

def creation_arbres(lst_eq, lst_act):
    """
    fonction qui creer les arbres puis les ajoute dans une liste liste_arbres
    ----------
    lst_eq : list
        liste des equipes
    lst_act : list
        liste des activites
    """
    liste_arbres = []

    #INIT des arbres
    for eq in lst_eq:
        liste_arbres.append(Arbre(eq.nom))


def generation(lst_eq, lst_act,liste_arbres,liste_arbres_fixe, n):
    """
    fonction qui genere les arbres de facon recursive
    ----------
    lst_eq : list
        liste des equipes
    lst_act : list
        liste des activites
    liste_arbres : list
        liste des arbres
    n : int
        n est une variable qui prend la valeur de la longueur de la list_act et qui est decrementee de 1 a chaque appel recursif 

    """
    if n==0:
        return liste_arbres_fixe
    
    for act in lst_act:
        nb_equipes_act = act.nb_equipe
        X = 0
        lst_arbs_mm_act = [] #variable temporelle pour garder les equipes dans les memes activites
        i=0
        arbre=liste_arbres[i]
        arbre_fixe=liste_arbres_fixe[i]
        #ajout des activites dans les arbres
        while X!=nb_equipes_act :
            if arbre.sag is None:
                if act not in arbre_fixe.cle.get_liste_act : # verifier si 
                    
                    arbre.sag = Arbre(act.get_nom())
                    X += 1
                    lst_arbs_mm_act.append(arbre)
                    
                    #On rajoute le equipes a droite pour les memes activites
                    if X != 1 and X==nb_equipes_act:
                        for arb in lst_arbs_mm_act:
                            arbre.sad = arb.getCle()
                
                #Une vérification d'ajout d'une activité, le cas dans lequel il n'y a pas assez d'equipes
                if i > len(liste_arbres):
                    if nb_feuille(liste_arbres) == 0:
                        if X != nb_equipes_act:
                            Y = nb_equipes_act - X
                            return "Il manque au moins" + str(Y) + "équipe(s)" + "ou, supprimez une activité demandant" + str(Y) + "groupe(s)"
            i+=1
    liste_sous_arbres=[]
    for j in range(len(liste_arbres)) :
        liste_sous_arbres.append(arb.sag)
        gauche=liste_arbres_fixe[j]
        while gauche.sag is not None :
            gauche=gauche.sag
        gauche.sag=liste_sous_arbres[j]
        
    return generation(lst_eq, lst_act,liste_sous_arbres,liste_arbres_fixe, n-1)


generation(lst_eq, lst_act, liste_arbres, liste_arbres_fixe, n)