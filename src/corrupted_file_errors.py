'''
Created on 19.4.2016

@author: Kalmis
'''

class CorruptedIngredientFileError(Exception):

    def __init__(self, message):
        super(CorruptedIngredientFileError, self).__init__(message)