.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Arvio lopputuloksesta
======================================

Kokonaisuudessaan olen tyytyväinen projektin lopputulokseen. Paljon mieleen tulleita ominaisuuksia jäi toteuttamatta, mutta kuten todettu tämä oli myös tietoinen valinta. Halusin, että palautuksen koittaessa projekti on hyvin tehty sekä dokumentoitu eikä niin, että siinä on paljon toiminnallisuuksia, mutta ne ovat tehty huonosti. 

Eniten parannettavaa on mielestäni omissa työskentelytavoissani. Liian useat ominaisuudet tuli tehtyä yhteen tai kahteen kertaan, koska en ollut tyytyväinen toteutukseeni tai keksin paremman tavan. Tulevaisuudessa pyrin myöskin tekemään yhden osion kerralla kuntoon ja sitten jatkaa seuraavaan. Jokaisen osion välissä pitäisi myöskin malttaa suunnitella toiminallisuuden impelementaatio kunnolla ja miettiä mm. toteutuksen skaalautuvuutta. 

Ohjelman oleellisen puute lienee se, että raaka-aineiden reseptejä on hieman hankala tarkastella. Haku ottaa huomioon raaka-aineiden reseptit ja näin ollen palauttaa reseptejä, joihin ei suoraan ole raaka-aineita. Näkymä ei kuitenkaan indikoi mitenkään, että mikä raaka-aine puuttuu ja pitää tehdä reseptistä, vaan se jää käyttäjän vastuulle. Muut puutteet on kerrottu tämän dokumentin kohdassa 9. Ohjelman puutteet.

Ohjelman parantamiseksi refaktoroisin IO luokan lähes kokonaan ja parantaisin sen virheenkäsittelyä sekä virheen heittämistä. Muut parannukset koskisivat pääasiassa toiminnallisuuksia, kuten:
* raaka-aineen lisäys ja poisto
* varastotuotteen lisäys ja poisto
* Tallennettavien tai ladattavien tiedostojen polkujen valitseminen käyttöliittymältä
* Reseptin katsominen helpommaksi hakunäkymällä

Paremmin projektissa olisi mielestäni voinut tehdä tietorakenteiden valinnan. Kuten kohdassa 5. Tietorakenteet totesin, niin listoilla tietokannan luominen ei ole järin hyvä vaihtoehto. Parempi vaihtoehto olisi ollut esim SQLite3 kirjaston käyttö. Ohjelma on muilta osin mielestäni hyvin skaalautuva ja uusien toiminnallisuuksien lisääminen käyttäen olemassa olevia metodeja pitäisi olla verrattain yksinkertaista - osittain kattavan dokumentaation takia. Oikean tietokannan puuttuminen kuitenkin heikentää ohjelman skaalautuvuutta merkittävästi. Projekti on myös todella kattavasti dokumentoitu, joten myöhemmin projektin jatkaminen pitäisi olla verrattain helppoa.