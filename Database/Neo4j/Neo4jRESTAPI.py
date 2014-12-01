'''
Created on Dec 1, 2014

@author: Administrator
'''

import Database.Neo4j.Relationship as relationship
import httplib

SERVER_ROOT_URI = 'http://localhost:7474'

def getServerStatus(self):
    status = 500
    try:
        url = SERVER_ROOT_URI
        
        
        