'''
Created on Jun 1, 2015

@author: Bumsub
'''
import xlrd
import openpyxl

def excelRead(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)
    
    num_rows = worksheet.nrows -1
    curr_row = -1
    result = []
    
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        result.append(row)
    
    return result

def excelWriteOnExistingFile(filepath, sheetname, columnNum, insult): 
    wb = xlrd.open_workbook(filepath)
    ws = wb.sheet_by_name(sheetname)
    workbook = openpyxl.load_workbook(filepath)
    worksheet = workbook.active
    
    num_rows = ws.nrows -1
    curr_row = -1
    
    while curr_row < num_rows:
        curr_row += 1
        
        worksheet[columnNum+str(curr_row+1)] = insult[curr_row][0]
        asciiNum = ord(columnNum)+1
        columnNumPlus = chr(asciiNum)
        worksheet[columnNumPlus+str(curr_row+1)] = insult[curr_row][1]
        
    workbook.save(filepath)