'''
Created on Nov 28, 2014

@author: Administrator
'''

import FoursquareAPI as fsAPI
import FsURL as fsURL
import FsToken as fstoken
import Neo4jRESTAPI as neo4j
import Process as process

if __name__ == '__main__':
    url = "https://api.foursquare.com/v2/venues/40a55d80f964a52020f31ee3/nextvenues?client_id=S3TCARJS00I452G1FSIPZZ0LDOKWX5MBCJ3V1SYPKS2V4Z2I&client_secret=JBJBBXH1RN4D105TFW0O4YEEUAJ2PCKOF5PZEYSBXARLGGZJ&v=20141006"
    venues = fsAPI.venues_NextVenues(url)
    
    fromList = process.iteration(4, venues)
    
    token = fstoken.tokenReady("tokenList.xls", "sheet1")
    
    for i in range(len(fromList)):
        tokenSet = token[i%token.size()]
        url1 = fsURL.makeURL_venues_nextVenues(fromList[i][0], tokenSet)
        venues1 = fsAPI.venues_NextVenues(url1)
        starNode = neo4j.createUniqueNode("Id", fromList[i][0], None)
        
        for j in venues1 :
            endNode = neo4j.createUniqueNode("Id", j[0], None)
            relationId = fromList[i][0]+"_to_"+j[0]
            relation = neo4j.addUniqueRelationship("Id", relationId, starNode, endNode, None)
        