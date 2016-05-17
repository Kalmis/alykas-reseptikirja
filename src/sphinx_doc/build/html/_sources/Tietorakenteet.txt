.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tietorakenteet
======================================

Raaka-aineista tehdään jokaisesta oma olio, jossa on raaka-aineen perustiedot kuten nimi, tiheys, allergeenit ym. Useissa resepteissä esiintyy samat raaka-aineet, mutta ei ole kovin mielekästä monistaa samaa pohja dataa useisiin olioihin. Tämän vuoksi ohjelmassa on ns. ”ingredientContainer” olio, jossa on viittaus perus raaka-aineolioon sekä erikseen määritelty määrä sekä määrän yksikkö. Näin Jauhelihan tietoja ei tarvitse tallentaa useaan olioon, ainoastaan viittaus Jauhelihan olioon. 

Olioita (reseptit, raaka-aineet sekä ingredientContainer) säilytetään yksinkertaisesti listassa. Pythonin lista on muuttuvatilainen rakenteinen. Jos ohjelmaa kehittäisi eteenpäin, niin yksi ominaisuus olisi reseptin tai raaka-aineen poistaminen. Olioita pitää siis olla mahdollista poistaa myös listan keskeltä, joten muuttuvatilainen rakenne on parempi.

Massa- sekä tilavuusyksiköt ovat ohjelmassa tallennettuna sanakirjaan. Sanakirja on tähän sopiva valinta, koska yksiköistä ei riitä ainoastaan nimi, vaan täytyy tietää myös jonkinlainen suhdeluku muihin yksikköihin verrattuna ja tämän suhdeluvun pitää löytyä nimenomaan yksikön nimellä.

Jo ohjelmaa suunnitellessa tiesin, ettei ”tietokannan” luominen listoilla ole kovin järkevää, mutta kurssin alueen puitteissa päädyin tähän ratkaisuun. Fiksumpi vaihtoehto olisi ollut esimerkiksi käyttää Pythonin SQLite3 kirjastoa. Näin data olisi ollut tallennettuna tiedostoihin. Tämä olisi myös tehnyt ohjelmasta paljon helpommin skaalattavan, koska datan hakeminen tietokannasta olisi jo perustunut SQL kyselyihin ja siirtyminen käyttämään oikeaa tietokantapalvelinta olisi ollut verrattain helppoa. Myöhemmin dokumentissa puhutaan myös hakualgoritmeista ja niiden tehokkuudesta. Oikean tietokannan käyttäminen helpottaisi myös paljon hakujen tekemistä ja niiden tehokkuudesta huolehtiminen siirtyisi tietokannan puolelle, joka on suunniteltu tehokkuus ja haut mielessä. 

.. automodule:: ingredient
	:members:
	:noindex:
	

.. automodule:: recipe
	:members:
	:noindex:
