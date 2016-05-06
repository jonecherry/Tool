#coding=utf-8
import  MySQLdb
import linecache

conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306, charset='utf8')
cur=conn.cursor()
cur.execute('set interactive_timeout=96*3600')
conn.select_db('bbsdata')

tb= 'l4'

property = open('property.dat','w')
f = open('Network/2016_05_06_23_16_45/Nodeindex.csv','r')
count = len(f.readlines())
for i in range(count):
    line = linecache.getline('Network/2016_05_06_23_16_45/Nodeindex.csv',i+1)
    elements = line.split(':')
    cur.execute('SELECT xb,hylx,fwl FROM bbsdata_0326.l4 where uid ='+ elements[1])
    slist=cur.fetchall()
    # print slist[0][0]

    xingbie = slist[0][0].encode('utf-8')

    if xingbie == '男':
        xingbie = 1
    if xingbie == '女':
        xingbie = 2
    if xingbie == '保密':
        xingbie = 3
    xb =  str(xingbie)
    if xb.strip()=='':
        xingbie = 3
    xingbie = str(xingbie)

    huiyuanleixing = slist[0][1].encode('utf-8')
    if huiyuanleixing == '客服':
        huiyuanleixing = 3
    if huiyuanleixing == '医生':
        huiyuanleixing = 1
    if huiyuanleixing == '家属':
        huiyuanleixing =4
    if huiyuanleixing == '其他':
        huiyuanleixing = 5

    if str(huiyuanleixing).strip()=='':
        huiyuanleixing = 6
    if huiyuanleixing == 'X':
        huiyuanleixing = 7
    huiyuanleixing = str(huiyuanleixing)
    fangwenliang = slist[0][2].encode('utf-8')

    fangwenliang = str(fangwenliang)

    temp = xingbie+' '+huiyuanleixing+' '+fangwenliang+'\n'
    print temp
    property.write(temp)
