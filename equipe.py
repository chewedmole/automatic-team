#crée des objets de type équipes possédant un nom et la liste des membres de l'équipe
class Equipe : 
    
    def __init__(self,nom,membres):
        self.nom = nom
        self.membres = membres
        
    def __str__(self):
        return f"Equipe : {self.nom} , {self.membres}"
    
    def get_equipe(self):
        return self.nom, self.membres
    
    def set_nom(self,nom):
        self.nom = nom
    
    def set_membres(self, membres):
        self.membres=membres

