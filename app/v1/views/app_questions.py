from flask import make_response, jsonify
from flask_restful import Resource, reqparse

from app.v1.models.model_questions import Questions


parser = reqparse.RequestParser()
parser.add_argument('question', required=True, help='type cannot be blank')
parser.add_argument('answerA', required=True, help='type cannot be blank')
parser.add_argument('answerB', required=True, help='type cannot be blank')
parser.add_argument('answerC', required=True, help='type cannot be blank')
parser.add_argument('answerD', required=True, help='type cannot be blank')

class Question(Resource):
    def post(self):
        data = parser.parse_args()
        keys = data.keys()
        for key in keys:
            if not data[key]:
                return {"status": 404, "data": [{"message": "please comment on the incident you would like to report"}]}, 404
        question = Questions(**data)
        question.add_question()
        response = {
            "status": 201,
            "data": [{
                "message":  "Question added to the DB"
            }]
        }

        return make_response(jsonify(response), 201)

    def get(self):
        question = Questions
        all_questions = question.get_all_questions()
        return make_response(jsonify(all_questions), 200)
        


class UniqueQuestion(Resource):
    def get(self, id):
        for question in Questions.get_all_questions():
            if question["id"] == id:
                return make_response(jsonify(question), 200)
        resp = {
            "message": "The answer does not exist"
        }
        return make_response(jsonify(resp), 404)
