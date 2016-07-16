#coding

import json


with open("location.json","rw") as f:
    data = f.read()
    circles = json.loads(data)

circles = circles[0]

edges = None
with open("net192to172.json","r") as f:
    edges = json.loads(f.read())["edges"]

net192to172 = {}
nodes = []
for circle in circles:
    node = {}
    node["x"] = circle["__data__"]["x"]
    node["y"] = circle["__data__"]["y"]
    node["opacity"] = circle["__data__"]["opacity"]
    node["name"] = circle["__data__"]["name"]
    node["color"] = circle["__data__"]["color"]
    node["display"] = circle["__data__"]["display"]
    node["fixed"] = "true"
    nodes.append(node)

net192to172["nodes"] = nodes
net192to172["edges"] = edges
with open("net192to172New.json","wr") as f:
    f.write(json.dumps(net192to172))


