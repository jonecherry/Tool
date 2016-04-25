import xlrd

array = [[1,2],[3,4]]
out = open('/Users/cherry/Desktop/juzhen','w')
for i in range(len(array)):
    for j in range(len(array[i])):
        out.write('%s'%(array[i][j]))
        out.write('\t')


    out.write('\n')
out.close()