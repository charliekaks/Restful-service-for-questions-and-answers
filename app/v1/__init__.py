from flask import Blueprint
from flask_restful import Api
from .views.app_answers import Answer, UniqueAnswer
from .views.app_questions import Question, UniqueQuestion


v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

api.add_resource(Answer, '/answers')
api.add_resource(UniqueAnswer, '/answers/<int:id>')
api.add_resource(Question, '/questions')
api.add_resource(UniqueQuestion, '/questions/<int:id>')
