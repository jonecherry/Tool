#coding=utf-8
import xlrd

def toEdges():
    data = xlrd.open_workbook('/Users/cherry/Desktop/ceshi.xls')
    table = data.sheet_by_index(0)
    edges = open('/Users/cherry/Desktop/t0.txt','w')

    for col in range(table.ncols):

        startNode = str(table.row(col)[0].value)
        endNodes = str(table.row(col)[1].value)
        nodes = endNodes.split(',')
        for node in nodes:
            line = startNode+','+node+'\n'
            edges.write(line)
    edges.close()

if __name__ == '__main__':
    toEdges()