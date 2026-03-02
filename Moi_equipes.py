liste_equipe = []#créer une liste contenant toutes les équipes
liste_test = []#juste pou

#fonction qui permet de demander à l'utilisateur quelles 
#équipes il veut ajouter
def ajouter_equipe(nom,membres):
        liste = []
        liste.append(str(nom))
        liste.append(membres)
        liste_equipe.append(liste)

#crée des objets de type équipes possédant un nom et la liste des membres de l'équipe
class Equipe : 
    
    def __init__(self,nom,membres):
        self.nom = nom
        self.membres = membres
        
    def __str__(self):
        return f"Equipe : {self.nom} , {self.membres}"

#fonction qui parcours la liste d'équipe une fois terminée et qui crée des objets pour chaque éléments à l'intéreur et les ajoutent à une nouvelle liste
def creer_equipes():
    for i in range(len(liste_equipe)) : 
        liste_equipe[i][0] = Equipe(nom=liste_equipe[i][0],membres = liste_equipe[i][1])
        liste_test.append(liste_equipe[i][0])
        
    