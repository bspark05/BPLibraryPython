'''
Created on Nov 30, 2014

@author: Administrator
'''
import xlrd
from future.backports.email._header_value_parser import TokenList

def tokenReady(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)
    
    num_rows = worksheet.nrows -1
    curr_row = -1
    fstoken = []
    
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        fstoken.append(row)
    
    return fstoken

def tokenIterator(tokenList, index):
    tokenPair = []
    i = index%tokenList.size()
    tokenPair = tokenList[i]
    ++index
    
    if index>tokenList.size():
        index=0
        
    return tokenPair
        
    