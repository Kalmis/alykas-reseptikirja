.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ohjelman rakenne
======================================

Yleiskatsaus ja UML-kaavio
################################

Ohjelman rakenne on nähtävissä alla olevasta UML-kaaviosta. Kaaviossa ei ole luokkien kaikkia metodeja tai attribuutteja, vaan muutama, jotta käy paremmin ilmi mitä niiltä odotetaan.

Käyttöliittymä on tehty PyQt kirjastoa ja QT designeria hyödyntäen. Käyttöliittymän ulkoasu on Qt designerin generoimaa koodia, jossa painikkeet ja taulut laitetaan oikeille paikoille. Pääikkunan design on luokka nimelta Ui_MainWindow, jonka ohjelman pääluokka MainGUI perii.

MainGUI luokassa määritellään mitä metodia kutsutaan, kun käyttöliittymässä esim. painetaan painiketta. Myös nämä kutsuttavat metodit ovat MainGUI luokassa ja sisältävät pääosin taulujen ja kenttien populoimista sekä niistä tietojen lukemista. 

MainGUI luokassa myös säilytetään listaa kaikista raaka-aine, resepti ja varastotuote (ingredientContainer) olioista. Oikeastaan kaikki käyttöliittymään liittymättömät toiminnallisuudet toteutetaan hyödyntäen eri luokkien kuten Search ym. metodeja. 

Toteutettu rakenne on hyvin toimiva, mutta muutamien metodien suhteen herää kysymys, että mihin luokkaan niiden tulisi kuulua. Esimerkiksi joitain aika yleisiä apumetodeja olisi voinut laittaa uuteen omaan luokkaan.

Yleiskuvaus luokista ja niiden tärkeimmistä metodeista on generoitu automaattisesti koodista alla olevan kuvan alapuolelle.

.. image:: alykas_reseptikirja.png

MainGUI
###########
MainGUI luokasta on vaikea valita mitään erityisen tärkeitä metodeja, mutta kuvauksessa on selitetty mitä minkäkin niminen metodi yleensä tekee sekä jokaisesta on yksi esimerkki. Jokainen metodi on myös kommentoitu, joten halutessaan tämän dokumentin lopusta voi katsoa mitä metodeja luokka sisältää ja mitä ne tekevät.

.. automodule:: mainGUI
.. autoclass:: MainGUI
	:noindex:
	:members: addNewRecipeIngredient, deleteRecipeIngredient, getRecipesInDataListForTable, initButtons, loadFromFileToList, populateIngredientsTable, populateIngredientsEditFields, saveIngredientsEdit

Recipe
##########
.. automodule:: recipe
.. autoclass:: Recipe
	:noindex:
	:members: addIngredientContainer, deleteIngredient, getAllergensDistinctGUI, getIngredients, getName, setName, setTime 

Ingredient 
####################################

.. automodule:: ingredient
.. autoclass:: Ingredient
	:noindex:
	:members: getAllergens, setName, getDensityGUI, removeAllergens, removeRecipe, setRecipe, loadRecipe

IngredientContainer
######################
.. automodule:: ingredient
.. autoclass:: IngredientContainer
	:noindex:
	:members: getQuantityStr, getAllergensStr, hasRecipe, setIngredient

IO
######

.. automodule:: IO
.. autoclass:: IO
	:noindex:
	:members:

Search
##########

.. automodule:: search
.. autoclass:: Search
	:noindex:
	:members: searcForhRecipesNIngredientsInStorage, searchFromList, searchIncludesIngredient, searchNoAllergen

Conversion
#############

.. automodule:: conversion
.. autoclass:: Conversion
	:noindex:
	:members: 

CustomErrors
###################
.. automodule:: customErrors
	:noindex:
	:members:

