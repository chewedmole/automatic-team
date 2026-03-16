#import des classes tournoi et atelier 
#methodes Equipes : get_equipes, set_nom, set_memebres
#methodes Atelier : set_nom, set_nb_equipe, get_nom, get_nb_equipe
import atelier 
import equipe



#création de la classe tournoi
class Tournoi :
    
    def __init__(self):
        self.liste_atelier = []
        self.liste_equipes = []
    #fonction qui permet de créer des objets Equipes et de les ajouter à la liste des equipes du tournoi   
    def creer_equipes(self):
        for i in range(len(equipes)) : 
            equipes[i][0] = equipe.Equipe(nom=equipes[i][0],membres = equipes[i][1])
            self.liste_equipes.append(equipes[i][0])
    
    #affiche les listes misent en argument
    def __str__(self):
        return f"Equipe : {self.liste_equipes}"

    #ajoute la liste des ateliers disponibles pour le tournoi
    def ajouter_atelier():
        pass
    
    def get_list_equipes(self):
        return self.liste_equipes
    
    def set_liste_equipes(self,new_liste):
        self.liste_equipes = new_liste
    
    def get_liste_ateliers(self): 
        return self.liste_atelier
    
    def set_liste_ateliers(self,new_liste):
        self.liste_atelier = new_liste
    
    
equipes=[]
 #fonction qui permet de saisir les equipes avant de les transformer en objets       
def ajouter_equipe(nom,membres):
    liste = []
    liste.append(str(nom))
    liste.append(str(membres))
    equipes.append(liste)        

st.title('Coucou')