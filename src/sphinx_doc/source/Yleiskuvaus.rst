.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Yleiskuvaus
======================================

Toteutin Älykkään reseptikirjan keskivaikeana. Ohjelmassa on graafinen käyttöliittymä, jossa voi selata tallennettuja reseptejä, raaka-aineita sekä varastossa olevia raaka-aineita. Näitä kaikkia on myös mahdollista muokata, sekä reseptejä on mahdollista luoda ohjelmassa. Käyttäjä voi myös tallentaa tekemänsä muutokset tiedostoihin tai halutessaan ladata tiedostosta alkuperäiset reseptit, raaka-aineet ja/tai varastotilanteen. Älykkään reseptikirjasta tekee sen hakutoiminnot. Reseptikirjalla voi hakea reseptit, joihin löytyy raaka-aineet varastosta tai jotka sisältävät esim. tiettyä raaka-ainetta. 

Projekti täyttää keskivaikean toteutuksen vaatimukset. Lisätoiminnallisuuksien implementoimisen sijaan keskityin koodin hyvään luettavuuteen, kommentointiin sekä koodin automaattiseen dokumentointiin. Oikeastaan 99% koodin metodeista on kommentoitu ja tämän dokumentin lopussa on koodista automaattisesti generoitu dokumentointi. Siitä käy ilmi jokaisen metodin toiminnallisuus. Näiden lisäksi tein myös kattavat yksikkötestit ohjelman tärkeimmille toiminnoille.

Ohjelman vaatimukset:

* Python 3.x versio
* PyQt5

Projektin toiminnallisuudet alla. Suurimmilta osin kuvaus on projektin vaatimuksista, mutta osaa kohtia on muokattu.

* Ohjelman käyttäjällä on jääkaappi ja muut kaapit täynnä ruoan raaka-aineita ja tarkat ajanmukaiset tiedot siitä kuinka paljon mitäkin  ainetta on varastossa. Ohjelman avulla voidaan etsiä vain ne ruokalajit, jotka voidaan valmistaa käymättä kaupassa tai ruokalajit, jotka vaativat N puuttuvaa tai osittain puuttuvaa ainetta.

* Lisäksi voidaan hakea erityisesti reseptit jotka sisältävät tiettyjä aineita. Ruoka-aineisiin voidaan liittää merkintä siitä, että se sisältää jotakin allergisoivaa tekijää. (Esim maito, kerma jne sisältävät laktoosia) Ohjelmalla tulee voida rajoittaa haku niin, että tietyssä haussa vältettäväksi halutut allergeenit jäävät pois.

* Jotkut raaka-aineet voidaan myös rakentaa itse reseptistä kuin ruokalajit. Esim jauhelihapihvin resepti sisältää lihamureketaikinaa jolla taas on oma resepti. Vastaavasti joulutortut tehdään voitaikinasta, joka sekin on itse valmistettavissa. Jos jääkaapissa ei ole voitaikinaa, ohjelman tulee yrittää koota taikina raaka-aineista. (Huomaa että tämä tekee raaka-aineista ja tuotetuista ruoista hyvin samankaltaisia...)

* Lienee itsestään selvää että jotkin aineet kuten munat tai sipulit ovat laskettavissa kappaleittain. Moni raaka-aine kuitenkin mitataan erilaisilla mitoilla. Kaapissa oleva jauho myös ostetaan kiloittain, mutta mitataan resepteissä desilitroissa. Tee ohjelmaasi luokka joka hoitaa kaikki muunnokset mittojen välillä. (vinkki: aineella on tiheys)

* Graafinen käyttöliittymä

* (Komentorivi käyttöliittymä, jossa osa toiminnoista, mutta testaaminen hyvin vähäistä.)

* Ohjelman käyttäjällä on jääkaappi ja muut kaapit täynnä ruoan raaka-aineita. Ohjelmalla voidaan pitää näistä kirjaa.

* Ohjelman avulla voidaan etsiä vain ne ruokalajit, jotka voidaan valmistaa käymättä kaupassa tai ruokalajit, jotka vaativat korkeintaan N puuttuvaa tai osittain puuttuvaa (riittää vain pieneen määrään) ainetta.

* Lisäksi voidaan hakea erityisesti reseptit jotka sisältävät tiettyjä aineita. Vaikkapa kala täytyy käyttää pois.

* Raaka-aineisiin tulee voida liittää merkintä siitä, että kyseinen raaka-aine sisältää jotakin allergisoivaa tekijää. (Esim maito, kerma jne sisältävät laktoosia) Ohjelmalla tulee voida rajoittaa reseptien haku niin, että kyseisessä haussa vältettäväksi halutut allergeenit jäävät pois.

* Jotkut raaka-aineet voidaan myös rakentaa itse reseptistä samoin kuin ruokalajit. Esim jauhelihapihvin resepti sisältää lihamureketaikinaa, jolla taas on oma resepti. Vastaavasti joulutortut tehdään voitaikinasta, joka sekin on itse valmistettavissa. Jos jääkaapissa ei ole valmista voitaikinaa, ohjelman tulee katsoa sen sijaan onko taikinan tekoon tarvittavat raaka-aineet tarjolla.

* Lienee itsestään selvää että jotkin aineet kuten munat tai sipulit ovat laskettavissa kappaleittain. Moni raaka-aine kuitenkin mitataan erilaisilla mitoilla. Kaapissa oleva jauho myös ostetaan kiloittain, mutta mitataan resepteissä desilitroissa. Tee ohjelmaasi luokka joka hoitaa kaikki muunnokset mittojen välillä.

* Raaka-aineet allergiamäärityksineen, ruokareseptit ja jääkaapin sisältö tulee tallentaa sopiviin tiedostoihin tekstimuodossa.

* reseptien interaktiivinen rakentaminen ja muokkaaminen käyttöliittymän kautta