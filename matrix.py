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

def sequence():
    seq = {}
    edges = open('/Users/cherry/Desktop/t0.txt','r')
    i = 0
    for edge in edges:
        edge = edge.strip()
        elemts = edge.split(',')
        for elemt in elemts:

            if not seq.has_key(elemt):
                seq[elemt] = i
                i = i + 1
    return seq



if __name__ == '__main__':
    # toEdges()
    seq = sequence()
    print seq