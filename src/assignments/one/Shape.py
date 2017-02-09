'''
Created on 7 feb. 2017

@author: Sophia
'''

class Shape(object):
    '''
    classdocs
    '''
    
    x = 0;
    y = 0;

    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        
    def area(self):
        return self.x * self.y;
    
    @staticmethod
    def isStatic():
        return True;