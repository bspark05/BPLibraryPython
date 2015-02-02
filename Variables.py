'''
Created on Feb 1, 2015

@author: Bumsub
'''

SERVER_ROOT_URI = 'http://localhost:7474/db/data/'
START_VENUE1 = "https://api.foursquare.com/v2/venues/"
START_VENUE2 = "/nextvenues?client_id=S3TCARJS00I452G1FSIPZZ0LDOKWX5MBCJ3V1SYPKS2V4Z2I&client_secret=JBJBBXH1RN4D105TFW0O4YEEUAJ2PCKOF5PZEYSBXARLGGZJ&v=20141006"


def start_venue(venueId):
    uri = START_VENUE1+venueId+START_VENUE2
    return uri