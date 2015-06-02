'''
Created on Jun 1, 2015

@author: Bumsub
'''
#from geopy.geocoders import Nominatim
import geocoder

def geocodeList(addressExcelList):
    
    #geolocator = Nominatim()
    searchingAddress = ''
    resultList = []
    count = 0
    for rows in addressExcelList:
        searchingAddress=''
        searchingAddress+=str(rows[3].value)
        searchingAddress+=' '
        searchingAddress+=str(rows[4].value)
        searchingAddress+=' '
        searchingAddress+=str(rows[6].value)
        searchingAddress+=' '
        searchingAddress+=str(rows[7].value)    
        
        print(searchingAddress)
        location = geocoder.google(searchingAddress)
        print(location.latlng)
        if location.latlng == [] :
            resultList.append(['',''])
        else:
            resultList.append(location.latlng)
            
        print(count)
        count+=1
    return resultList