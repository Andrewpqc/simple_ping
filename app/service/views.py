from flask import jsonify
from . import service
from app.models import Requirement,PingInfo
from app import db

@service.route('/')
def index(id):
    pass




