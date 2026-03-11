class Arbre:
    """
    Une structure de donnees hierarchique.
    Chaque arbre possede des sous-arbres dont la parité est inferieur de 1.
        cle - noeud d'un arbre
        sag - sous-arbre gauche
        sad - sous-arbre droit(utilise pour marquer un equipe dans un atelier a double equipe)
    """
    def __init__ (self, cle):
        self.cle = cle
        self.sag = None
        self.sad = None

    def setGauche(self, sag):
         self.sag = sag

    def setDroit(self, sad):
        self.sad = sad

    def getBranches(self) -> tuple:
        return (self.sag, self.sad)

    def getCle(self):
        return self.cle
    
    def setCle(self, cle):
        self.cle = cle

    def estFeuille(self):
        if self.getBranches()[0] is None and self.getBranches()[1] is None:
            return True
        else:
            return False

    def afficher_arbre_infixe(self):
        """
        Fonction recursive qui permet d'afficher tous le noeuds d'un arbre passe en parametres en utilisant le parcours en profondeur infixe
        """
        if self is not None:
            if self.sag is not None:
                self.sag.afficher_arbre_infixe()
            print(self.getCle())
            if self.sad is not None:
                self.sad.afficher_arbre_infixe()

def generation(lst_eq, lst_act):
    liste_arbres = []

    #INIT des arbres
    for eq in lst_eq:
        liste_arbres.append(Arbre(eq.nom))


    for _ in range(len(lst_act)):
        for act in lst_act:
            nb_equipes_act = act.nb_equipe
            X = 0
            lst_arbs_mm_act = [] #variable temporelle pour garder les equipes dans les memes activites
            for arbre in liste_arbres:
                if arbre.sag is None:
                    arbre.sag = Arbre(act.get_nom())
                    X += 1
                    lst_arbs_mm_act.append(arbre)
                    #On rajoute le equipes a droite pour les memes activites
                    if X != 1 and X==nb_equipes_act:
                        for arb in lst_arbs_mm_act:
                            arbre.sad = arb.getCle()
    return liste_arbres
    '''
    Une vérification d'ajout d'une activité
    Le cas dans lequel il n'y a pas assez d'equipes

    if nb_feuille(liste_arbre) == 0:
        if X != Nb_eq_act:
            Y = Nb_eq_act - X
            return "Il manque au moins" + str(Y) + "équipe(s)" + "ou, supprimez une activité demandant" + str(Y) + "groupe(s)"
    '''
                    

#jeu de tests-----------------------------------------------


