from flask import Flask,request
from flask import request , jsonify, json
from flask import Resource
from flask_restful import Api,requestparse
from app.models import Questions
from app.models import Answer
from app import app


app = Flask(__name__)
api = Api(app)
answer = Answer('title', 'content')

def home():

     return jsonify({"endpoints":[
         {'Get all questions': "/api/v1/question GET"},
         {'Get all questions': "/api/v1/question/answer GET"}
         ]})




if __name__ == '__main__':
    app.run(debug=True)