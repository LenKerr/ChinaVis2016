#coding=utf-8

import json
import MySQLdb

nodesdictlist = None
with open("ipServerNew.json","rw") as f:
    nodesdictlist = json.loads(f.read())

conn = MySQLdb.connect(host="localhost",port = 3306,user = "root",passwd = "wangjunwei",db ="ChinaVis2016")
cur = conn.cursor()

for each in nodesdictlist:
    sql = "insert into net726node(ip,groupnum) values('"+ each["name"]+"',"+str(each["group"])+");"
    print sql
    cur.execute(sql)
    
