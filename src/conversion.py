# -*- coding: utf-8 -*-


class Conversion:
    
    def __init__(self):
        
        self.massDict = {'g' : 1, 'kg' : 1000, 'annos' : 250}
        self.volumeDict = {'m3' : 1000, 'l' : 1, 'dl' : 0.1, 'sl' : 0.01, 'ml' : 0.001, 'rkl' : 0.015, 'tl' : 0.005}
        self.notConvertableList = ['kpl']
        
    def convertFromTo(self, amount, unitFrom,unitTo, density):
        
        if unitFrom in self.notConvertableList or unitTo in self.notConvertableList:
            return None
        elif unitFrom in self.massDict.keys() and unitTo in self.massDict.keys():
            return self.convertMassToMass(amount, unitFrom, unitTo)
        elif unitFrom in self.volumeDict.keys() and unitTo in self.volumeDict.keys():
            return self.convertVolumeToVolume(amount, unitFrom, unitTo)
        elif density is not None and unitFrom in self.volumeDict.keys() and unitTo in self.massDict.keys():
            pass
        elif density is not None and unitFrom in self.massDict.keys() and unitTo in self.volumeDict.keys():
            pass
        else:
            return 0
        
    def convertMassToMass(self,amount,unitFrom,unitTo):
        multiplier = self.massDict[unitFrom]/self.massDict[unitTo]
        return amount * multiplier
    
    def convertVolumeToVolume(self,amount,unitFrom,unitTo):
        multiplier = self.volumeDict[unitFrom]/self.volumeDict[unitTo]
        return amount * multiplier
    
    def convertMassToVolume(self,amount,unitFrom,unitTo,density):
        volumeM3 = self.convertMassToMass(amount, unitFrom, 'kg') * density
        return self.convertVolumeToVolume(volumeM3, 'm3', unitTo)
    
    def convertVolumeToMass(self,amount,unitFrom,unitTo,density):
        massKG = self.convertVolumeToVolume(amount, unitFrom, 'm3') * density
        return self.convertMassToMass(massKG, 'massKG', unitTo)