'''
Created on Nov 28, 2014

@author: Administrator
'''
def readAll(reader):
    while (cp = reader.read()) != -1 :
        stringBuilder.append((char) cp)
    return stringBuilder.toString()

def readJsonFromUrl(url):
    inputStream =       