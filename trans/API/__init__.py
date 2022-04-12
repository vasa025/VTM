from flask import Flask
from flask_restful import Resource, reqparse, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)

from API.getTransDetails import GetTransdata
from API.getUserDetails import GetUserData


api.add_resource(GetTransdata,"/getTransDetails")
api.add_resource(GetUserData,"/getUserDetails")

