#coding=utf-8
import MySQLdb
import json
import os

conn = MySQLdb.connect(host = "localhost", port = 3306, user = "root", passwd = "wangjunwei", db ="ChinaVis2016")

cur = conn.cursor()
result = cur.execute("select ip from `net10andnet10node`")
rows = cur.fetchall()

ip_name_dict = {}
dict_index = 0
with open("10and10Nodes.csv","w") as f:
    f.write("Id,Label,Modularity Class\n")
    for row in rows:
        f.write(str(dict_index)+","+row[0]+",0\n")
        ip_name_dict[row[0]] = dict_index
        dict_index = dict_index+1

result = cur.execute("select srcip,dstip,cnum from `net10andnet10`")
rows = cur.fetchall()
line_index = 0
with open("10and10Edges.csv","w") as f:
    f.write("Source,Target,Type,Id,Label,Weight\n")
    for row in rows:
        f.write(str(ip_name_dict[row[0]])+","+str(ip_name_dict[row[1]])+",Directed,"+str(line_index)+
                ",,"+str(row[2])+"\n")
        line_index = line_index+1





