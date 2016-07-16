#coding=utf-8
import MySQLdb
import json
import os

conn = MySQLdb.connect(host = "localhost", port = 3306, user = "root", passwd = "wangjunwei", db ="ChinaVis2016")

cur = conn.cursor()

focusiplist = []
string = "select * from (select srcip as ip ,sum(cnum) as n,count(*) as c,sum(filelen) as s from net10andnet10searchserver group by srcip order by count(*) desc) a where c>24 and s>27197408 and n > 3015 order by ip"
result = cur.execute(string)
rows = cur.fetchall()
for row in rows:
    focusiplist.append(row[0])

result = cur.execute("select ip from `net10andnet10nodeDraw*`")
rows = cur.fetchall()

ip_name_dict = {}
dict_index = 0
nodes = []

bset = []
for row in rows:
    node = {}
    node["id"] = dict_index
    node["label"] = row[0]
    bstring = row[0].split(".")[1]
    if bstring not in bset:
        bset.append(bstring)
    if row[0] in focusiplist:
        node["color"] = "rgba(255,0,0,1)"
    node["group"] = bset.index(bstring)
    nodes.append(node)
    ip_name_dict[row[0]] = dict_index
    dict_index = dict_index+1


result = cur.execute("select srcip,dstip,cnum,filelen from `net10andnet10Draw*`")
rows = cur.fetchall()
lines = []
for row in rows:
    line = {}
    line["from"] = ip_name_dict[row[0]]
    line["to"] = ip_name_dict[row[1]]
    line["color"] = "rgba(0,0,255,0.09)"
    line["value"] = row[2]*row[3]/1000.0
    lines.append(line)

with open('net10andnet10.js','w') as f:
    f.write("var nodes = \n")
    f.write(json.dumps(nodes))
    f.write("\n")
    f.write("var edges = \n")
    f.write(json.dumps(lines))
    f.close()
