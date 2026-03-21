# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:24:54 2026

@author: kazakov.roman
"""
# importations à faire pour la réalisation d'une interface graphique
import sys
import PyQt5.QtWidgets as QT
import tester

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
    root.show()
    
    # exécution de l'application, l'exécution permet de gérer les événements
    sys.exit(app.exec_())
    
liste = tester.generation_combinaison([1,2,3,4,5,6], 6)

afficher_tableau(6, 6, liste)
