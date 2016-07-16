#coding=utf-8
import MySQLdb as mysql
import json
from flask.ext.bootstrap import Bootstrap
from flask import Flask, jsonify, render_template, request,json
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
# 主页面
    return render_template("main.html")

@app.route('/add')
def add_numbers():

    data = json.loads(request.args.get("data"))
    print data
    with open("location.json","w") as f:
        f.write(json.dumps(data))
        f.close()
    return json.dumps({"result":"good"})

if __name__=="__main__":
    app.run(host = "0.0.0.0",port = 5000, debug = True)