'''
Created on Dec 1, 2014

@author: Administrator
'''

import Database.Neo4j.Relationship as relationship
import requests
import Variables as var


def createUniqueNode(key, value, jsonAttributes):
    try:
        nodePointUrl = var.SERVER_ROOT_URI + '/db/data/index/node/venue?uniqueness=get_or_create'
        
        # set json payload
        nodeKeyValueJson = generateJsonUniqueNode(key, value, jsonAttributes)
        #print(nodeKeyValueJson)
        # set headers
        headers = {'content-type':'application/json', 'accept':'application/json'}
        
        request = requests.post(nodePointUrl, data=nodeKeyValueJson, headers=headers)
        print(request)
        
        locationHeader = request.headers.get('location')
        return locationHeader
    except :
        print('Exception in creating node in neo4j')   
        
def generateJsonUniqueNode(key, value, jsonAttributes):
    sb = ''
    sb+='{ \"key\" : \"'
    sb+=key
    sb+='\",'
    
    sb+='\"value\" : \"'
    sb+=value
    
    #if jsonAttributes == None | len(jsonAttributes)<1:
    if jsonAttributes == None :    
        sb+='\"'
    else:
        sb+='\", \"properties\" : '
        for i in jsonAttributes:
            sb+=i
            if i < len(jsonAttributes):
                sb+=', '
    sb+=' }'

    return sb            
        
def addUniqueRelationship(key, value, startNodeURI, endNodeURI, jsonAttributes):
    try:
        fromUrl = var.SERVER_ROOT_URI +'/db/data/index/relationship/rels?uniqueness=get_or_create'
        print('from URL : '+ fromUrl)
        
        relationshipJson = generateJsonUniqueRelationship(key, value, startNodeURI, endNodeURI, jsonAttributes)
        print('relationshipJson : '+ relationshipJson)
        
        headers = {'content-type':'application/json', 'accept':'application/json'}
        
        request = requests.post(fromUrl, data=relationshipJson, headers=headers)
        print(request)
        locationHeader = request.headers.get('location')
        return locationHeader
    except :
        print('Exception in creating relationship in neo4j')
        
def generateJsonUniqueRelationship(key, value, startNodeURI, endNodeURI, jsonAttributes):
    sb = ''
    sb+='{ \"key\" : \"'
    sb+=key
    sb+='\",'
    
    sb+='\"value\" : \"'
    sb+=value
    sb+='\", '
    
    sb+='\"start\" : \"'
    sb+=startNodeURI
    sb+='\", '
    
    sb+='\"end\" : \"'
    sb+=endNodeURI
    sb+='\", '
    
    sb+='\"type\" : \"'
    sb+='next'
    
    if jsonAttributes == None:
        sb+='\"'
    else:
        sb+='\", \"data\" : {'
        for i in jsonAttributes:
            sb+=i
            if i < len(jsonAttributes):
                sb+=', '
    sb+=' }'

    return sb
    