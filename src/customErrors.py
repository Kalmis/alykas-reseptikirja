# -*- coding: utf-8 -*-

'''
Created on 19.4.2016

@author: Kimi Päivärinta
'''

class CorruptedFileError(Exception):
    '''Korruptoituneen tiedoston exception'''
    pass
    

class SetAttributeError(Exception):
    ''' Käytetään, kun olion attribuutin asettamisessa tapahtuu virhe'''
    pass