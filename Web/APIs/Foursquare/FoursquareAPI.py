'''
Created on Nov 28, 2014

@author: Administrator
'''
import json
import requests
from _pytest.pastebin import url
from _license import json

def venues_search(url):
    request = requests.get(url)
    fsdata = json.loads(request.text)
    fsout = []
    
    for item in fsdata['response']['venues']:
        fstemp = []
        fstemp.append(item['id'])
        fstemp.append(item['name'])
        
        fstemp.append(item['categories']['name'])
        
        fstemp.append(item['location']['lat'])
        fstemp.append(item['location']['lng'])
        fstemp.append(item['stats']['checkinsCount'])
        fstemp.append(item['stats']['usersCount'])
        
        fsout.append(fstemp)
        
    return fsout
    
        
def venues_NextVenues(url):
    request =requests.get(url)
    fsdata = json.loads(request.text)
    fsout = []
    
    for item in fsdata['response']['nextVenues']['items']:
        fstemp = []
        fstemp.append(item['id'])
        fstemp.append(item['name'])
        
        fstemp.append(item['categories']['name'])
        
        fstemp.append(item['location']['lat'])
        fstemp.append(item['location']['lng'])
        fstemp.append(item['stats']['checkinsCount'])
        fstemp.append(item['stats']['usersCount'])
        
        fsout.append(fstemp)
        
    return fsout    