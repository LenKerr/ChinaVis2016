from flask import Flask, jsonify, render_template, request
import json

app=Flask(__name__)
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='POST':
        data = json.loads(request.form.get('data'))
        ss = data['value']
        print ss
        n=[request.form.get(x,"default") for x in{'n1','n2','n3'}]
        print n
        n= request.get_json(silent = False)
        print n
        n= request.data()
        print n
        return jsonify(max=max(n),min=min(n))
    else:
        return render_template('ajaxtest.html')

if __name__=='__main__':
    app.run()