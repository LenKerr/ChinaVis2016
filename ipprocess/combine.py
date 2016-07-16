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

#print "refer:" + str(len(node1251referServer))
node1251referServer = node1251referServer[:688]
node1251 = list(set(node1251ftpServer).union(set(node1251smtpServer)).union(set(node1251dnsServer)) 
        .union(set(node1251dbServer)).union(set(node1251httpServer)).union(set(node1251fileServer))
        .union(set(node1251unkServer)).union(set(node1251referServer)))

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

#print len(node1231referServer)
node1231referServer = node1231referServer[:658]
node1231 = list(set(node1231ftpServer).union(set(node1231smtpServer)).union(set(node1231dnsServer)) 
        .union(set(node1231dbServer)).union(set(node1231httpServer)).union(set(node1231fileServer))
        .union(set(node1231unkServer)).union(set(node1231referServer)))


unkServer = list(set(node684unkServer).difference(set(node684ftpServer))
        .difference(set(node684smtpServer)).difference(set(node684dnsServer))
        .difference(set(node684dbServer)).difference(set(node684httpServer))
        .difference(set(node684fileServer)))

referServer = list(set(node684referServer))

Server = list(set(node684))


conn = MySQLdb.connect(host = "localhost",port = 3306,user = "root",passwd = "wangjunwei",db = "ChinaVis2016")

cur = conn.cursor()
sql = "select srcip,dstip from `net10andnet10`" 
result = cur.execute(sql)
rows = cur.fetchall()
nodehasedges = set()

for row in rows:
    if row[0] in Server and row[1] in Server:
        nodehasedges.add(row[0])
        nodehasedges.add(row[1])

#684turn
Server = set(Server).intersection(set(nodehasedges))
ftpServer = list(set(node684ftpServer).intersection(set(Server)))
smtpServer = list(set(node684smtpServer).intersection(set(Server)))
dnsServer = list(set(node684dnsServer).intersection(set(Server)))
dbServer = list(set(node684dbServer).intersection(set(Server)))
httpServer = list(set(node684httpServer).intersection(set(Server)))
fileServer = list(set(node684fileServer).intersection(set(Server)))
unkServer = list(set(unkServer).intersection(set(Server)))
referServer = list(set(referServer).difference(set(unkServer)).intersection(set(Server)))

#1251turn
unkServer1251 = list(set(node1251unkServer).difference(set(node1251ftpServer))
        .difference(set(node1251smtpServer)).difference(set(node1251dnsServer))
        .difference(set(node1251dbServer)).difference(set(node1251httpServer))
        .difference(set(node1251fileServer)))
referServer1251 = list(set(node1251referServer).difference(set(unkServer1251)))
Server1251= list(set(node1251))
nodehasedges = set()

for row in rows:
    if row[0] in Server1251 and row[1] in Server1251:
        nodehasedges.add(row[0])
        nodehasedges.add(row[1])
Server1251 = set(Server1251).intersection(set(nodehasedges))
unkServer1251 = list(set(unkServer1251).intersection(set(Server1251)))
referServer1251 = list(set(referServer1251).difference(set(unkServer1251)).intersection(set(Server1251)))    

#print "1231"
#1231turn
unkServer1231 = list(set(node1231unkServer).difference(set(node1231ftpServer))
        .difference(set(node1231smtpServer)).difference(set(node1231dnsServer))
        .difference(set(node1231dbServer)).difference(set(node1231httpServer))
        .difference(set(node1231fileServer)))
referServer1231 = list(set(node1231referServer).difference(set(unkServer1231)))
Server1231= list(set(node1231))
nodehasedges = set()

for row in rows:
    if row[0] in Server1231 and row[1] in Server1231:
        nodehasedges.add(row[0])
        nodehasedges.add(row[1])
Server1231 = set(Server1231).intersection(set(nodehasedges))
unkServer1231 = list(set(unkServer1231).intersection(set(Server1231)))
referServer1231 = list(set(referServer1231).difference(set(unkServer1231)).intersection(set(Server1231)))    


Server = list(set(Server).union(set(Server1251)).union(set(Server1231)))
ftpServer = list(set(node684ftpServer).intersection(set(Server)))
smtpServer = list(set(node684smtpServer).intersection(set(Server)))
dnsServer = list(set(node684dnsServer).intersection(set(Server)))
dbServer = list(set(node684dbServer).intersection(set(Server)))
httpServer = list(set(node684httpServer).intersection(set(Server)))
fileServer = list(set(node684fileServer).intersection(set(Server)))
unkServer = list(set(unkServer).union(set(unkServer1231)).union(set(unkServer1251)))
unkServer = list(set(unkServer).difference(set(ftpServer))
        .difference(set(smtpServer)).difference(set(dnsServer))
        .difference(set(dbServer)).difference(set(httpServer))
        .difference(set(fileServer)))
referServer = list(set(referServer).union(set(referServer1251)).union(set(referServer1231)).difference(set(unkServer)))

Server.remove("10.79.105.230")
Server.remove("10.67.220.248")
unkServer.remove("10.79.105.230")
referServer.remove("10.67.220.248")
print unkServer
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
    if each != "10.79.105.230":
        ip = {}
        ip["name"] = each
        ip["group"] = 7
        ips.append(ip)
for each in referServer:
    if each != "10.67.220.248":
        ip = {}
        ip["name"] = each
        ip["group"] = 8
        ips.append(ip)
print len(ips)

with open('ipServerNew.json','w') as f:
    f.write(json.dumps(ips))
