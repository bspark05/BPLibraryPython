'''
Created on Dec 1, 2014

@author: Administrator
'''

import Web.APIs.Foursquare.FoursquareAPI as fsAPI
import Web.APIs.Foursquare.FsToken as fstoken
import Web.APIs.Foursquare.FsURL as fsURL

def iteration(depth, fromList):
    token = fstoken.tokenReady('tokenList.xls', 'Sheet1')
    
    indexFromList = len(fromList)
    print('initial no. of fromList = ' + str(indexFromList))
    
    startIndex = 0
    
    while depth>0:
        tempFromList = []
        print('depth = '+ str(depth))
        for k in fromList:
            tempFromList.append(k)
        print('size of tempFromList = '+ str(len(tempFromList)))
        
        index = 0
        
        for index, list1 in enumerate(tempFromList[startIndex:]):
            tokenSet = token[index%len(token)]
            
            url = fsURL.makeURL_venues_nextVenues(list1[0], tokenSet)
            venues1 = fsAPI.venues_NextVenues(url)
            
            for j in venues1:
                resultFromList = checkList(j, fromList)
                fromList = resultFromList
            ++index
            print('# in fromList = '+ str(index))
        startIndex = startIndex+index
        
        depth = depth -1
        print('size of fromList in the depth = '+str(len(fromList)))
        
    print('final len(fromList) = '+ str(len(fromList)))
    return fromList    

def checkList(oneVenue, fromList):
    for i in fromList:
        if i[0] == oneVenue[0] :
            print('in the list')
            return fromList
    fromList.append(oneVenue)
    print('added value = '+ oneVenue[0])
    return fromList

def setAttributes(venue):
    attribute = ''
    attribute+= '{ \"name\" : \"'+ venue[1] +'\", '
    attribute+= ' \"category\" : \"' + venue[2] +'\", '
    attribute+= ' \"lat\" : \"' + str(venue[3]) + '\", '
    attribute+= ' \"lng\" : \"' + str(venue[4]) + '\", '
    attribute+= ' \"checkins\" : \"' + str(venue[5]) + '\", '
    attribute+= ' \"users\" : \"' + str(venue[6]) + '\"}'
    print(attribute)
    return attribute;
    