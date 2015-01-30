'''
Created on Jan 13, 2015

@author: Bumsub
'''
from neo4jrestclient.client import GraphDatabase

SERVER_ROOT_URI = 'http://localhost:7474/db/data/'
gdb = GraphDatabase(SERVER_ROOT_URI)

def findAllNodes():
    q_all="MATCH n RETURN n"
    results_all= gdb.query(q=q_all)
    return results_all

def findAllNodes1(attr):
    q_all="MATCH n RETURN n."+attr
    results_all = gdb.query(q=q_all)
    return results_all
    
def findAllNodes2(attr1, attr2):
    q_all="MATCH n RETURN n."+attr1+", n."+attr2
    results_all = gdb.query(q=q_all)
    return results_all