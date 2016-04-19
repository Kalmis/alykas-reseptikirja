# -*- coding: utf-8 -*-





class Main(object):
    
    def __init__(self):
        
        
        
        #TODO: Automaattinen aineiston sisäänluku ja niiden tallentaminen listoihin
        # Testimoodi pois päältä oletuksena. Testimoodissa mm. AskUserInput metodit käyttävät kysymystä syötteenä.
        self.TestMode = False
        self.MainMenuTitles = ["1. Varastotilanne", "2. Raaka-aineet", "3. Reseptit","4. Haku","5. Tallenna", "6. Lataa", "0. Sulje ohjelma"]
    
    def RunMenu(self, MenuTitles):
        
        for i in MenuTitles:
            print(i)
        while True:
            UserInput = self.AskUserInputInt("Valintasi > ")
            if UserInput >= 0 and UserInput <= len(MenuTitles):
                return UserInput
            else:
                print("Virheellinen valinta")

    
    def AskUserInputText(self,question):
        
        UserInput = input(question)
        return UserInput    
    
    def AskUserInputInt(self,question):
       
       
        if self.TestMode:
            UserInput = question
        else:
            UserInput = input(question) 
            
        while True:
            # Testimoodissa käytetään argumenttia syötteenä.
            
            try:
                UserInput = int(UserInput)
                return(UserInput)
            except ValueError:  
                print("Syöte ei kokonaisluku")
            UserInput = input(question) 
            
    def AskUserInputFloat(self,question):
        
        if self.TestMode:
            UserInput = question
        else:
            UserInput = input(question)
        
        while True:
            # Testimoodissa käytetään argumenttia syötteenä.
            
            
            try:
                UserInput = float(UserInput)
                return(UserInput)
            except ValueError:  
                print("Syöte ei desimaaliluku")
            UserInput = input(question)
              
    def MainMenu(self):
        
        while True:
            UserChoice = self.RunMenu(self.MainMenuTitles)
            
            if UserChoice == 1:
                self.StorageMenu()
            elif UserChoice == 2:
                self.IngredientsMenu()
            elif UserChoice == 3:
                self.RecipesMenu()
            elif UserChoice == 4:
                self.SearchMenu()
            elif UserChoice == 5:
                self.SaveMenu()
            elif UserChoice == 6:
                self.LoadMenu()
            elif UserChoice == 7:
                return 0 

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
        
        while 1:
            print("1. Kerro lisätietoja raaka-aineesta")
            print("2. Listaa raaka-aineet")
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
                    print("Lista raaka-aineista")
                    break;
                elif UserInput == "0":
                    return 0 
                else:
                    print("Virheellinen valinta.")   
        
    def RecipesMenu(self):
        print("RecipesMenu")
        
        while 1:
            print("1. Kerro lisätietoja reseptistä")
            print("2. Listaa reseptit")
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
                    print("Lista resepteistä")
                    break;
                elif UserInput == "0":
                    return 0 
                else:
                    print("Virheellinen valinta.")   
        
    def SearchMenu(self):
        print("SearchMenu")   
        
        while 1:
            print("1. Kerro lisätietoja reseptistä")
            print("2. Reseptit, joissa raaka-aine esiintyy")
            print("3. Sopii allergikolle")
            print("4. Reseptit, joihin varastotarvikkeet riittävät")
            print("5. Reseptit, joista puuttuu N-määrä raaka-aineita varastosta")
            print("6. Reseptit, joista löytyy N-määrä raaka-aineita varastosta")
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
                    print("reseptejä")
                    break;
                elif UserInput == "3":
                    print("allergikko")
                    break;
                elif UserInput == "4":
                    print("reseptejä")
                    break;
                elif UserInput == "5":
                    print("Reseptejä")
                    break;
                elif UserInput == "6":
                    print("Reseptejä")
                    break;
                elif UserInput == "0":
                    return 0 
                else:
                    print("Virheellinen valinta.")    
        
    def SaveMenu(self):
        print("SaveMenu")
        
        while 1:
            print("1. Tallenna kaikki")
            print("2. Tallenna reseptit")
            print("3. Tallenna raaka-aineet")
            print("4. Tallenna varasto")
            print("0. Takaisin")
            
            # Pyydetään käyttäjältä inputtia, kunnes saadaan validi vastaus. 
            # TÄmän jälkeen break, jotta tulostetaan menu uudelleen
            while 1:
                UserInput = self.AskUserInputText("Valintasi > ")
                print("\n")
                if UserInput == "1":
                    print("kaikki")
                    break;
                elif UserInput == "2":
                    print("reseptit")
                    break;
                elif UserInput == "3":
                    print("raaka-aineet")
                    break;
                elif UserInput == "4":
                    print("varasto")
                    break;
                elif UserInput == "0":
                    return 0 
                else:
                    print("Virheellinen valinta.")
    
    def LoadMenu(self):
        print("LoadMenu")        
        
        while 1:
            print("1. Lataa kaikki")
            print("2. Lataa reseptit")
            print("3. Lataa raaka-aineet")
            print("4. Lataa varasto")
            print("0. Takaisin")
            
            # Pyydetään käyttäjältä inputtia, kunnes saadaan validi vastaus. 
            # TÄmän jälkeen break, jotta tulostetaan menu uudelleen
            while 1:
                UserInput = self.AskUserInputText("Valintasi > ")
                print("\n")
                if UserInput == "1":
                    print("kaikki")
                    break;
                elif UserInput == "2":
                    print("reseptit")
                    break;
                elif UserInput == "3":
                    print("raaka-aineet")
                    break;
                elif UserInput == "4":
                    print("varasto")
                    break;
                elif UserInput == "0":
                    return 0 
                else:
                    print("Virheellinen valinta.")
        
if __name__ == "__main__":
    program = Main()
    program.MainMenu()
                   
        