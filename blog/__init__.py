from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)
    app.secret_key = 'hdjds njdj'
    app.config['SESSION_TYPE'] = 'file system'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    
    
    
    return app
