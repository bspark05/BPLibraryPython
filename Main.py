'''
Created on Nov 28, 2014

@author: Administrator
'''

import Web.APIs.Foursquare.FoursquareAPI as fsAPI
import Web.APIs.Foursquare.FsURL as fsURL
import Web.APIs.Foursquare.FsToken as fstoken
import Database.Neo4j.Neo4jRESTAPI as neo4j
import Process as process


if __name__ == '__main__':
    url = "https://api.foursquare.com/v2/venues/4a8b60c7f964a5204d0c20e3/nextvenues?client_id=S3TCARJS00I452G1FSIPZZ0LDOKWX5MBCJ3V1SYPKS2V4Z2I&client_secret=JBJBBXH1RN4D105TFW0O4YEEUAJ2PCKOF5PZEYSBXARLGGZJ&v=20141006"
    venues = fsAPI.venues_NextVenues(url)
    
    fromList = process.iteration(1, venues)
    
    token = fstoken.tokenReady("tokenList.xls", "Sheet1")
    
    for i in range(len(fromList)):
        tokenSet = token[i%len(token)]
        url1 = fsURL.makeURL_venues_nextVenues(fromList[i][0], tokenSet)
        venues1 = fsAPI.venues_NextVenues(url1)
        
        nodeAttribute1 = process.setAttributes(fromList[i],1)
        starNode = neo4j.createUniqueNode("Id", fromList[i][0], nodeAttribute1)
        
        
        for j in venues1 :
            nodeAttribute2 = process.setAttributes(j,0)
            endNode = neo4j.createUniqueNode("Id", j[0], nodeAttribute2)
            relationId = fromList[i][0]+"_to_"+j[0]
            relation = neo4j.addUniqueRelationship("Id", relationId, starNode, endNode, None)

'''
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

if __name__ == '__main__':
    SERVER_ROOT_URI = 'http://localhost:7474/db/data/'
    gdb = GraphDatabase(SERVER_ROOT_URI)
    
    q_all="MATCH n RETURN n.id"
    results = gdb.query(q=q_all)
    print(len(results))
    
    for nodes in results:
        #print(nodes[0])
        node = nodes[0]
    
        q_node = "MATCH (n{id:'"+node+"'})<--(x) RETURN count(n)"
        results_node = gdb.query(q=q_node)
        print(results_node[0][0])
    
        q_write = "MATCH (n{id:'"+node+"'}) SET n.RelCount="+str(results_node[0][0])+" RETURN n.name"
        results_write = gdb.query(q=q_write)
        #print(results_write[0][0])
'''