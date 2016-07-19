#coding=utf-8

import MySQLdb as mysql
import json
from flask import Flask,request,render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = mysql.connect(host = "localhost",port = 3306, user = "root", passwd = "wangjunwei" ,db = "ChinaVis2016")
db.autocommit(True)

c = db.cursor()

#对主页的访问分为请求页面的get请求和提交数据的post请求
@app.route("/",methods=["GET","POST"])
def hello():
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render_template("chinavis.html")

@app.route("/datalocation",methods=["GET","POST"])
def getdatalocation():
    data = json.loads(request.args.get("data"))
    with open("location.json","w") as f:
        f.write(json.dumps(data))
    return json.dumps({"result":"good"})

@app.route("/datavcp",methods=["GET"])
def getvcpdata():
    vp = request.args.get('vp', 0, type=int)
    vc = request.args.get('vc', 0, type=int)
    ones = []
    c.execute("select time,filelen,rpc,exe,picture,rtfs,rars,htmls,cs,\
            filelen-rpc-exe-picture-rtfs-rars-htmls-cs as unknown from vcptype where VPI1 ="+str(vp)+" and VCI1 ="+str(vc))
    raws = c.fetchall()
    for j in range(1,10):
        one = []
        for raw in raws:
            one.append([raw[0]+8*3600000,raw[j]])
        ones.append(one)
    #return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))
    #callback方法把json对象
    return json.dumps(ones)

@app.route("/flowip",methods=["GET"])
def getflowipdata():
    c.execute("select time,sum(flow) from flowip group by time order by time")
    ones = [[i[0]+8*3600000,int(i[1])] for i in c.fetchall()]
    return json.dumps(ones)

@app.route("/vcptime",methods=["GET"])
def getvcptimedata():
    sql = "select vpi1,vci1 from vcptype group by vpi1,vci1"
    c.execute(sql)
    raws = c.fetchall()
    ones = []
    for raw in raws:
        c.execute("select time,filelen from vcptype where vpi1 = "+str(raw[0])+" and vci1 = "+str(raw[1])+" order by timeid,VPI1,VCI1")
        one = [[i[0]+8*3600000,i[1]] for i in c.fetchall()]
        ones.append(one)
    c.execute("select time,sum(flow) from flowip group by time order by time")
    ones.append([[i[0]+8*3600000,int(i[1])] for i in c.fetchall()])
    return json.dumps(ones)

@app.route("/ipsdistributewithtime",methods=["GET"])
def ipsdistributedata():
    time = request.args.get("time")
    sql = "select srcid as id from ((select srcid from flowip where time = "+ str(time)+\
        ") union (select dstipid from flowip where time = "+str(time)+" )) a"
    print sql
    c.execute(sql)
    ones = [i[0] for i in c.fetchall()]
    #print ones
    return json.dumps(ones)

@app.route("/ipsdistributewithperiod",methods=["GET"])
def ipsdistributewithperiod():
    starttime = request.args.get("starttime")
    stoptime = request.args.get("stoptime")
    sql = "select srcid as id from ((select srcid from flowip where time >= "+ str(starttime)+\
        " and time <= "+str(stoptime)+") union (select dstipid from flowip where time >= "+str(starttime)+" and time <= "+str(stoptime)+" )) a"
    print sql
    c.execute(sql)
    ones = [i[0] for i in c.fetchall()]
    #print ones
    return json.dumps(ones)

@app.route("/getserverflow",methods=["GET"])
def getserverflow():
    sql = "select starttimeunix*1000,fcount from traffic1"
    c.execute(sql)
    ones = [[i[0]+8*3600000,i[1]] for i in c.fetchall()]
    return json.dumps(ones)

if __name__ == "__main__":
    app.run(debug = True)

