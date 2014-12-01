'''
Created on Nov 28, 2014

@author: Administrator
'''
import json
import requests

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
        
        
    
        
    