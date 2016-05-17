.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ohjelman puutteet
======================================

* Raaka-ainetta tai reseptiä tallennettaessa ei tarkasteta onko samalla nimellä jo olemassa olio. Tämä joissain tilanteissa aiheuttaa hieman outoja hakutuloksia. Ratkaisu: Pitäisi tarkastaa onko samannimistä oliota jo olemassa.

* Raaka-aineen reseptin tarkasteleminen ei ole kovinkaan yksinkertaista käyttöliittymällä. Esim. raaka-ainetta kaksoisklikkaamalla voisi aueta raaka-aineen resepti

* Hakunäkymällä resepteistä ei saa kovinkaan paljoa irti, vaan pitää siirtyä reseptit näkymälle. Haku näkymältä pitäisi saada resepti kokonaisuudessaan helposti auki.

* Raaka-aineelta ei voi poistaa reseptiä

* Raaka-aineelta ei voi poistaa kaikkia allergeenejä

* Haku kyllä tarkistaa voiko raaka-aineen tehdä reseptistä, jos sitä ei ole tarpeeksi varastossa. Haku ei kuitenkaan skaalaa määriä eli jos tarvitaan 500g pizzataikinaa, mutta pizzataikinan ohjeesta saadaan 1kg, niin silloin tarkastetaan riittääkö ainekset 1kg tekemiseen eikä 500g. Tämän korjaamiseksi howManyIngredientsFOundInStorage metodissa pitäisi laskea suhdeluku raaka-aineen määrän ja raaka-aineen reseptin lopputuloksen välillä, jota voitaisiin hyödyntää vertailussa. Tätä toimintoa varten ohjelmassa on myös oletus, että annos = 250g, jotta reseptien lopputulosta voi todella verrata tarvittaviin määriin.