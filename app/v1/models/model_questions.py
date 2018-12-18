
from flask_sqlalchemy import SQLAlchemy 
import json
db = SQLAlchemy()



class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable= False)
    answerA = db.Column(db.String, nullable= False)
    answerB = db.Column(db.String, nullable= False)
    answerC = db.Column(db.String, nullable= False)
    answerD = db.Column(db.String, nullable= False)

    def json_maker(self):
        return {'id': self.id, 'question': self.question, "answerA": self.answerA, "answerB":self.answerB, "answerC":self.answerC, "answerD":self.answerD}

   
    def __init__(self, question, answerA, answerB, answerC, answerD):
        self.question = question
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.answerD = answerD


    def __repr__(self):
        question_object = {
            'id' : self.id,
            'question' : self.question,
            'answerA' : self.answerA,
            'answerB' : self.answerB,
            'answerC' : self.answerC,
            'answerD' : self.answerD
            }
        return json.dumps(question_object)

    
   
    def add_question(self):
        new_question = Questions(self.question,self.answerA,self.answerB, self.answerC, self.answerD)
        db.session.add(new_question)
        db.session.commit()

    @staticmethod
    def get_a_question(_id):
        return Questions.query.filter_by(_id=id).first()

    @staticmethod
    def get_all_questions():
        return [Questions.json_maker(question) for question in Questions.query.all()]