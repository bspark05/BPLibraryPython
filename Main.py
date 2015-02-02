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
import Variables as var



gdb = GraphDatabase(var.SERVER_ROOT_URI)
    
    
if __name__ == '__main__':
    
    url = var.start_venue("49d77968f964a520275d1fe3")
    venues = fsAPI.venues_NextVenues(url)
    
    fromListIndex= 0
    iterationDepth = 4
    
    if fromListIndex == 0:
        fromList = process.iteration(iterationDepth, venues)
        

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
# insert a field for no. of relationships
    results_all = query.findAllNodes1('id')
    
    for nodes in results_all:
        node = nodes[0]
        q_rel = "MATCH (n{id:'"+node+"'})<--(x) RETURN count(n)"
        q_isLast = "MATCH (n{id:'"+node+"'})-->(x) RETURN count(n)"
        results_rel = gdb.query(q=q_rel)
        results_isLast = gdb.query(q=q_isLast)
    
        q_rel1 = "MATCH (n{id:'"+node+"'}) SET n.RelCount="+str(results_rel[0][0])+" RETURN n.name"
        results_rel1 = gdb.query(q=q_rel1)
        
        if results_isLast[0][0] == 0:            
            q_isLast1 = "MATCH (n{id:'"+node+"'}) SET n.isLast = 1 RETURN n.name, n.isLast"
            results_isLast1 = gdb.query(q=q_isLast1)
        else : 
            q_isLast1 = "MATCH (n{id:'"+node+"'}) SET n.isLast = 0 RETURN n.name, n.isLast"
            results_isLast1 = gdb.query(q=q_isLast1)
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
    shp.save('shapefile/test/point_chicago1')

 
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
    shp_line.save('shapefile/test/line_chicago1')

    
    
    