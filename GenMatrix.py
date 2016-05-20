#!/usr/bin/env python
#coding=utf-8

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
def friendsnum():
    limit = 0
    minnum = 5
    friendsnum = []
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306, charset='utf8')
        cur=conn.cursor()
        cur.execute('set interactive_timeout=96*3600')
        conn.select_db('bbsdata')
        # conn.select_db('test1')

        for tb in ['l4']:


            cur.execute("SELECT uid,friends FROM "+tb)
            slist=cur.fetchall()
            for line in slist:

                uid=int(line[0])
                friends=line[1]
                friends=friends.strip(';')
                flist=friends.split(';')
                numoffriends = len(flist)
                if numoffriends >= minnum:

                    friendsnum.append(uid)
                limit = limit +1
                # if limit == 10000:
                #     break

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    finally:
        cur.close()
        conn.close()

    return friendsnum

def qujiaoji(unionNodes,umatch):
    slice = []
    for node in umatch:
        if str(node) in unionNodes:
            slice.append(int(node))
            if len(slice)>=500:
                break
    return slice


def getlist(db):
    linelimit = 0
    distinct_all=[]
    edges=[]
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306, charset='utf8')
        cur=conn.cursor()
        cur.execute('set interactive_timeout=96*3600')
        conn.select_db(db)
        
        for tb in ['l4']:
            
            print 'reading '+db+'.'+tb+'...'
            cur.execute("SELECT uid,friends FROM "+tb+" WHERE uid IN (SELECT uid FROM bingbingusers)")
            slist=cur.fetchall()
        #        print l3list
            print '%s cases in total.'%(len(slist))
            for line in slist:



                uid=str(line[0])
                uid = uid.encode("utf-8")
                if uid not in distinct_all:
                    distinct_all.append(uid)
                friends=line[1]
                friends = friends.encode("utf-8")
                friends=friends.strip(';')
                flist=friends.split(';')
                # print flist
                # print '-----------------distinctall----------------------'
                # print distinct_all
                for friend in flist:
                    # print friend

                    if friend not in distinct_all :
                        # print friend
                        distinct_all.append(friend)
                    # print friend

                    # edge = (friend,uid)
                    # print edge
                    edges.append((friend,uid))
                linelimit = linelimit +1
                # if linelimit ==10000:
                #     break
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
    for db in ['bbsdata','bbsdata_0306','bbsdata_0326']:
    # for db in ['test1','test2']:
        temp = getlist(db)
        addset.append(temp[0])
        edgelists[db]=temp[1]
    
    unionNodes = jiaoji(addset)
    # print '------------unionnodes-------------'
    # print unionNodes
    umatch = friendsnum()
    # print '------------度满足条件的点--------'
    # print umatch
    # slice = qujiaoji(unionNodes,umatch)
    slice = unionNodes
    print '------------样本-----------------'
    print slice


    d = len(slice)
    
    print 'there are '+str(d)+' users in all databases sampled'
    print 'generating index for uid...'
    NodesIndex = open (os.path.join(time_stamp_folder,'NodeIndex.csv'),'w')
    for i in range(d):
        aaa = str(i)+':'+str(slice[i])+'\n'
        NodesIndex.write(aaa)
    NodesIndex.close()    
    print 'generating matrix...'

    for key in edgelists:

        edgelist = edgelists[key]
        # print '--------------边-------------------'
        # print edgelist[0]
        if not os.path.exists(os.path.join(time_stamp_folder,key)):
            os.mkdir(os.path.join(time_stamp_folder,key))
        matrixFile = open(os.path.join(time_stamp_folder,key,'matrix_Di.csv'),'a')   
        for i in range(d):
            row='';
            for j in range(d):
                if (str(slice[i]),str(slice[j])) in edgelist:
                    matrixFile.write(str(1)+'    ')
#                    row = row+'1    '
                else:
                    matrixFile.write(str(0)+'    ')
#                    row = row+'0    '
            matrixFile.write(row+'\n')
        matrixFile.close()
    print 'complete!'
        