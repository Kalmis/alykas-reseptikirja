.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Testaus
======================================

Yleisesti
###########

Ohjelma nojaa hyvin paljon siihen, ettei virheellistä dataa ole mahdollista tallentaa olioihin. Dataa ei siis enää validoida, kun se haetaan oliosta tai muualta. Tämän vuoksi oli hyvin tärkeää testata kunnolla kaikki paljon käytetyt metodit, joilla asetetaan arvoja eri olioille. Myös yksikkömuunnoksien toimivuus on tärkeää, mutta myös testaaminen helppoa yksikkötesteillä.

Suunnitelmissa oli testata kaikki ohjelman luokat yksikkötesteillä, mutta se ei tämän kurssin ja ajan puitteissa ole järkevää. 

Yksikkötestit
################
Tärkeimpien ja eniten käytettyjen metodien toimivuuden varmistamiseksi kirjoitin kattavat yksikötestit. Yksikkömuunnoksista testaan jokaista apumetoda useammalla eri arvoilla. Näiden lisäksi on myös testattu, että apumetodit abstrahoiva metodi toimii halutulla tavalla.

Raaka-aineen attribuuttien asetus metodit ovat myöskin testattu kattavasti. Yksikkötesteillä on varmistettu, ettei vääränlaisia arvoja ole mahdollista asettaa olioille sekä että metodit palauttavat fiksun virheen eivätkä kaada ohjelmaa. Tämän lisäksi on tarkastettu, että metodit hyväksyvät niitä arvoja joita kuuluukin. Samalla on myös varmistettu, että arvojen palautus metodit toimivat.

IngredientContainer sekä resepti oliot ja niiden metodit ovat myöskin testattu hyvin samalla tavalla kuin raaka-aine olion. Koko ohjelma oikeastaan perustuu näiden kolmen luokan eri metodeihin, joten niiden toimivuuden varmistaminen on tärkeää.

Tämän lisäksi yksikkötestein on tarkistettu jokaisen eri tiedostotyypin sisäänluku ja arvojen tallennus olioihin. Testattavia asioita on mm., että tiedoston epäonnistuessa heitetään järkevä virhe eikä ohjelma kaadu.


Manuaalinen testaaminen
############################

Haun testaaminen yksikkötesteillä olisi järkevää, sillä se on myös yksi ohjelman tärkeistä ominaisuuksista. Sen testaaminen yksikkötesteillä on kuitenkin hyvin työlästä, joten päädyin tekemään sen manuaalisesti ohjelmaa käyttäen. Hakua on testattu eri hakusyötteillä sekä hakuvaihtoehdoilla. Hakutuloksien oikeellisuus on pystytty varmistamaan, kun tiedetään mitä dataa ohjelmassa on sisällä. Testidatan koko on verrattain pieni, joten päätteleminen on mahdollista.

Käyttöliittymää ei myöskään ole yksikkötestattu, koska yksikkötesteillä ns. BDD testien tekeminen ei ole kovinkaan helppoa. Käyttöliittymää on testattu käyttämällä sitä. Muutamia testattuja asioita mainitakseni

* Väärien syötteiden antaminen tekstikenttiin, esim. kopioimalla
* Nappuloiden klikkaaminen useita kertoja
* Taulukoiden klikkaaminen useita kertoja
* Painikkeiden, tekstien, taulukoiden ”drag-n-drop”
* Ikkunan venyttäminen
