from flask import Blueprint, redirect, render_template, flash, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    
    render_template('login.html')
    


@auth.route('/logout')
def logout():
    
    render_template(url_for('login.html'))
    

@auth.route('/sign-up')
def sign_up():
    
    render_template('sign_up.html')
    

@auth.route('/write')
def post():
    
    render_template('posts.html')
    
    

@auth.route('write/edit/<int:id>')
def edit(id):
    
    render_template('edit.html')
    

@auth.route('/write/delete/<int:id>')
def delete(id):
    
    redirect(url_for('auth.post'))
