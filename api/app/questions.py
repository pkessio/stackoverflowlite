from flask import Flask,request
from flask import request , jsonify, json
from flask import Resource
#from flask_restful import Api,requestparse
from api.app.models import Questions
from app import app


app = Flask(__name__)
api = Api(app)
question = []

def home():

     return jsonify({"endpoints":[
         {'Get all questions': "/api/questions/all GET"},
         {'Get all questions': "/api/v1/question GET"}
         ]})

#get all questions

api.add_resource(question, '/api/questions/all', methods=['GET'])
def get_all_questions():
        return jsonify({"Questions": question.questions}), 200





#get a specific question 

api.add_resource(get_question_id, '/api/questions/id',methods=['GET'])
def get_question_id(id):
        for quest in question.questions:
            if id == quest["question_id"]:
                return jsonify({"message": "Question found", "Question": quest}), 200
        return jsonify({"message": "Question not found"}), 404


#adding one question
api.add_resource(get_question_id, '/api/answer',methods=["POST"])
class post_single_question(Resource):
    def post(self, question_id):
         request_data = request.get_json()
         question_id = str(len(question.questions) + 1)
         title = request_data["title"] 


if __name__ == '__main__':
    app.run(debug=True)


