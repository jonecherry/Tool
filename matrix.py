#coding=utf-8
import xlrd
import math

def toEdges():
    data = xlrd.open_workbook('/Users/cherry/Desktop/ceshi.xls')
    table = data.sheet_by_index(0)
    edges = open('/Users/cherry/Desktop/t0.txt','w')

    for col in range(table.ncols):

        startNode = table.row(col)[0].value
        startNode = int(startNode)
        startNode = str(startNode)
        endNodes = table.row(col)[1].value
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
            elemt = int(elemt)
            if not seq.has_key(elemt):
                seq[elemt] = i
                i = i + 1
    return seq
def multiArray():
    Array = []
    dimensions = len(seq)
    for i in range(dimensions):
        line = []
        for j in range(dimensions):
            line.append(0)
        Array.append(line)
    # print Array
    edges = open('/Users/cherry/Desktop/t0.txt','r')
    for edge in edges:
        elements = edge.split(',')
        x = seq[int(elements[0])]
        y = seq[int(elements[1])]

        Array[x][y] = 1
    return Array


def printArray(array):
    out = open('/Users/cherry/Desktop/juzhen1','w')
    for i in range(len(array)):
        for j in range(len(array[i])):
            out.write('%s'%(array[i][j]))
            out.write('\t')
        out.write('\n')
    out.close()
    print '关系矩阵生成'

if __name__ == '__main__':
    # toEdges()
    seq = sequence()
    Array = multiArray()

    printArray(Array)