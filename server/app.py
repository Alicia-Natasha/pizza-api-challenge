from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from server import models 
from server.models import db

from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp


def create_app():

    
    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)
    CORS(app)

    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)
    @app.route('/')
    def index():
            return {'message': 'Welcome to the Pizza API!'}
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555)
