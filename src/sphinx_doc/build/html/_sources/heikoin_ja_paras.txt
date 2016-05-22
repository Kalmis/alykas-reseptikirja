.. Recipebook documentation master file, created by
   sphinx-quickstart on Tue May  3 01:21:28 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Heikoimmat ja parhaat kohdas
======================================

Parhaina kohtina pidän koodin virheenkäsittelyä, yksikkötestien kattavuutta sekä koodin helppolukuisuutta. Käyttöliittymää on myöskin testattu paljon, enkä ole millään toiminnolla tai syötteellä saanut ohjelmaa kaatumaan tai näyttämään vääriä tietoja.

Ohjelman heikoin kohta on IO luokka. Sisäänlukujen koodi ei ole kovin lukijaystävällistä sekä se on toisteista. Metodeita olisi helppo jakaa pienempiin osiin, joita voisi hyödyntää kaikissa tiedostonluku metodeissa. Myöskin osa sisäänluvun virheistä tulostetaan konsoliin eikä niitä näytetä ollenkaan käyttöliittymällä. Myöskään virhellisiä syötteitä tiedostoissa ei ole testattu tarpeeksi ja uskon, että nimenomaan siinä on ohjelman heikoin kohta. 
