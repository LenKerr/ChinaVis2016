#coding=utf-8
import MySQLdb
import json
import os

conn = MySQLdb.connect(host = "localhost", port = 3306, user = "root", passwd = "wangjunwei", db ="ChinaVis2016")

string = ""
cur = conn.cursor()
#result = cur.execute("select distinct id from `vcpip` where vpi1 = 9075 and vci1 = 883 order by id")
sql = "select distinct id from vcpip where ip in (select srcip from ((select distinct srcip from exception) UNION (select distinct dstip from exception) ) a)"
cur.execute(sql)

rows = cur.fetchall()
for row in rows:
    string = string + str(row[0])+","

print string
