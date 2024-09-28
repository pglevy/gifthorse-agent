import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    @app.route('/')
    def index():
        return render_template('base.html')

    with app.app_context():
        db.create_all()

    return app
