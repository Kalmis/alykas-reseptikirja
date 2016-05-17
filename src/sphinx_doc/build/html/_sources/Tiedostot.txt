.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tiedostot
======================================

Yleisesti
#############

Ohjelma lukee ja tallentaa tekstitiedostoja. Raaka-aineilla, resepteillä ja varastolistauksella on kaikilla omat tiedostoformaattinsa, jotka ovat ihmisen helposti luettavissa sekä muokattavissa. Projektissa on mukana esimerkkitiedostot ’raaka_aineet.txt’, ’reseptit.txt’ sekä ’varasto.csv’.

Raaka-aineet
##############

Esimerkki ja tietuekuvaus::

	INGREDIENTLIST
	
	#Ingredient
	Date                   : 18.4.2015
	Name                   : Kala
	Density                : 0.5
	Allergen               : Kala
	Recipe			: Jauheliha pizza

	
	#Ingredient
	Date                   : 18.4.2015
	Name                   : Maito
	Density                : 1.0
	Allergen               : Laktoosi
	Allergen		 : Maito	

Ekan rivin alussa oltava INGREDIENTLIST, muuten tiedostoa ei lueta.

#Ingredient kertoo uuden raaka-aineen alkamisesta, ei maksimimäärää.

Tiedot kerrotaan yleensä [attribuutti] : [arvo] sekä joillain attribuuteilla on useampia arvoja, kuin 1, nekin ovat erotettu kaksoispisteellä.

Pakolliset attribuutit

Date: Raaka-aineen luontipäivä, oltava muodossa dd.mm.yyyy

Name: Raaka-aineen nimi, oltava yli kaksi merkkiä pitkä

Tiheys: Aineen tiheys (float)

Vapaaehtoiset attribuutit:

Allergen: Allergeeni tekstinä, voi olla useita

Recipe: Resepti


Reseptit
#########

Esimerkki ja tietuekuvaus::

	RECIPELIST

    	#Recipe 
	Date : 18.4.2016 
	Name : Jauheliha pizza 
	Time : 40 
	Outcome : 2.0 : annos 
	Ingredient : Jauheliha : 600.0 : g 
	Ingredient : Pizzataikina : 300.0 : g 
	Ingredient : Juusto : 0.1 : kg 
	Ingredient : Oregano : 5.0 : g 
	Ingredient : Tomaattimurska : 300.0 : g 
	Instruction : Ruskista jauheliha 
	Instruction : Kaada kaikki sekoitettuna uuniin 
	Instruction : Nauti kylman PepsiColan kanssa.
	
Ensimmäisen rivin alussa oltava RECIPELIST, muuten tiedostoa ei tunnisteta.

#Recipe kertoo uuden reseptin alkamisesta. Tiedostossa voi olla useita reseptejä.

Tiedot kerrotaan yleensä [attribuutti] : [arvo] sekä joillain attribuuteilla on useampia arvoja, kuin 1, nekin ovat erotettu kaksoispisteellä.

Pakolliset attribuutit:

Date: reseptin luontipäivä, oltava muodossa dd.mm.yyyy

Name: reseptin nimi, oltava yli 2 merkkiä pitkä

Time: Kauanko reseptin tekemiseen menee minuuteissa, kokonaisluku

Outcome: reseptin lopputuloksen määrä (float) ja yksikkö

Ingredient: raaka-aineen nimi, määrä (float) ja yksikkö. Raaka-aineiden maksimimäärää ei määritelty.

Instruction: Ohje, ohjeet tulee reseptille tässä järjestyksessä. 

Varastotilanne
#################

Csv-tiedosto, jossa soluerottimena puolipiste eikä tekstin ympärillä ”” merkkejä.
Esimerkki ja tietuekuvaus::

	STORAGELIST
	Kala;800.0;g
	Maito;35.0;l
	Vehnajauho;2.0;kg
	Pizzataikina;350.0;g
	Jauheliha;2.0;kg
	Tomaattimurska;400.0;g
	Juusto;3.0;kg
	Oregano;5.0;kg

Ensimmäisellä rivilla oltava STORAGELIST tai tiedostoa ei lueta. 

Rivin ensimmäisessä solussa raaka-aineen nimi

Rivin toisessa solussa määrä (float) desimaalipilkulla tai pisteellä

Rivin kolmannessa solussa määrän yksikkö
