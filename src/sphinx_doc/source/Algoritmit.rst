.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Algoritmit
======================================

Yksikkömuunnokset
###################

Älykäs reseptikirja vaatii algoritmeja yksikkömuunnosten tekemiselle. Yksinkertaisessa tilanteessa on kyse kertoimen muuntamisesta eli massa <-> massa ( g<->kg) tai tilavuus <-> tilavuus. 

Haastavimmissa tilanteissa pitää myös pystyä tehdä muutoksia massa <-> tilavuus. Näissä muunnoksissa ohjelma hyödyntää kaavaa m = v * r, jossa m = massa, v = tilavuus sekä r = aineen tiheys. Jokaisesta aineesta täytyy siis olla tallennettuna tiheys, jotta muunnokset ovat mahdollisia. Tämän lisäksi ohjelmaan on tallennettu lista muista tunnetuista yksiköista ja niiden suhdeluvut.

Erikoistilanteen luo yksiköt, jotka eivät ole muunnettavissa kuten ’kpl’ ja ’tlk’.

Ohjelmassa on omat metodit jokaiselle eri muunnostyypille. Nämä metodit ovat absrahoitu yhden metodin taakse, jolla pystyy tehdä kaikkia muunnoksia. Alla metodeista automaattisesti generoitu dokumentaatio.


.. automodule:: conversion
.. autoclass:: Conversion
	:noindex:
	:members: convertMassToMass, convertVolumeToVolume, convertMassToVolume, convertVolumeToMass, convertFromTo 

Haku
######

Reseptejä voi hakea eri hakuehdoilla. Ohjelmaa tehdessä on oletettu, ettei raaka-aineita, reseptejä tai varastotuotteita tule kovinkaan paljon, joten tehokkaita hakualgoritmejä ei ole tarve tehdä. Kaikki edellä mainitut asiat ovat ohjelmassa tallennettuna listoissa tallennusjärjestyksessä, joten esimerkiksi binäärihaun suoraan hyödyntäminen ei onnistu. Ohjelman haut yksinkertaisesti käyvät listaa läpi alusta loppuun mitään oletuksia tekemättä.

Ohjelman muuttaminen käyttämään ns. binäärihakua ei pitäisi olla hirveän vaikeaa. Tällöin lista pitäisi kuitenkin pitää jollain tapaa aina järjestyksessä, joka tuottaa kuormaa aina kun raaka-aine lisätään tai poistetaan.

Oikeastaan kaikki haut perustuvat nimien (string) vertailuun ja lista, josta etsitään käydään kokonaan tai osittain läpi. Osa algoritmeista laskee vastaavuuksien määrän ja toiset palauttavat vastaavuuden. Yksi haku algoritmeista myös kutsuu rekursiivisesti itseään, koska ”hakulista” saattaa sisältää toisen ”hakulistan.

.. automodule:: search
.. autoclass:: Search
	:noindex:
	:members: searcForhRecipesNIngredientsInStorage, searchFromList, searchIncludesIngredient, searchNoAllergen
