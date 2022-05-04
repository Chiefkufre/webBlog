from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = 'hdjds njdj'
    app.config['SESSION_TYPE'] = 'file system'
    
    
    
    return app
