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
    cur.execute('SELECT xb,hylx,fwl,sr,jf,jq,hy,yhz,zxsj FROM bbsdata_0326.l4 where uid ='+ elements[1])
    slist=cur.fetchall()
    # print slist[0][0]

    xingbie = slist[0][0].encode('utf-8')

    if xingbie == '男':
        xingbie = 1
    if xingbie == '女':
        xingbie = 2
    if xingbie == '保密':
        xingbie = -1
    xb =  str(xingbie)
    if xb.strip()=='':
        xingbie = -1
    xingbie = str(xingbie)

    huiyuanleixing = slist[0][1].encode('utf-8')
    if huiyuanleixing == '1':
        huiyuanleixing = 1
    if huiyuanleixing == '2':
        huiyuanleixing = 2
    if huiyuanleixing == 'X':
        huiyuanleixing = 3
    if huiyuanleixing == '家属':
        huiyuanleixing = 4
    if huiyuanleixing == '医生':
        huiyuanleixing = 5
    if huiyuanleixing == '客服':
        huiyuanleixing = 6
    if huiyuanleixing == '其他':
        huiyuanleixing = 7
    if str(huiyuanleixing).strip()=='':
        huiyuanleixing = -1
    huiyuanleixing = str(huiyuanleixing)

    fangwenliang = slist[0][2].encode('utf-8')
    fangwenliang = str(fangwenliang)

    shengri = slist[0][3].encode('utf-8')
    if str(shengri[0:2]).strip()=='':
        age = -1
    elif shengri[0:2] != '19' and shengri[0:2] != '20':
        age = -1
    else:
        shengri = shengri[0:4]
        age = 2016 - int(shengri)
    age = str(age)


    jifen = slist[0][4].encode('utf-8')
    jifen = str(jifen)

    jinqian = slist[0][5].encode('utf-8')
    jinqian = str(jinqian)

    haoyoushu = slist[0][6].encode('utf-8')
    haoyoushu = str(haoyoushu)

    yonghuzu = slist[0][7].encode('utf-8')
    yonghuzudic = {'未晋级':0,'托儿所':1,'幼儿园':2,'小学':3,'初中':4,'高中':5,'大专':6,'预科':7,'本科':8,'硕士':9,'博士':10}
    if str(yonghuzu).strip()=='':
        yonghuzu = 0
    elif yonghuzudic.has_key(yonghuzu):
        yonghuzu = yonghuzudic[yonghuzu]
    else:
        yonghuzu = 11
    yonghuzu = str(yonghuzu)

    zaixianshichang = slist[0][8].encode('utf-8')
    zaixianshichang = str(zaixianshichang)

    temp = xingbie+' '+huiyuanleixing+' '+fangwenliang+' '+age+' '+jifen+' '+jinqian+' '+haoyoushu+' '+yonghuzu+' '+zaixianshichang+'\n'
    print temp
    property.write(temp)
