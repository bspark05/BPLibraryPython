'''
Created on Nov 28, 2014

@author: Administrator
'''

import Web.APIs.Foursquare.FoursquareAPI as fsAPI
import Web.APIs.Foursquare.FsURL as fsURL
import Web.APIs.Foursquare.FsToken as fstoken
import Process as process
import Database.Neo4j.Neo4jQuery as query
from neo4jrestclient.client import GraphDatabase
import shapefile
import xlrd
import xlwt


SERVER_ROOT_URI = 'http://localhost:7474/db/data/'
gdb = GraphDatabase(SERVER_ROOT_URI)
    
    
if __name__ == '__main__':
    
    url = "https://api.foursquare.com/v2/venues/4a8b60c7f964a5204d0c20e3/nextvenues?client_id=S3TCARJS00I452G1FSIPZZ0LDOKWX5MBCJ3V1SYPKS2V4Z2I&client_secret=JBJBBXH1RN4D105TFW0O4YEEUAJ2PCKOF5PZEYSBXARLGGZJ&v=20141006"
    venues = fsAPI.venues_NextVenues(url)
    
    fromListIndex=1
    iterationDepth = 1
    
    if fromListIndex == 0:
        fromList = process.iteration(1, venues)
        

        workbookOut = xlwt.Workbook()
        sheet = workbookOut.add_sheet("sheet1")
        for index1, value1 in enumerate(fromList):
            for index2, value2 in enumerate(value1):
                sheet.write(index1, index2, value2)
        workbookOut.save('fromList.xls')
    else:
        workbook = xlrd.open_workbook("fromList.xls")
        worksheet = workbook.sheet_by_name("sheet1")
    
        num_rows = worksheet.nrows -1
        curr_row = -1
        fromListInit = []
    
        while curr_row < num_rows:
            curr_row += 1
            row = worksheet.row(curr_row)
            fromListInit.append(row)
        
        fromListInitAfter = []
        for j in fromListInit:
            fromListInitAfterTemp = [str(j[0].value),str(j[1].value),str(j[2].value),float(j[3].value),float(j[4].value),float(j[5].value),float(j[6].value)]
            fromListInitAfter.append(fromListInitAfterTemp)


        fromList = process.iteration(iterationDepth, fromListInitAfter)


        workbookOut = xlwt.Workbook()
        sheet = workbookOut.add_sheet("sheet1")
        for index1, value1 in enumerate(fromList):
            for index2, value2 in enumerate(value1):
                sheet.write(index1, index2, value2)
        workbookOut.save('fromList.xls')
    
    
    
    
    for list in fromList:
        attribute = query.setAttributesNode(list)
        startNode = query.createUniqueNode(attribute)

    token = fstoken.tokenReady("tokenList.xls", "Sheet1")
    
    for i in range(len(fromList)):
        tokenSet = token[i%len(token)]
        url1 = fsURL.makeURL_venues_nextVenues(fromList[i][0], tokenSet)
        venues1 = fsAPI.venues_NextVenues(url1)
        
        nodeAttribute1 = query.setAttributesNode(fromList[i])
        starNode = query.createUniqueNode(nodeAttribute1)
        
        for j in venues1 :
            nodeAttribute2 = query.setAttributesNode(j)
            endNode = query.createUniqueNode(nodeAttribute2)
            
            relAttribute = query.setAttributesRel(starNode[0], endNode[0])
            relation = query.addUniqueRelationship(starNode[0], endNode[0], relAttribute)
            
    
# insert a field for isLast
    results_all1= query.findAllNodes1('id')
    
    for nodes in results_all1:
        node = nodes[0]
        q_isLast1 = "MATCH (n{id:'"+node+"'}) SET n.isLast = 1 RETURN n.name, n.isLast"
        results_isLast1 = gdb.query(q=q_isLast1)    
    
    for k in fromList:
        id_fromList=k[0]
        q_isLast2="MATCH (k {id:'"+id_fromList+"'}) SET k.isLast = 0 RETURN k.name, k.isLast"
        results_isLast2 = gdb.query(q=q_isLast2)
        #print(results_isLast2[0])


# insert a field for no. of relationships
    results_all = query.findAllNodes1('id')
    
    for nodes in results_all:
        node = nodes[0]
        q_node = "MATCH (n{id:'"+node+"'})<--(x) RETURN count(n)"
        results_node = gdb.query(q=q_node)
    
        q_write = "MATCH (n{id:'"+node+"'}) SET n.RelCount="+str(results_node[0][0])+" RETURN n.name"
        results_write = gdb.query(q=q_write)
        #print([results_node[0][0],results_write[0][0]])

    
    
# convert to shpfile_Point
    results_point = query.findAllNodes()    
    shp = shapefile.Writer(shapefile.POINT)
    shp.field('Id')
    shp.field('name')
    shp.field('category')
    shp.field('lat','F')
    shp.field('lng','F')
    shp.field('checkins','F')
    shp.field('users','F')
    shp.field('isLast','F')
    shp.field('RelCount','F')
    
    for pnt in results_point:
        print(pnt[0])
        shp.point(pnt[0]['data']['lng'],pnt[0]['data']['lat'])
        shp.record(pnt[0]['data']['id'],pnt[0]['data']['name'],pnt[0]['data']['category'],pnt[0]['data']['lat'],pnt[0]['data']['lng'],pnt[0]['data']['checkins'],pnt[0]['data']['users'],
                   pnt[0]['data']['isLast'],pnt[0]['data']['RelCount'])
        #print(pnt[0]['data']['name'])
    shp.save('shapefile/test/point1')

 
# convert to shpfile_Line
    results_line = query.findAllRelationships()
    
    shp_line = shapefile.Writer(shapefile.POLYLINE)
    shp_line.field('fromLng','F')
    shp_line.field('fromLat','F')
    shp_line.field('fromId')
    shp_line.field('fromName')
    shp_line.field('fromCate')
    shp_line.field('fromChins','F')
    shp_line.field('fromUsers','F')
    shp_line.field('toLng','F')
    shp_line.field('toLat','F')
    shp_line.field('toId')
    shp_line.field('toName')
    shp_line.field('toCate')
    shp_line.field('toChins','F')
    shp_line.field('toUsers','F')
    
    for line in results_line:
        shp_line.line(parts=[[[line[0]['data']['fromLng'],line[0]['data']['fromLat']],[line[0]['data']['toLng'],line[0]['data']['toLat']]]])
        shp_line.record(line[0]['data']['fromLng'],line[0]['data']['fromLat'],line[0]['data']['fromId'],line[0]['data']['fromName'],line[0]['data']['fromCate'],line[0]['data']['fromCheckins'],line[0]['data']['fromUsers'],
                    line[0]['data']['toLng'],line[0]['data']['toLat'],line[0]['data']['toId'],line[0]['data']['toName'],line[0]['data']['toCate'],line[0]['data']['toCheckins'],line[0]['data']['toUsers'])    
    shp_line.save('shapefile/test/line1')

    
    
    