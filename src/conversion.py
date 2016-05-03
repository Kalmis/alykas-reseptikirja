# -*- coding: utf-8 -*-

'''
Created on 19.4.2016

@author: Kalmis
'''

class Conversion:
    '''
    Conversion luokka sisältää kaikki ohjelman tuntemat yksiköt sekä niiden "suhdeluvut", jotka mahdollistaa muunnokset.
    Tämän luokan avulla onnistuu yksikkömuunnokset.
    '''
    def __init__(self):
        '''Ohjelman tuntemat yksiköt: massat, tilavuudet sekä yksiköt, joita ei pysty muuttamaan toiseen yksikköön'''
        
        self.massDict = {'g' : 1, 'kg' : 1000, 'annos' : 250}
        self.volumeDict = {'m3' : 1000, 'l' : 1, 'dl' : 0.1, 'sl' : 0.01, 'ml' : 0.001, 'rkl' : 0.015, 'tl' : 0.005}
        self.notConvertableList = ['kpl']
        
    def isValidUnit(self,unit):
        '''
        Tällä metodilla voidaan tarkistaa onko sille parametrina annettu yksikkö ohjelman tuntema
        
        Returns:
            Tunnettu: True
            Ei tunnettu: False
        '''
        if unit in self.massDict.keys() or unit in self.volumeDict.keys() or unit in self.notConvertableList:
            return True
        else:
            return False
        
    def convertFromTo(self, amount, unitFrom,unitTo, density):
        '''
        Tekee yksikkömuunnoksen ja palauttaa muunnetun arvon
        
        Args:
            amount: Muunnettava määrä
            unitFrom: Alkuperäinen yksikkö
            unitTo: Haluttu yksikkö
            density: aineen tiheys, tarvitaan vain kun muunnetaan massa<->tilavuus
        Returns:
            Muunnetun yksikön (int)
        '''
        if unitFrom in self.notConvertableList or unitTo in self.notConvertableList:
            return None
        elif unitFrom in self.massDict.keys() and unitTo in self.massDict.keys():
            return self.__convertMassToMass(amount, unitFrom, unitTo)
        elif unitFrom in self.volumeDict.keys() and unitTo in self.volumeDict.keys():
            return self.__convertVolumeToVolume(amount, unitFrom, unitTo)
        elif density is not None and unitFrom in self.volumeDict.keys() and unitTo in self.massDict.keys():
            pass
        elif density is not None and unitFrom in self.massDict.keys() and unitTo in self.volumeDict.keys():
            pass
        else:
            return 0
        
    def __convertMassToMass(self,amount,unitFrom,unitTo):
        ''' Muuttaa massa yksikön massa yksiköksi, esim. g->kg'''
        multiplier = self.massDict[unitFrom]/self.massDict[unitTo]
        return amount * multiplier
    
    def __convertVolumeToVolume(self,amount,unitFrom,unitTo):
        ''' Muuttaa tilavuus yksikön tilavuus yksiköksi, esim. l -> m3'''
        multiplier = self.volumeDict[unitFrom]/self.volumeDict[unitTo]
        return amount * multiplier
    
    def __convertMassToVolume(self,amount,unitFrom,unitTo,density):
        ''' Muuttaa massa yksikön tilavuus yksiköksi, esim. kg -> l. Hyödyntää kaavaa m = r*v'''
        volumeM3 = self.__convertMassToMass(amount, unitFrom, 'kg') * density
        return self.__convertVolumeToVolume(volumeM3, 'm3', unitTo)
    
    def __convertVolumeToMass(self,amount,unitFrom,unitTo,density):
        ''' Muuttaa tilavuus yksikön massa yksiköksi, esim. l -> kg. Hyödyntää kaavaa v = m / r'''
        massKG = self.__convertVolumeToVolume(amount, unitFrom, 'm3') * density
        return self.__convertMassToMass(massKG, 'massKG', unitTo)