# -*- coding: utf-8 -*-

class Main:
    
    def __init__(self):
        
        print("Käynnistetään ohjelma. Ehkäpä autom sisäänluku ym. tässä?")
        
        
    def MainMenu(self):
        
        
        while 1:
            print("1. Varastotilanne")
            print("2. Raaka-aineet")
            print("3. Reseptit")
            print("4. Haku")
            print("5. Tallenna")
            print("6. Lataa")
            print("0. Sulje ohjelma")
            
            # Pyydetään käyttäjältä inputtia, kunnes saadaan validi vastaus. 
            # TÄmän jälkeen break, jotta tulostetaan menu uudelleen
            while 1:
                valinta = input("Valintasi > ")
                print("\n")
                if valinta == "1":
                    self.StorageMenu()
                    break;
                elif valinta == "2":
                    self.IngredientsMenu()
                    break;
                elif valinta == "3":
                    self.RecipesMenu()
                    break;
                elif valinta == "4":
                    self.SearchMenu()
                    break;
                elif valinta == "5":
                    self.SaveMenu()
                    break
                elif valinta == "6":
                    self.LoadMenu()
                    break
                elif valinta == "0":
                    return(0)
                else:
                    print("Virheellinen valinta.")    
                
        
        
        
        
    def StorageMenu(self):
        while 1:
            print("1. Kerro lisätietoja raaka-aineesta")
            print("2. Näytä varastotilanne")
            print("0. Takaisin")
            
            # Pyydetään käyttäjältä inputtia, kunnes saadaan validi vastaus. 
            # TÄmän jälkeen break, jotta tulostetaan menu uudelleen
            while 1:
                valinta = input("Valintasi > ")
                print("\n")
                if valinta == "1":
                    print("Lisätietoja")
                    break;
                elif valinta == "2":
                    print("Varastotilanne")
                    break;
                elif valinta == "0":
                    return(0)
                else:
                    print("Virheellinen valinta.")   
        
    def IngredientsMenu(self):
        print("IngredientsMenu")
        
    def RecipesMenu(self):
        print("RecipesMenu")
        
    def SearchMenu(self):
        print("SearchMenu")    
        
    def SaveMenu(self):
        print("SaveMenu")
    
    def LoadMenu(self):
        print("LoadMenu")        
        
            
program = Main()
program.MainMenu()
print("Ohjelma sammuu")
exit()
        