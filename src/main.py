# -*- coding: utf-8 -*-

class Main(object):
    
    def __init__(self):
        
        
        
        #TODO: Automaattinen aineiston sisäänluku ja niiden tallentaminen listoihin
        # Testimoodi pois päältä oletuksena. Testimoodissa mm. AskUserInput metodit käyttävät kysymystä syötteenä.
        self.TestMode = False
        
    
    
    def AskUserInputText(self,question):
        
        UserInput = input(question)
        return UserInput    
    
    def AskUserInputInt(self,question):
        
        if self.TestMode:
            UserInput = question
        else:
            UserInput = input(question)
        
        try:
            UserInput = int(UserInput)
            return(UserInput)
        except ValueError:  
            return False
            
            
    def AskUserInputFloat(self,question):
        
        if self.TestMode:
            UserInput = question
        else:
            UserInput = input(question)
        
        try:
            UserInput = float(UserInput)
            return(UserInput)
        except ValueError:  
            return False
              
    
        
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
                UserInput = self.AskUserInputText("Valintasi > ")
                print("\n")
                if UserInput == "1":
                    self.StorageMenu()
                    break;
                elif UserInput == "2":
                    self.IngredientsMenu()
                    break;
                elif UserInput == "3":
                    self.RecipesMenu()
                    break;
                elif UserInput == "4":
                    self.SearchMenu()
                    break;
                elif UserInput == "5":
                    self.SaveMenu()
                    break
                elif UserInput == "6":
                    self.LoadMenu()
                    break
                elif UserInput == "0":
                    return 0
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
                UserInput = self.AskUserInputText("Valintasi > ")
                print("\n")
                if UserInput == "1":
                    print("Lisätietoja")
                    break;
                elif UserInput == "2":
                    print("Varastotilanne")
                    break;
                elif UserInput == "0":
                    return 0 
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
        
            
        