'''
Created on Dec 1, 2014

@author: Administrator
'''

OUT = 'out'
IN = 'in'
BOTH = 'both'
type1 = ''
direction = ''

def __init__(self, type1='', direction=''):
    self.type = type1
    self.direction = direction        
        
def toJsonCollection(self):
    sb = ''
    sb+='{ '
    sb+=' \"type\" : \"'+ type1 + '\"'
    if direction != None :
        sb+=', \"direction\" : \"'+ direction + '\"'
    sb+=' }'
    return sb

    