'''
Created on Dec 1, 2014

@author: Administrator
'''
import xlrd

def boundaryReady(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)
    
    num_rows = worksheet.nrows -1
    curr_row = -1
    boundary = []
    
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        boundary.append(row)
    
    return boundary

def makeURL_venues_search(radius, lat, lng, tokenSet):
    clientId = tokenSet[0]
    clientSc = tokenSet[1]
    tokenDate = tokenSet[2]
    
    url = 'https://api.foursquare.com/v2/venues/search?ll='+lat+','+lng+'&radius='+radius+'&limit=50&&client_id='+clientId.value+'&client_secret='+clientSc.value+'&v='+tokenDate.value
    
    return url

def makeURL_venues_nextVenues(placeID, tokenSet):
    clientId = tokenSet[0]
    clientSc = tokenSet[1]
    tokenDate = tokenSet[2]
    
    url = 'https://api.foursquare.com/v2/venues/'+placeID+'/nextvenues?client_id='+clientId.value+'&client_secret='+clientSc.value+'&v='+tokenDate.value
    
    print(url)
    return url