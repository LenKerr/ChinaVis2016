#coding=utf-8
import json
import MySQLdb
from collections import defaultdict

jsonstr = ""
with open("ipServer684.json","rw") as f:
    for row in f:
        jsonstr = jsonstr +row

nodes684dictlist = json.loads(jsonstr)

node684ftpServer = []
node684smtpServer = []
node684dnsServer = []
node684dbServer = []
node684httpServer = []
node684fileServer = []
node684unkServer = []
node684referServer = []
node684 = []

for each in nodes684dictlist:
    node684.append(each["name"])
    if each["group"] ==1:
        node684ftpServer.append(each["name"])
    elif each["group"] ==2:
        node684smtpServer.append(each["name"])
    elif each["group"] ==3:
        node684dnsServer.append(each["name"])
    elif each["group"] ==4:
        node684dbServer.append(each["name"])
    elif each["group"] ==5:
        node684httpServer.append(each["name"])
    elif each["group"] ==6:
        node684fileServer.append(each["name"])
    elif each["group"] ==7:
        node684unkServer.append(each["name"])
    elif each["group"] ==8:
        node684referServer.append(each["name"])
    
jsonstr = ""
with open("ipServer1251.json","rw") as f:
    for row in f:
        jsonstr = jsonstr +row

nodes1251dictlist = json.loads(jsonstr)

node1251ftpServer = []
node1251smtpServer = []
node1251dnsServer = []
node1251dbServer = []
node1251httpServer = []
node1251fileServer = []
node1251unkServer = []
node1251referServer = []
node1251 = []

for each in nodes1251dictlist:
    node1251.append(each["name"])
    if each["group"] ==1:
        node1251ftpServer.append(each["name"])
    elif each["group"] ==2:
        node1251smtpServer.append(each["name"])
    elif each["group"] ==3:
        node1251dnsServer.append(each["name"])
    elif each["group"] ==4:
        node1251dbServer.append(each["name"])
    elif each["group"] ==5:
        node1251httpServer.append(each["name"])
    elif each["group"] ==6:
        node1251fileServer.append(each["name"])
    elif each["group"] ==7:
        node1251unkServer.append(each["name"])
    elif each["group"] ==8:
        node1251referServer.append(each["name"])
 
jsonstr = ""
with open("ipServer.json","rw") as f:
    for row in f:
        jsonstr = jsonstr +row

nodes1231dictlist = json.loads(jsonstr)

node1231ftpServer = []
node1231smtpServer = []
node1231dnsServer = []
node1231dbServer = []
node1231httpServer = []
node1231fileServer = []
node1231unkServer = []
node1231referServer = []
node1231 = []

for each in nodes1231dictlist:
    node1231.append(each["name"])
    if each["group"] ==1:
        node1231ftpServer.append(each["name"])
    elif each["group"] ==2:
        node1231smtpServer.append(each["name"])
    elif each["group"] ==3:
        node1231dnsServer.append(each["name"])
    elif each["group"] ==4:
        node1231dbServer.append(each["name"])
    elif each["group"] ==5:
        node1231httpServer.append(each["name"])
    elif each["group"] ==6:
        node1231fileServer.append(each["name"])
    elif each["group"] ==7:
        node1231unkServer.append(each["name"])
    elif each["group"] ==8:
        node1231referServer.append(each["name"])
 
#print len(node684unkServer)
#print len(node1251unkServer)
#print len(node1231unkServer)

unkServer = list(set(node684unkServer).union(set(node1251unkServer)))
unkServer = list(set(unkServer).union(set(node1231unkServer)))
#print len(unkServer)

referServer = list(set(node684referServer).union(set(node1251referServer)))
referServer = list(set(referServer).union(set(node1231referServer)))
#print len(referServer)

Server = list(set(node684).union(set(node1231)))
Server = list(set(Server).union(set(node1251)))
#print len(Server)

