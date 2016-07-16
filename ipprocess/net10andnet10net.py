#coding=utf-8
import MySQLdb
import json
import os

conn = MySQLdb.connect(host = "localhost", port = 3306, user = "root", passwd = "wangjunwei", db ="ChinaVis2016")

cur = conn.cursor()
total =0
for b in range(256):
    string = "select srcip as ip from rpcServer where srcip like '10."+str(b)+".%' group by ip order by ip "
    result = cur.execute(string)
    rows = cur.fetchall()
    if result >0:
        print "10."+str(b)+" has "+str(result)+" ip"
        total = total + result
print total
