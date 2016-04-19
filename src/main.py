# -*- coding: utf-8 -*-

class Main():
    
    def __init__(self):
        
        print("Käynnistetään ohjelma. Ehkäpä autom sisäänluku ym. tässä?")
        
        
    def MainMenu(self):
        
        
        while 1:
            print("1. Varastotilanne")
            print("2. Raaka-aineet")
            print("3. Reseptit")
            print("4. Haku")
            print("0. Sulje ohjelma")
            
            # Pyydetään käyttäjältä inputtia, kunnes saadaan validi vastaus. 
            # TÄmän jälkeen break, jotta tulostetaan menu uudelleen
            while 1:
                valinta = int(input("Valintasi > "))
                if valinta == 1:
                    self.StorageMenu()
                    break;
                elif valinta == 2:
                    self.IngredientsMenu()
                    break;
                elif valinta == 3:
                    self.RecipesMenu()
                    break;
                elif valinta == 4:
                    self.SearchMenu()
                    break;
                elif valinta == 0:
                    return(0)
                else:
                    print("Virheellinen valinta.")    
                
        
        
    def StorageMenu(self):
        print("STorageMenu")
        
    def IngredientsMenu(self):
        print("IngredientsMenu")
        
    def RecipesMenu(self):
        print("RecipesMenu")
        
    def SearchMenu(self):
        print("SearchMenu")    
        
            
program = Main()
program.MainMenu()
print("Ohjelma sammuu")
exit()
        