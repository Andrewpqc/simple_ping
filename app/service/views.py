from flask import jsonify,Response
from . import service
from app.models import Requirement,PingInfo
from manage import command_360,command_vivo,command_baidu
from app import db
import json

@service.route('/simpleping')
def index():
    a=[]
    pinginfos=PingInfo.query.all()
    for pinginfo in pinginfos:
        temp={}
        if pinginfo.company==2:
            temp["company"]="百度"
        elif pinginfo.company==3:
            temp["company"]="奇虎306"
        elif pinginfo.company==4:
            temp["company"]="Vivo"

        if pinginfo.category==1:
            temp["category"]="技术"
        elif pinginfo.category==2:
            temp["category"]="产品"
        elif pinginfo.category==3:
            temp["category"]="设计"
        elif pinginfo.category==4:
            temp["category"]="市场"

        if pinginfo.pingType==0:
            temp["pingType"]="实习生招聘"
        elif pinginfo.pingType==1:
            temp["pingType"]="校园招聘"

        temp["jobTitle"]=pinginfo.jobTitle
        temp["time"]=pinginfo.time
        temp["location"]=pinginfo.location
        temp["link"]=pinginfo.link
        temp["email"]=pinginfo.email
        temp["requirements"]=[]
        for req in pinginfo.requirements:
            temp["requirements"].append(req.text)
        a.append(temp)
    return Response(json.dumps(a),mimetype="application/json")

@service.route("/flush")
def flush():
    try:
        db.drop_all()
        db.create_all()
        command_baidu()
        command_360()
        command_vivo()
    except Exception as e:
        print(e)
        return "ERROR"
    else:
        return "OK"






