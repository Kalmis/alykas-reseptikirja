'''
Created on 27.4.2016

@author: Kalmis
'''
# -*- coding: utf-8 -*-

from main import Main
from mainGUI import MainGUI

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, 
    QInputDialog, QApplication)

if __name__ == '__main__':
    userInput = input("Valitse käytettävä UI \n 1. Komentorivi \n 2. GUI\n Valintasi > ") 
    while True:
            try:
                userInput = int(userInput)
            except ValueError:  
                print("Syöte ei kokonaisluku")
            if userInput == 1:
                CUI = Main()
                CUI.mainMenu()
                exit()
            elif userInput == 2:
                app = QApplication(sys.argv)
                program = MainGUI()
                program.show()
                sys.exit(app.exec_())  
            else:
                userInput = input("Valitse käytettävä UI \n 1. Komentorivi \n 2. GUI") 