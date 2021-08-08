from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_migrate import Migrate

login_manager = LoginManager()
login_manager.login_view = 'main.login'

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__) 
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    #injections de dépendance
    migrate = Migrate(app, db)
    db.init_app(app)
    # attach routes and custom error pages here

    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint)

    from .agent import agent as agent_blueprint 
    app.register_blueprint(agent_blueprint)

    from .customer import customer as customer_blueprint 
    app.register_blueprint(customer_blueprint)


    login_manager.init_app(app) 

    return app
