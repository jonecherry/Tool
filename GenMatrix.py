#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb
import os
from numpy import *
from random import sample
import time

def jiaoji(lists) :
    temp= lists[0]
    for list in lists :
        temp=[i for i in list if i in temp ]
    return temp



def getlist(db):
    distinct_all=[]
    edges=[]
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306, charset='utf8')   
        cur=conn.cursor()
        cur.execute('set interactive_timeout=96*3600')
        conn.select_db(db)
        
        for tb in ['l4']:
            
            print 'reading '+db+'.'+tb+'...'
            cur.execute("SELECT uid,friends FROM "+tb)
            slist=cur.fetchall()
        #        print l3list
            print '%s cases in total.'%(len(slist))
            for line in slist:
                uid=line[0]
                if str(uid) not in distinct_all:
                    distinct_all.append(str(uid))
                friends=line[1]
                friends=friends.strip(';')
                flist=friends.split(';')
                for friend in flist:
                    if friend not in distinct_all :
                        distinct_all.append(friend)
                    edges.append((friend,str(uid)))
            
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    else:
        print 'Successful!'
    finally:
        cur.close()
        conn.close()
        print 'done'
    return (distinct_all,edges)



def genMatrix(rows,cols):  
    matrix = [[0 for col in range(cols)] for row in range(rows)]  
    for i in range(rows):  
        for j in range(cols):  
            matrix[i][j]
    return matrix


if __name__=='__main__':
    time_stamp = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    if not os.path.exists('Network'):
        os.mkdir('Network')
    time_stamp_folder = os.path.join('Network',time_stamp)
    os.mkdir(time_stamp_folder)
    addset=[]
    edgelists={}
    for db in ['bbsdata','bbsdata_0306']:
        temp = getlist(db)
        addset.append(temp[0])
        edgelists[db]=temp[1]
    
    unionNodes = jiaoji(addset)
    
    slice = sample(unionNodes,1000)
    d = len(slice)
    
    print 'there are '+str(d)+' users in all databases sampled'
    print 'generating index for uid...'
    NodesIndex = open (os.path.join(time_stamp_folder,'NodeIndex.csv'),'w')
    for i in range(d):
        aaa = str(i)+':'+slice[i]+'\n'
        NodesIndex.write(aaa)
    NodesIndex.close()    
    print 'generating matrix...'
    for key in edgelists:
        edgelist = edgelists[key]
        if not os.path.exists(os.path.join(time_stamp_folder,key)):
            os.mkdir(os.path.join(time_stamp_folder,key))
        matrixFile = open(os.path.join(time_stamp_folder,key,'matrix_Di.csv'),'a')   
        for i in range(d):
            row='';
            for j in range(d):
                if (slice[i],slice[j]) in edgelist:
                    matrixFile.write(str(1)+'    ')
#                    row = row+'1    '
                else:
                    matrixFile.write(str(0)+'    ')
#                    row = row+'0    '
            matrixFile.write(row+'\n')
        matrixFile.close()
    print 'complete!'
        