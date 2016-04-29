#coding=utf-8
import MySQLdb

minnum = 2

friendsnum = []
try:
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',port=3306, charset='utf8')
    cur=conn.cursor()
    cur.execute('set interactive_timeout=96*3600')
    conn.select_db('bbsdata')

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


except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

finally:
    cur.close()
    conn.close()
print friendsnum