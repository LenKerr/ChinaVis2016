#coding=utf-8
import MySQLdb
import json
import os

conn = MySQLdb.connect(host = "localhost", port = 3306, user = "root", passwd = "wangjunwei", db ="ChinaVis2016")

cur = conn.cursor()
result = cur.execute("select ip from `net192andnet172node`")
rows = cur.fetchall()

ip_name_dict = {}
dict_index = 0
nodes = []
for row in rows:
    node = {}
    node["id"] = dict_index
    node["label"] = row[0]
    #print row[0][:2]
    if row[0][:2] == "19":
        node["group"] = 1
    else:
        node["group"] = 2
    nodes.append(node)
    ip_name_dict[row[0]] = dict_index
    dict_index = dict_index+1


result = cur.execute("select srcip,dstip,filelen from `net192andnet172`")
rows = cur.fetchall()
lines = []
for row in rows:
    line = {}
    line["from"] = ip_name_dict[row[0]]
    line["to"] = ip_name_dict[row[1]]
    line["value"] = row[2]
    lines.append(line)

with open('net192andnnet172.js','w') as f:
    f.write("var nodes = \n")
    f.write(json.dumps(nodes))
    f.write("\n")
    f.write("var edges = \n")
    f.write(json.dumps(lines))
    f.close()
