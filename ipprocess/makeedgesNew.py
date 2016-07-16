#coding=utf-8
import json
import MySQLdb

jsonstr = ""
with open("ipServerNew.json","rw") as f:
    for row in f:
        jsonstr = jsonstr + row
#print jsonstr
nodesdictlist = json.loads(jsonstr)
nodesnamelist = []
nodeslist = []
ip_name_dict = {}
dict_index = 0
for each in nodesdictlist:
    node = {}
    node["id"] = dict_index
    node["label"] = each["name"]
    node["group"] = each["group"]
    nodeslist.append(node)
    ip_name_dict[each["name"]] = dict_index
    dict_index = dict_index + 1
    nodesnamelist.append(each["name"])

#print nodeslist

conn = MySQLdb.connect(host = "localhost", port = 3306, user = "root", passwd = "wangjunwei", db ="ChinaVis2016")

cur = conn.cursor()
result = cur.execute("select srcip,dstip from `net10andnet10`")
rows = cur.fetchall()

edgeslist = []

for row in rows:
    if row[0] in nodesnamelist and row[1] in nodesnamelist:
        line = {}
        line["from"] = ip_name_dict[row[0]]
        line["to"] = ip_name_dict[row[1]]
        edgeslist.append(line)

#print edgeslist
 
with open("ipServerNew.js","w") as f:
    f.write("var nodes = \n")
    f.write(json.dumps(nodeslist))
    f.write("\n")
    f.write("var edges = \n")
    f.write(json.dumps(edgeslist))
    f.close


    
