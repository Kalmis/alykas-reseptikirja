# -*- coding: utf-8 -*-

class Main(object):
    
    def __init__(self):
        

        #TODO: Automaattinen aineiston sisäänluku ja niiden tallentaminen listoihin
        # Testimoodi pois päältä oletuksena. Testimoodissa mm. AskUserInput metodit käyttävät kysymystä syötteenä.
        self.TestMode = False
        self.MainMenuTitles = ["1. Varastotilanne", "2. Raaka-aineet", "3. Reseptit","4. Haku","5. Tallenna", "6. Lataa", "0. Sulje ohjelma"]
        self.StorageMenuTitles = ["1. Kerro lisätietoja raaka-aineesta", "2. Näytä varastotilanne", "0. Takaisin"]
        self.IngredientsMenuTitles = ["1. Kerro lisätietoja raaka-aineesta", "2. Listaa raaka-aineet", "0. Takaisin"]
        self.RecipesMenuTitles = ["1. Kerro lisätietoja reseptistä", "2. Listaa reseptit", "0. Takaisin"]
        self.SearchMenuTitles = ["1. Kerro lisätietoja reseptistä", "2. Reseptit, joissa raaka-aine esiintyy", "3. Sopii allergikolle", "4. Reseptit, joihin varastotarvikkeet riittävät", "5. Reseptit, joista puuttuu N-määrä raaka-aineita varastosta", "6. Reseptit, joista löytyy N-määrä raaka-aineita varastosta", "0. Takaisin"]
        self.SaveMenuTitles =  ["1. Tallenna kaikki", "2. Tallenna reseptit", "3. Tallenna raaka-aineet", "4. Tallenna varasto", "0. Takaisin"]
        self.LoadMenuTitles =  ["1. Lataa kaikki", "2. Lataa reseptit", "3. Lataa raaka-aineet", "4. Lataa varasto", "0. Takaisin"]

            
    
    def RunMenu(self, MenuTitles):
        
        for i in MenuTitles:
            print(i)
        while True:
            UserInput = self.AskUserInputInt("Valintasi > ")
            if UserInput >= 0 and UserInput < len(MenuTitles):
                return UserInput
            else:
                print("Virheellinen valinta")

    def AskUserInputText(self,question):
        
        UserInput = input(question)
        return UserInput    
    
    def AskUserInputInt(self,question):
       
        # Testimoodissa käytetään argumenttia syötteenä.
        if self.TestMode:
            UserInput = question
        else:
            UserInput = input(question) 
        while True:
            try:
                UserInput = int(UserInput)
                return(UserInput)
            except ValueError:  
                print("Syöte ei kokonaisluku")
            UserInput = input(question) 
            
    def AskUserInputFloat(self,question):
        # Testimoodissa käytetään argumenttia syötteenä.
        if self.TestMode:
            UserInput = question
        else:
            UserInput = input(question)
        
        while True:
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
            elif UserChoice == 0:
                return 0 

    def StorageMenu(self):
        
        while True:
            UserChoice = self.RunMenu(self.StorageMenuTitles)
            if UserChoice == 1:
                print("Lisätietoja")
            elif UserChoice == 2:
                print("Varastotilanne")
            elif UserChoice == 0:
                return 0 
        
    def IngredientsMenu(self):
        while True:
            UserChoice = self.RunMenu(self.IngredientsMenuTitles)
            if UserChoice == 1:
                print("Lisätietoja")
            elif UserChoice == 2:
                print("Lista raaka-aineista")
            elif UserChoice == 0:
                return 0   
        
    def RecipesMenu(self):
        
        while 1:
            UserChoice = self.RunMenu(self.RecipesMenuTitles)
            if UserChoice == 1:
                print("Lisätietoja")
            elif UserChoice == 2:
                print("Lista resepteistä")
            elif UserChoice == 0:
                return 0   
        
    def SearchMenu(self):
        
        while 1:
            UserChoice = self.RunMenu(self.SearchMenuTitles)
            if UserChoice == 1:
                print("Lisätietoja")
            elif UserChoice == 2:
                print("reseptejä")
            elif UserChoice == 3:
                print("allergikko")
            elif UserChoice == 4:
                print("reseptejä")
            elif UserChoice == 5:
                print("Reseptejä")
            elif UserChoice == 6:
                print("Reseptejä")
            elif UserChoice == 0:
                return 0   
        
    def SaveMenu(self):  
              
        while 1:
            UserChoice = self.RunMenu(self.SaveMenuTitles)
            if UserChoice == 1:
                print("kaikki")
            elif UserChoice == 2:
                print("reseptit")
            elif UserChoice == 3:
                print("raaka-aineet")
            elif UserChoice == 4:
                print("varasto")
            elif UserChoice == 0:
                return 0 

    def LoadMenu(self):
        while 1:
            UserChoice = self.RunMenu(self.LoadMenuTitles)
            if UserChoice == 1:
                print("kaikki")
            elif UserChoice == 2:
                print("reseptit")
            elif UserChoice == 3:
                print("raaka-aineet")
            elif UserChoice == 4:
                print("varasto")
            elif UserChoice == 0:
                return 0 
        
if __name__ == "__main__":
    program = Main()
    program.MainMenu()
    print("Exit")
                   
        