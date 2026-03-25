# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:24:54 2026

@author: kazakov.roman
"""
# importations à faire pour la réalisation d'une interface graphique
import sys
import PyQt5.QtWidgets as QT
import tester


# Première étape : création d'une application Qt avec QApplication
#    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
#    on vérifie s'il existe déjà une instance de QApplication
app = QT.QApplication.instance() 
if not app: # sinon on crée une instance de QApplication
    app = QT.QApplication(sys.argv)
    
root = QT.QWidget()
    

def afficher_tableau(lignes:int, colonnes:int, data):
    # Première étape : création d'une application Qt avec QApplication
    #    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
    #    on vérifie s'il existe déjà une instance de QApplication
    app = QT.QApplication.instance() 
    if not app: # sinon on crée une instance de QApplication
        app = QT.QApplication(sys.argv)
    
    
    root = QT.QWidget()
    
    
    # création d'une fenêtre avec QWidget dont on place la référence dans fen
    tab = QT.QTableWidget(root)
    tab.setGeometry(50, 50, 1000, 1000)
    tab.setRowCount(lignes)
    tab.setColumnCount(colonnes)
    for i in range(len(data)):
        for j in range(len(data[i].L)):
            tab.setItem(i, j, QT.QTableWidgetItem(str(data[i].L[j])))
    
    # la fenêtre est rendue visible
    root.showMaximized()
    
    # exécution de l'application, l'exécution permet de gérer les événements
    sys.exit(app.exec_())
    
def f1():
    layout = QT.QVBoxLayout(root)
    

    btn_confirm = QT.QPushButton(text = "Confirmer")
    nb_equipes = QT.QLineEdit("Entrez le nombre d'équipes...")
    nb_ateliers = QT.QLineEdit("Entrez le nombre d'ateliers...")
    noms_eq = QT.QLineEdit("Précisez les noms des équipes")
    noms_at = QT.QLineEdit("Précisez les noms des ateliers")
    at_doubles = QT.QLineEdit("Entrez les noms des ateliers à double équipe...")

    
    layout.addWidget(nb_equipes)
    layout.addWidget(nb_ateliers)
    layout.addWidget(noms_eq)
    layout.addWidget(noms_at)
    layout.addWidget(at_doubles)
    layout.addWidget(btn_confirm)

    root.showMaximized()

    sys.exit(app.exec_())


def f2():
    layout = QT.QVBoxLayout(root)
    
    btn_confirm = QT.QPushButton(text = "Confirmer2")
    btn_retour = QT.QPushButton(text="Retour")


    layout.addWidget(btn_confirm)
    layout.addWidget(btn_retour)
    root.showMaximized()

    sys.exit(app.exec_())



def f3(lignes, colonnes, data):
    layout = QT.QHBoxLayout(root)
    mi_layout = QT.QVBoxLayout()
    
    btn_confirm = QT.QPushButton(text = "Confirmer3")
    btn_retour = QT.QPushButton(text="Retour")

    
    tab = QT.QTableWidget(root)
    tab.setGeometry(50, 50, 1000, 1000)
    tab.setRowCount(lignes)
    tab.setColumnCount(colonnes)
    for i in range(len(data)):
        for j in range(len(data[i].L)):
            tab.setItem(i, j, QT.QTableWidgetItem(str(data[i].L[j])))

    layout.addWidget(tab)
    layout.addLayout(mi_layout)
    mi_layout.addWidget(btn_confirm)
    mi_layout.addWidget(btn_retour)
    
    root.showMaximized()

    sys.exit(app.exec_())


liste = tester.generation_combinaison([1,2,3], 3)

f1()