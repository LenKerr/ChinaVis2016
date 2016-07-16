#coding=utf-8

import MySQLdb
import json

conn = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="wangjunwei",db="ChinaVis2016")
c = conn.cursor()

sql = "select sip_id as id,srcip as label from ((select distinct sip_id,SRCIP from day26 ) union \
        (select distinct dip_id,dstIP from day26 ) union (select distinct sport_id,SRCPORT from day26 ) \
        union (select distinct dport_id,DSTPORT from day26 )) a"
c.execute(sql)
nodes = []
for row in c.fetchall():
    node = {}
    node["id"] = row[0]
    node["label"] = row[1]
    if "." in node["label"]:
        node["shape"] = "circle"
        if row[1][:3] == "192":
            node["group"] = 1
        else:
            node["group"] = 2
    else:
        node["size"] = 80 
        node["shape"] = "diamond"
        node["group"] = 3
    nodes.append(node)

print nodes
lines = []
sql = "select sip_id,sport_id,dport_id,dip_id from day26"
c.execute(sql)
for row in c.fetchall():
    lines.append({"from":row[0],"to":row[1]})
    lines.append({"from":row[1],"to":row[2]})
    lines.append({"from":row[2],"to":row[3]})

#print len(lines)
with open('day26.js',"w") as f:
    f.write("var nodes=\n")
    f.write(json.dumps(nodes))
    f.write("\n")
    f.write("var edges=\n")
    f.write(json.dumps(lines))
    f.close()

