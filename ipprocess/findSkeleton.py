#coding=utf-8
import MySQLdb
from random import choice
import json

ftpServer = ["10.18.112.26","10.52.148.111","10.65.216.226"]
smtpServer = ["10.18.112.114","10.67.220.229"]
dnsServer = ["10.18.112.246","10.18.112.247","10.24.158.248"]
dbServer = ["10.24.249.221","10.52.140.45","10.54.240.17"]
httpServer = ["10.18.17.106","10.18.112.113","10.18.112.213","10.18.112.222",
    "10.20.1.31","10.20.1.207","10.20.4.11","10.20.11.20","10.20.16.53","10.20.111.101",
    "10.20.111.105","10.22.0.10","10.22.0.22","10.22.0.190","10.22.137.240","10.24.249.230",
    "10.46.48.1","10.52.1.41","10.52.63.80"]
fileServer = ["10.18.112.30","10.18.248.242",
        "10.24.248.253","10.24.249.125","10.24.249.225","10.24.249.227","10.33.216.221",
        "10.33.219.246","10.37.216.221","10.39.216.247","10.46.236.221","10.54.216.221",
        "10.67.216.221","10.67.220.221","10.114.216.221","10.114.218.221",
        "10.114.219.221","10.116.160.247","10.116.160.248","10.116.217.221","10.118.161.1",
        "10.118.161.2","10.118.161.3","10.118.165.199","10.118.216.221","10.145.216.221",
        "10.146.216.221"]
referServer = ["10.65.216.31","10.65.216.48","10.65.216.146","10.65.216.221","10.65.216.113",
        "10.67.220.1","10.67.220.52","10.67.220.71","10.67.220.105","10.67.220.109",
        "10.67.220.110","10.67.220.147"]
unkServer = []
Server = []
Server.extend(ftpServer),Server.extend(smtpServer),Server.extend(dnsServer),Server.extend(dbServer)
Server.extend(httpServer),Server.extend(fileServer)
Server.extend(referServer)
#print tuple(Server)

conn = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="wangjunwei",db ="ChinaVis2016")
cur = conn.cursor()

#result = cur.execute("select dstip from `rpcServer` where srcip in "+str(tuple(Server))+\
#        " group by dstip having count(distinct srcip)>=10 order by sum(filelen) desc limit 20")
#rows = cur.fetchall()
#print rows


result = cur.execute("select ip from `net10andnet10nodeDraw*`")
rows = cur.fetchall()

allNodeList =[]

for row in rows:
    allNodeList.append(row[0])
#print allNodeList
#print len(allNodeList)


result = cur.execute("select srcip,dstip from `net10andnet10`")
rows = cur.fetchall()

allEdgeList =[]

for row in rows:
    allEdgeList.append(tuple([row[0],row[1]]))
#for i in range(10):
#    print allEdgeList[i]

result = cur.execute("select ip from net10iporderbyconnect")
rows = cur.fetchall()

ipOrderByCon =[]
for row in rows:
    ipOrderByCon.append(row[0])
ipOrderIndex = 0#insert index


restList = list(set(allNodeList)-set(Server))
#print len(set(restList))
origin = len(set(restList))
complete = 0.9

def neighborNode(node,server):
    for eachNode in server:
        if tuple([node,eachNode]) in allEdgeList or tuple([eachNode,node]) in allEdgeList:
            return True
    return False

def isServer(node):
    result = cur.execute("select count(*) as c,sum(filelen) as f from `rpcServer` where srcip ='"+node+\
            "' having c >400 and f > 2595616*2")
    if result <= 0:
        return False
    else:
        rows = cur.fetchall()
        filelen = rows[0][1]
        result = cur.execute("select sum(filelen) as flow from rawdataall where dstip like '"+node+"' group by DSTPORT having flow > 0.1*"+str(filelen))
        if result <= 0:
            return False
    return True

while len(restList) > len(allNodeList)*(1-complete):
    randomNode = choice(restList) 
    if randomNode in Server:
        restList.remove(randomNode)
    else:
        if neighborNode(randomNode,Server): 
            restList.remove(randomNode)
        else:
            toAddIsServer = False
            while ipOrderByCon[ipOrderIndex] in Server or neighborNode(ipOrderByCon[ipOrderIndex],Server):
                toAddIsServer = isServer(ipOrderByCon[ipOrderIndex])
                if toAddIsServer:
                    break
                ipOrderIndex = ipOrderIndex + 1 
            Server.append(ipOrderByCon[ipOrderIndex])
            if toAddIsServer:
                unkServer.append(ipOrderByCon[ipOrderIndex])
            else:
                referServer.append(ipOrderByCon[ipOrderIndex])
            ipOrderIndex = ipOrderIndex + 1
            print "Server:"+str(len(Server))+"\t"+"rest:"+str(len(restList)-int(len(allNodeList)*(1-complete)))+\
                    "\t"+"complete:"+str(("%.2f" % (100*(origin-len(restList))/(origin-(len(allNodeList)*(1-complete))))))+\
                    "%"+"\t"+"unkServer:"+str(len(unkServer))

print len(Server)

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

with open('ipServer.json','w') as f:
    f.write(json.dumps(ips))
