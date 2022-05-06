from flask import Blueprint, redirect, render_template, flash, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import BlogContent, User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password or username, try again', category='error')
        else:
            flash('Email does not exist', category='error')
    
    return render_template('login.html',user = current_user)
    


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template(url_for('login.html'))
    

@auth.route('/sign-up')
def sign_up():
    
    return render_template('sign_up.html')
    

@auth.route('/write')
def post():
    
    return render_template('posts.html')
    
    

@auth.route('write/edit/<int:id>')
def edit(id):
    
    return render_template('edit.html')
    

@auth.route('/write/delete/<int:id>')
def delete(id):
    
    return redirect(url_for('auth.post'))
