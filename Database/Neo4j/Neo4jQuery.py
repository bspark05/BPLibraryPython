'''
Created on Jan 13, 2015

@author: Bumsub
'''
from neo4jrestclient.client import GraphDatabase

SERVER_ROOT_URI = 'http://localhost:7474/db/data/'
gdb = GraphDatabase(SERVER_ROOT_URI)

def findAllNodes(attr):
        q_all="MATCH n RETURN n."+attr
        results_all = gdb.query(q=q_all)
        return results_all