Server2 = list(set(node684ftpServer).union(set(node684smtpServer)))
Server2 = list(set(Server2).union(set(node684dnsServer)))
Server2 = list(set(Server2).union(set(node684dbServer)))
Server2 = list(set(Server2).union(set(node684httpServer)))
Server2 = list(set(Server2).union(set(node684fileServer)))
Server2 = list(set(Server2).union(set(unkServer)))
Server2 = list(set(Server2).union(set(referServer)))
#print len(Server2)
#print len(node684ftpServer)
#print len(node684smtpServer)
#print len(node684dnsServer)
#print len(node684dbServer)
#print len(node684httpServer)
#print len(node684fileServer)
#print len(unkServer)
#print len(referServer)
#print len(set(unkServer).union(set(referServer)))#has intersect

conn = MySQLdb.connect(host = "localhost",port = 3306,user = "root",passwd = "wangjunwei",db = "ChinaVis2016")

cur = conn.cursor()
#sql = "select srcip from rpcServer where srcip in ("
#for i in range(len(Server)):
#    if i < len(Server)-1:
#        sql = sql + "'"+str(Server[i])+"',"
#    else:
#        sql = sql + "'"+str(Server[i])+"') and dstip in ("
#for i in range(len(Server)):
#    if i < len(Server)-1:
#        sql = sql + "'"+str(Server[i])+"',"
#    else:
#        sql = sql + "'"+str(Server[i])+"')"
#
##print sql/ over the len that mysql could execute
sql = "select srcip,dstip from `net10andnet10`" 
result = cur.execute(sql)
rows = cur.fetchall()
nodehasedges = set()

#print len(set(Server))
#print len(set(referServer).intersection(set(unkServer)))
for row in rows:
    if row[0] in Server and row[1] in Server:
        nodehasedges.add(row[0])
        nodehasedges.add(row[1])

#print len(nodehasedges)

Server = set(Server).intersection(set(nodehasedges))
ftpServer = list(set(node684ftpServer).intersection(set(Server)))
smtpServer = list(set(node684smtpServer).intersection(set(Server)))
dnsServer = list(set(node684dnsServer).intersection(set(Server)))
dbServer = list(set(node684dbServer).intersection(set(Server)))
httpServer = list(set(node684httpServer).intersection(set(Server)))
fileServer = list(set(node684fileServer).intersection(set(Server)))
unkServer = list(set(unkServer).intersection(set(Server)))
referServer = list(set(referServer).difference(set(unkServer)).intersection(set(Server)))

print len(set(ftpServer).intersection(unkServer))
print len(set(smtpServer).intersection(unkServer))
print len(set(dnsServer).intersection(unkServer))
print len(set(dbServer).intersection(unkServer))
print len(set(httpServer).intersection(unkServer))
print len(set(fileServer).intersection(unkServer))

print len(Server),len(ftpServer),len(smtpServer),len(dnsServer),len(dbServer),len(httpServer),len(fileServer),len(unkServer),len(referServer)

ips = []
for each in ftpServer: 
    ip = {}
    ip["name"] = each
    ip["group"] = 1 
    ips.append(ip)
for each in smtpServer:
    ip = {}
    ip["name"] = each
    ip["group"] = 2
    ips.append(ip)
for each in dnsServer:
    ip = {}
    ip["name"] = each
    ip["group"] = 3
    ips.append(ip)
for each in dbServer:
    ip = {}
    ip["name"] = each
    ip["group"] = 4
    ips.append(ip)
for each in httpServer:
    ip = {}
    ip["name"] = each
    ip["group"] = 5
    ips.append(ip)
for each in fileServer:
    ip = {}
    ip["name"] = each
    ip["group"] = 6
    ips.append(ip)
for each in unkServer:
    ip = {}
    ip["name"] = each
    ip["group"] = 7
    ips.append(ip)
for each in referServer:
    ip = {}
    ip["name"] = each
    ip["group"] = 8
    ips.append(ip)

with open('ipServerNew.json','w') as f:
    f.write(json.dumps(ips))
