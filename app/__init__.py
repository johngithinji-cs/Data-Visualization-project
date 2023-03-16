#!/usr/bin/env python3
"""
Initializes our flask application
"""

from flask import Flask
from flask_login import LoginManager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(sessionmaker(autocimmit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def create_app():
    """
    Initialise flask and register blueprints
    """
    app = Flask(__name__)

    login_manager = LoginManager()
    # redirect url when a user attempts to access a login_required endpoint without
    # being logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        """callback used to reload the user object from the user ID
        stored in the session
        """
        return User.query.get(int(user_id))
    
    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Create the database
    Base.metadata.create_all(bind=engine)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
