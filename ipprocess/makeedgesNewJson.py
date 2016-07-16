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
    node["name"] = each["name"]
    node["display"] = "show"
    node["opacity"] = 0.4
    if each["group"] == 1:
        node["color"] = "#ff7f0e" 
    elif each["group"] == 2:
        node["color"] = "#2ca02c"
    elif each["group"] == 3:
        node["color"] = "#d62728"
    elif each["group"] == 4:
        node["color"] = "#9467bd"
    elif each["group"] == 5:
        node["color"] = "#8c564b"
    elif each["group"] == 6:
        node["color"] = "#e377c2"
    elif each["group"] == 7:
        node["color"] = "#7f7f7f"
    elif each["group"] == 8:
        node["color"] = "#bcbd22"
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
        line["source"] = ip_name_dict[row[0]]
        line["target"] = ip_name_dict[row[1]]
        line["color"] = "blue"
        crowdlist = ["10.18.112.26","10.18.112.242","10.18.112.244","10.18.112.246","10.18.112.247","10.19.112.246","10.33.216.221","10.33.219.246","10.39.216.247","10.46.236.221","10.39.216.247","10.50.112.246","10.54.216.221","10.67.216.221","10.114.218.221","10.116.217.221","10.118.216.221","10.145.216.221","10.146.216.221"]
        if row[0] in crowdlist or row[1] in crowdlist:
            line["opacity"] = 0.00001
        else:
            line["opacity"] = 0.05
        edgeslist.append(line)

#print edgeslist
 
with open("ipServerNewGraph.json","w") as f:
    data = {}
    data["nodes"] = nodeslist
    data["edges"] = edgeslist
    f.write(json.dumps(data))
    f.close()

nodeslist = []
dict_index = 0
for each in nodesdictlist:
    node = {}
    node["id"] = dict_index
    node["label"] = each["name"]
    node["group"] = each["group"]
    nodeslist.append(node)
    dict_index = dict_index +1

edgeslist = []

for row in rows:
    if row[0] in nodesnamelist and row[1] in nodesnamelist:
        line = {}
        line["from"] = ip_name_dict[row[0]]
        line["to"] = ip_name_dict[row[1]]
        edgeslist.append(line)

with open("ipServerNewGraph.js","w") as f:
    f.write("var nodes = \n")
    f.write(json.dumps(nodeslist))
    f.write("\n")
    f.write("var edges = \n")
    f.write(json.dumps(edgeslist))
    f.close()

















