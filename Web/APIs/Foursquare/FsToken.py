'''
Created on Nov 30, 2014

@author: Administrator
'''
import xlrd

def tokenReady(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)
    worksheet = workbook.sheet_by_name(sheetname)
    
    num_rows = worksheet.nrows -1
    curr_row = -1
    
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        print row