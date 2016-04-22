'''
Created on 19.4.2016

@author: Kalmis
'''

class CorruptedIngredientsFileError(Exception):

    def __init__(self, message):
        super(CorruptedIngredientsFileError, self).__init__(message)
        
class CorruptedRecipesFileError(Exception):

    def __init__(self, message):
        super(CorruptedRecipesFileError, self).__init__(message)
        
class CorruptedStorageFileError(Exception):

    def __init__(self, message):
        super(CorruptedStorageFileError, self).__init__(message)