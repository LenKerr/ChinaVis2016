#coding=utf-8
import MySQLdb
import json
import os

conn = MySQLdb.connect(host = "localhost", port = 3306, user = "root", passwd = "wangjunwei", db ="ChinaVis2016")

cur = conn.cursor()
result = cur.execute("select ip from ``")
rows = cur.fetchall()

ip_name_dict = {}
dict_index = 0
nodes = []
for row in rows:
    node = {}
    node["name"] = row[0]
    node["color"] = "green"
    node["opacity"] = 0.2
    node["display"] = "show"
    nodes.append(node)
    ip_name_dict[row[0]] = dict_index
    dict_index = dict_index+1

result = cur.execute("select srcip,dstip from ``")
rows = cur.fetchall()
lines = []
for row in rows:
    line = {}
    line["source"] = ip_name_dict[row[0]]
    line["target"] = ip_name_dict[row[1]]
    line["color"] = "blue"
    line["opacity"] = 0.2
    lines.append(line)

with open('net10and10.json','w') as f:
    data = {}
    data["nodes"] = nodes
    data["edges"] = lines
    f.write(json.dumps(data))

