import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from flask_mail import Mail
from flask_migrate import Migrate
from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError
import time

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()

def create_db_engine_with_retry(db_url, max_retries=3, retry_interval=5):
    for attempt in range(max_retries):
        try:
            engine = create_engine(db_url, poolclass=QueuePool, pool_size=10, max_overflow=20)
            # Test the connection
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return engine
        except SQLAlchemyError as e:
            if attempt < max_retries - 1:
                print(f"Database connection attempt {attempt + 1} failed. Retrying in {retry_interval} seconds...")
                time.sleep(retry_interval)
            else:
                raise e

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    
    # Mail configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')
    
    # Create the database engine with retry logic
    engine = create_db_engine_with_retry(app.config["SQLALCHEMY_DATABASE_URI"])
    db.init_app(app)
    
    # Set the custom engine for SQLAlchemy
    app.config['SQLALCHEMY_ENGINE'] = engine

    login_manager.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    login_manager.login_view = 'auth.login'

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    from wishlist import wishlist as wishlist_blueprint
    app.register_blueprint(wishlist_blueprint)

    @app.route('/')
    def index():
        return render_template('base.html')

    return app
