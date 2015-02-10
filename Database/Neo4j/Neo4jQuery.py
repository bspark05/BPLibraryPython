'''
Created on Jan 13, 2015

@author: Bumsub
'''
from neo4jrestclient.client import GraphDatabase
import Variables as var

gdb = GraphDatabase(var.SERVER_ROOT_URI)

def setAttributesNode(venue):
    attribute = ""
    attribute+= "{ id : '"+str(venue[0])+"', "
    attribute+= "name : \""+str(venue[1])+"\", "
    attribute+= "category : \""+str(venue[2])+"\", "
    attribute+= "lat : "+str(venue[3])+", "
    attribute+= "lng : "+str(venue[4])+", "
    attribute+= "checkins : "+str(venue[5])+", "
    attribute+= "users : "+str(venue[6])+" }"
    #print(attribute)
    return attribute;

def createUniqueNode2(label, attribute):
    q_node = "MERGE (n:"+label+" "+attribute+") RETURN n"
    result = gdb.query(q=q_node)
    #print(result[0])
    return result[0]

def createUniqueNode1(attribute):
    q_node = "MERGE (n "+attribute+") RETURN n"
    result = gdb.query(q=q_node)
    #print(result[0])
    return result[0]

def setAttributesRel(startNode, endNode):
    attribute = ""
    attribute+= "{ fromLng : "+str(startNode['data']['lng'])+", "
    attribute+= "fromLat : "+str(startNode['data']['lat'])+", "
    attribute+= "fromId : '"+startNode['data']['id']+"', "
    attribute+= "fromName : \""+startNode['data']['name']+"\", "
    attribute+= "fromCate : \""+startNode['data']['category']+"\", "
    attribute+= "fromCheckins : "+str(startNode['data']['checkins'])+", "
    attribute+= "fromUsers : "+str(startNode['data']['users'])+", "
    
    attribute+= "toLng : "+str(endNode['data']['lng'])+", "
    attribute+= "toLat : "+str(endNode['data']['lat'])+", "
    attribute+= "toId : '"+endNode['data']['id']+"', "
    attribute+= "toName : \""+endNode['data']['name']+"\", "
    attribute+= "toCate : \""+endNode['data']['category']+"\", "
    attribute+= "toCheckins : "+str(endNode['data']['checkins'])+", "
    attribute+= "toUsers : "+str(endNode['data']['users'])+" }"
    
    return attribute

def addUniqueRelationship(startNode, endNode, attribute):
    q_rel = "MATCH ( from { id : '"+startNode['data']['id']+"' } ), ( to { id : '"+endNode['data']['id']+"' } )"
    q_rel+= "CREATE UNIQUE (from)-[r:NEXT"
    q_rel+= attribute
    q_rel+= "]->(to)"
    q_rel+= "RETURN r"
    result = gdb.query(q=q_rel)
    #print(result[0])
    return result[0]
    

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

def findAllRelationships():
    q_all="MATCH ((n)-[r]-()) RETURN r"
    results_all = gdb.query(q=q_all)
    return results_all

def findAllOutRelationships1(attr):
    q_all="MATCH ((n)-[r]-() RETURN r."+attr
    results_all = gdb.query(q=q_all)
    return results_all
