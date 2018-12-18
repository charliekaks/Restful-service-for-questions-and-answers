"""App module: sets the configuration for the flask application"""

# Third party imports
from flask import Flask
from instance.config import config
from app.v1 import v1
from app.v1.models.model_questions import db
from app.v1.models.models import db as d

def create_app(config_name="development"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config['development'])
    app.config.from_pyfile('config.py')
    app.register_blueprint(v1)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/charles/answer-2/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    d.init_app(app)
    db.init_app(app)
    with app.test_request_context():
        db.create_all()
        d.create_all()
    return app