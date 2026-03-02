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

#jeu de tests
arb = Arbre("E1")
arb.setGauche(Arbre("A1"))
arb.sag.setGauche(Arbre("A2"))
arb.sag.setDroit(Arbre("E2"))

arb.afficher_arbre_infixe()