from flask import make_response, jsonify
from flask_restful import Resource, reqparse

from app.v1.models.models import Answers


parser = reqparse.RequestParser()
parser.add_argument('answer', required=True, help='type cannot be blank')

class Answer(Resource):
    def post(self):
        data = parser.parse_args()
        keys = data.keys()
        for key in keys:
            if not data[key]:
                return {"status": 404, "data": [{"message": "please comment on the incident you would like to report"}]}, 404
        answer = Answers(**data)
        answer.add_answer()
        response = {
            "status": 201,
            "data": [{
                "message":  "Answer added to the DB"
            }]
        }

        return make_response(jsonify(response), 201)

    def get(self):
        answer = Answers
        all_answer = answer.get_all_answers()
        return make_response(jsonify(all_answer), 200)
        

class UniqueAnswer(Resource):
    def get(self, id):
        for answer in Answers.get_all_answers():
            if answer["id"] == id:
                return make_response(jsonify(answer), 200)
        resp = {
            "message": "The answer does not exist"
        }
        return make_response(jsonify(resp), 404)
