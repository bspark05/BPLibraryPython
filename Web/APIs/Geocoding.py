'''
Created on Jun 1, 2015

@author: Bumsub
'''
from geopy.geocoders import Nominatim

def geocodeList(addressExcelList):
    geolocator = Nominatim()
    searchingAddress = ''
    for rows in addressExcelList:
        searchingAddress+=addressExcelList[rows][3].value
        searchingAddress+=addressExcelList[rows][4].value
        searchingAddress+=addressExcelList[rows][6].value
        searchingAddress+=addressExcelList[rows][7].value    
        
        #location = geolocator.geocode(addressExcelList[rows][columns])
    