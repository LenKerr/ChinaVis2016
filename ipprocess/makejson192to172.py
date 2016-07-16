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

srciplist = ["192.168.85.50","192.168.21.50","192.168.213.50","192.168.117.50","192.168.69.50"]

dstiplist = ["172.20.8.30","172.20.8.46",
            "172.20.8.54","172.20.8.58","172.20.8.60","172.20.8.61",
            "172.20.8.62"]
for row in rows:
    node = {}
    node["name"] = row[0]
    #print row[0][:2]
    if row[0] in srciplist:
        node["color"] = "brown"
    elif row[0] in dstiplist:
        node["color"] = "purple"
    elif row[0][:2] == "19":
        node["color"] = "green"
    else:
        node["color"] = "red"
    node["opacity"] = 0.2
    node["display"] = "show"
    nodes.append(node)
    ip_name_dict[row[0]] = dict_index
    dict_index = dict_index+1

result = cur.execute("select srcip,dstip from `net192andnet172`")
rows = cur.fetchall()
lines = []
for row in rows:
    line = {}
    line["source"] = ip_name_dict[row[0]]
    line["target"] = ip_name_dict[row[1]]
    line["color"] = "blue"
    line["opacity"] = 0.1
    lines.append(line)

with open('net192to172.json','w') as f:
    data = {}
    data["nodes"] = nodes
    data["edges"] = lines
    f.write(json.dumps(data))

