#coding

import json


with open("location.json","rw") as f:
    data = f.read()
    circles = json.loads(data)

Xmin = 0
Xmax = 0
Ymin = 0
Ymax = 0
for each in circles:
    if int(each["x"])<Xmin:
        Xmin = int(each["x"])
    if int(each["x"])>Xmax:
        Xmax = int(each["x"])
    if int(each["y"])<Ymin:
        Ymin = int(each["y"])
    if int(each["y"])>Ymax:
        Ymax = int(each["y"])
print Xmin,Xmax,Ymin,Ymax
for each in circles:
    each["x"] = str(10+(int(each["x"]-Xmin)/(22734.0)*570*7))
    each["y"] = str(10+(int(each["y"]-Ymin)/(44802.0)*1108*7))
#print circles

edges = None
with open("ipServerNewGraph.json","r") as f:
    edges = json.loads(f.read())["edges"]

nodesdictlist = None
with open("ipServerNew.json","rw") as f:
    nodesdictlist = json.loads(f.read())

net10to10  = {}
nodes = []
index = 0
for each in nodesdictlist:
    node = {}
    node["x"] = circles[index]["y"]
    node["y"] = circles[index]["x"]
    index = index +1
    node["opacity"] = 0.4
    node["name"] = each["name"]
    
    #if each["group"] == 1:
    #    node["color"] = "#ff7f0e"
    #elif each["group"] == 2:
    #    node["color"] = "#2ca02c"
    #elif each["group"] == 3:
    #    node["color"] = "#d62728"
    #elif each["group"] == 4:
    #    node["color"] = "#9467bd"
    #elif each["group"] == 5:
    #    node["color"] = "#8c564b"
    #elif each["group"] == 6:
    #    node["color"] = "#e377c2"
    #elif each["group"] == 7:
    #    node["color"] = "#7f7f7f"
    #elif each["group"] == 8:
    #    node["color"] = "#bcbd22" 
    
    node["display"] = "show"
    #node["fixed"] = "true"
    nodes.append(node)

net10to10["nodes"] = nodes
net10to10["edges"] = edges
with open("net10to10New.json","wr") as f:
    f.write(json.dumps(net10to10))

#print edges
nodeslist = []
dict_index = 0
name_id_index = {}
for each in nodesdictlist:
    node = {}
    node["id"] = dict_index
    name_id_index[each["name"]] = dict_index
    node["label"] = each["name"]
    node["group"] = each["group"]
    #if each["group"] == 1:
    #    node["color"] = "rgba(230,103,175,0.5)"
    #elif each["group"] == 2:
    #    node["color"] = "rgba(83,15,173,0.5)"
    #elif each["group"] == 3:
    #    node["color"] = "rgba(207,249,62,0.5)"
    #elif each["group"] == 4:
    #    node["color"] = "rgba(255,168,7,0.5)"
    #elif each["group"] == 5:
    #    node["color"] = "rgba(255,0,0,0.5)"
    #elif each["group"] == 6:
    #    node["color"] = "rgba(0,255,0,0,5)"
    #elif each["group"] == 7:
    #    node["color"] = "rgba(255,255,0,0.5)"
    #elif each["group"] == 8:
    #    node["color"] = "rgba(0,0,255,0.5)" 

    #node["color"]= "rgba(0,0,255,0.3)"
    node["x"] = circles[dict_index]["y"]
    node["y"] = circles[dict_index]["x"]
    node["fixed"] = "true"
    node["value"] = "30"
    dict_index = dict_index +1
    nodeslist.append(node)

edgeslist = []
for each in edges:
    line = {}
    line["from"] = each["source"]
    line["to"] = each["target"]
    crowdlist = ["10.18.112.26","10.18.112.242","10.18.112.244","10.18.112.246","10.18.112.247",
            "10.19.112.246","10.33.216.221","10.33.219.246","10.39.216.247","10.46.236.221",
            "10.39.216.247","10.50.112.246","10.54.216.221","10.67.216.221","10.114.218.221",
            "10.116.217.221","10.118.216.221","10.145.216.221","10.146.216.221"]
    crowdlistindex = []
    for each in crowdlist:
        crowdlistindex.append(name_id_index[each])
    if line["from"] in crowdlistindex or line["to"] in crowdlistindex:
        line["color"] = "rgba(0,108,81,0.1)"
    else:
        line["color"] = "rgba(0,108,81,0.5)"
    edgeslist.append(line)

with open("net10to10New.js","wr") as f:
    f.write("var nodes = \n")
    f.write(json.dumps(nodeslist))
    f.write("\n")
    f.write("var edges = \n")
    f.write(json.dumps(edgeslist))
    f.close()













