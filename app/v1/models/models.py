
from flask_sqlalchemy import SQLAlchemy 
import json

db = SQLAlchemy()

class Answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String, nullable= False)

    def __init__(self, answer):
        self.answer = answer

    def json_maker(self):
        return {'id': self.id, 'answer': self.answer}

    def __repr__(self):
        book_object = {
            'id' : self.id,
            'answer' : self.answer
            }
        return json.dumps(book_object)

    
   
    def add_answer(self):
        new_answer = Answers(self.answer)
        db.session.add(new_answer)
        db.session.commit()

    @staticmethod
    def get_a_answer(_id):
        return Answers.query.filter_by(_id=id).first()

    @staticmethod
    def get_all_answers():
        return [Answers.json_maker(answer) for answer in Answers.query.all()]