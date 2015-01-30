'''
Created on Nov 28, 2014

@author: Administrator
'''

import Web.APIs.Foursquare.FoursquareAPI as fsAPI
import Web.APIs.Foursquare.FsURL as fsURL
import Web.APIs.Foursquare.FsToken as fstoken
import Database.Neo4j.Neo4jRESTAPI as neo4j
import Process as process
import Database.Neo4j.Neo4jQuery as query
from neo4jrestclient.client import GraphDatabase



SERVER_ROOT_URI = 'http://localhost:7474/db/data/'
gdb = GraphDatabase(SERVER_ROOT_URI)
    
    
if __name__ == '__main__':
    url = "https://api.foursquare.com/v2/venues/4a8b60c7f964a5204d0c20e3/nextvenues?client_id=S3TCARJS00I452G1FSIPZZ0LDOKWX5MBCJ3V1SYPKS2V4Z2I&client_secret=JBJBBXH1RN4D105TFW0O4YEEUAJ2PCKOF5PZEYSBXARLGGZJ&v=20141006"
    venues = fsAPI.venues_NextVenues(url)
    
    fromList = process.iteration(1, venues)
    print(len(fromList))
    


        
    token = fstoken.tokenReady("tokenList.xls", "Sheet1")
    
    for i in range(len(fromList)):
        tokenSet = token[i%len(token)]
        url1 = fsURL.makeURL_venues_nextVenues(fromList[i][0], tokenSet)
        venues1 = fsAPI.venues_NextVenues(url1)
        
        nodeAttribute1 = process.setAttributes(fromList[i])
        starNode = neo4j.createUniqueNode("Id", fromList[i][0], nodeAttribute1)
        
        
        for j in venues1 :
            nodeAttribute2 = process.setAttributes(j)
            endNode = neo4j.createUniqueNode("Id", j[0], nodeAttribute2)
            relationId = fromList[i][0]+"_to_"+j[0]
            relation = neo4j.addUniqueRelationship("Id", relationId, starNode, endNode, None)
    
    
# insert a field for isLast
    results_all1= query.findAllNodes('id')
    
    for nodes in results_all1:
        node = nodes[0]
        q_isLast1 = "MATCH (n{id:'"+node+"'}) SET n.isLast = 1 RETURN n.name, n.isLast"
        results_isLast1 = gdb.query(q=q_isLast1)    
    
    for k in fromList:
        id_fromList=k[0]
        q_isLast2="MATCH (k {id:'"+id_fromList+"'}) SET k.isLast = 0 RETURN k.name, k.isLast"
        results_isLast2 = gdb.query(q=q_isLast2)
        print(results_isLast2[0])


# insert a field for no. of relationships
    results_all = query.findAllNodes('id')
    
    for nodes in results_all:
        node = nodes[0]
        q_node = "MATCH (n{id:'"+node+"'})<--(x) RETURN count(n)"
        results_node = gdb.query(q=q_node)
    
        q_write = "MATCH (n{id:'"+node+"'}) SET n.RelCount="+str(results_node[0][0])+" RETURN n.name"
        results_write = gdb.query(q=q_write)
        print([results_node[0][0],results_write[0][0]])
    
# convert to shp file
    
    