from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_ckeditor import CKEditor


# DB_NAME =  'database.db'

ckeditor = CKEditor()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'hdjds njdj'
    app.config['SESSION_TYPE'] = 'filesystem'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://quhndgozyzmwjb:615fdb6698b586d74a24c659dd67396f7b06c4d47e41faa28e5a77400231242e@ec2-52-4-104-184.compute-1.amazonaws.com:5432/d86porjmrvj6ar'
    db = SQLAlchemy(app)
    app.config['CKEDITOR_PKG_TYPE'] = 'standard'
    # db.init_app(app)
    ckeditor.init_app(app)
    
    # register routes
    from .views import views
    from .auth import auth
    
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from flask_login import LoginManager
    from .models import User, BlogContent, Contact
    
    # calling database
    # create_database(app)
    
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    

    return app

# function to create database in testing environmrnt when called
# def create_database(app):
#     if not path.exists('blog' + DB_NAME):
#         db.create_all(app=app)
#         print('database created!')
    
