#coding=utf-8
import MySQLdb
import json
import os

conn = MySQLdb.connect(host = "localhost", port = 3306, user = "root", passwd = "wangjunwei", db ="ChinaVis2016")

cur = conn.cursor()
result = cur.execute("select ip from `ipNodeCountFirstDraw*`")
rows = cur.fetchall()

FocusIplist = ["10.65.216.146","10.18.112.26","10.67.220.221","10.146.216.221","10.114.218.221"]

ip_name_dict = {}
dict_index = 0
nodes = []
for row in rows:
    node = {}
    node["name"] = row[0]
    if row[0] in FocusIplist:
        node["color"] = "red"
        node["opacity"] = 1
        node["display"] = "none"
    else:    
        node["color"] = "green"
        node["opacity"] = 0.2
        node["display"] = "none"
    nodes.append(node)
    ip_name_dict[row[0]] = dict_index
    dict_index = dict_index+1

with open('nodes.json', 'w') as f:
    f.write(json.dumps(nodes))

result = cur.execute("select srcip,dstip from `ipallfirstmonthDraw*`")
rows = cur.fetchall()
lines = []
for row in rows:
    line = {}
    line["source"] = ip_name_dict[row[0]]
    line["target"] = ip_name_dict[row[1]]
    lines.append(line)

with open('edges.json','w') as f:
    f.write(json.dumps(lines))
    




