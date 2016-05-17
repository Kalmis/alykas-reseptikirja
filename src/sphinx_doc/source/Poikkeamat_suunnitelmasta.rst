.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Poikkeamat suunnitelmasta
======================================

Poikkesin suunnitelmastani muutamassakin kohtaa. Päädyin lopulta tekemään graafisen käyttöliittymän komentorivi käyttöliittymän sijaan. Tämä oli mielestäni todella hyvä ratkaisu, koska nyt tajuaa, ettei GUI:n tekeminen ole mitenkään erityisen vaikeaa. Toisaalta huomasin myös, että uusien ominaisuuksien toteuttaminen oli jopa helpompaa graafisesti, esim. tietojen syöttäminen. En koskaan ollut tehnyt GUI:ta, joten tämän opettelu vei paljon enemmän aikaa, kun olin käyttöliittymän koodaamiseen suunnitellut käyttäväni. 

Toinen pieni muutos liittyy luokkajakoihin. Alkuperäisestä suunnitelmasta poiketen jaoin Ingredient luokan kahteen osaan: Ingredient ja IngredientContainer. Näin vältytään tiedon turhalta kopioimiselta ja säilyttämiseltä useampaan kuin yhteen kertaan. Tämän muutoksen tekeminen ei kauaa vienyt.

Toteutusjärjestys oli myös aivan toisenlainen kuin alunperin suunnittelin sen olevan. Tähän päätökseen päädyin jo projektin demotilaisuudessa, jossa assari suositteli tekemään aluksi toimivan ohjelman vähillä toiminnoilla ja sen jälkeen kasvattaa ohjelmaa. Alkuperäinen suunnitelmani oli tehdä kaikki osiot erikseen valmiiksi ja lopuksi integroida ne. Uskon, että käytetyllä suunnitelmalla säästin aikaa.