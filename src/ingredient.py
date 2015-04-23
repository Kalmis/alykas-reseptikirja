from recipe import Recipe

KG = 0
G = 1


class Ingredient():
    
    '''
    Asetetaan oliota luodessa kaikki paikalleen.
    
    '''
    
    def __init__(self, name, quantity, unit, recipe, allergen):
        
        self.name = name            #String
        self.quantity = quantity    #Int
        self.unit = unit            #Int
        self.allergen = allergen    #String list
        '''
        Raaka-aineet luetaan ennen kuin reseptit on luettu, joten ei pysty heti
        m��ritt�m��n oliota. Jos recipe ei ole None, niin otetaan nimi talteen sek� 
        laitetaan olioviittauksen puuttuminen merkkaamalla recipe_loaded = False
        '''
        
        if recipe != None:
            self.recipe = recipe    
            self.recipe_loaded = False
        else:
            self.recipe = None
            self.recipe_loaded = None
            
            
    def load_recipe(self,recipe_list):
        '''
        Jos ja kun False, niin resepti olisi, mutta ei ladattu.
        Etsit��n Resepti olio listasta raaka-aine olioon talletettua
        nime� totteleva olio ja asetetaan se reseptiksi.
        '''
        if(self.recipe_loaded == False):
            while i in recipe_list:
                if i.return_name == self.recipe:
                    self.recipe = i
                    self.recipe_loaded = True
                    return True
            # Resepti� kyseisell� nimell� ei l�ytynyt.
            return False
        else:
            return None # Ei ladattavaa
                
            
    '''
    Seuraavaksi m��ritelty yleisi� mahdollisesti tarvittavia funktioita
    '''        
            
    def return_name(self):
        return self.name
    def change_name(self,name):
        self.name = name
                
    def change_quantity(self,quantity):
        if quantity >= 0:
            self.quantity = quantity
        
    def change_unit(self,unit):
        self.unit = unit
        
    def set_recipe(self,recipe):
        self.recipe = recipe
        self.recipe_loaded = True
    
    def remove_recipe(self):
        self.recipe = None
        self.recipe_loaded = None
    
    def set_allergens(self,allergens):
        self.allergen = allergens
        
    def add_allergens(self,allergens):
        self.allergen.append(allergens)