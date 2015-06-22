'''
Created on Jun 18, 2015

@author: Bumsub
'''

import json
import requests

TT_SEGMENT_URL = 'https://data.cityofchicago.org/resource/n4j6-wkkf.json'
CHICAGO_DATA_TOKEN = 'n33xT1MxDZUaXEd3U9OaVzb5D'

def TT_by_Segment():
    URL = TT_SEGMENT_URL+'?$$app_token='+CHICAGO_DATA_TOKEN+"&$limit=2000"
    request = requests.get(URL)
    ttData = json.loads(request.text)
    
    ttOut = []
    
    for item in ttData:
        ttTemp = []
        ttTemp.append(item['segmentid'].encode("ascii", "ignore"))
        ttTemp.append(item['street'].encode("ascii", "ignore"))
        ttTemp.append(item['_direction'].encode("ascii", "ignore"))
        ttTemp.append(item['_fromst'].encode("ascii", "ignore"))
        ttTemp.append(item['_tost'].encode("ascii", "ignore"))
        ttTemp.append(item['_length'].encode("ascii", "ignore"))
        ttTemp.append(item['_strheading'].encode("ascii", "ignore"))
        ttTemp.append(item['start_lon'].encode("ascii", "ignore"))
        ttTemp.append(item['_lif_lat'].encode("ascii", "ignore"))
        ttTemp.append(item['_lit_lon'].encode("ascii", "ignore"))
        ttTemp.append(item['_lit_lat'].encode("ascii", "ignore"))
        ttTemp.append(item['_traffic'].encode("ascii", "ignore"))
        ttTemp.append(item['_last_updt'].encode("ascii", "ignore"))
        
        ttOut.append(ttTemp)
    
    return(ttOut)
