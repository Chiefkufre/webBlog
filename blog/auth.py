from flask import Blueprint, redirect, render_template, flash, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import BlogContent, User
from . import db

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
    

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('account already exist, please login', category='error')
        elif len(email) < 4:
            flash('email must be longer than four characters', category='error')
        elif len(password1) < 7:
            flash('password must be longer than seven characters', category='error')
        elif password1 != password2:
            flash('password don\'t match. Please check and try again', category='error')
        else:
            new_user = User(full_name=full_name, email=email,password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('account created successfully. Please login in', category='success')
            return redirect(url_for(auth.login))
            
    return render_template('sign_up.html', user= current_user)
    

@auth.route('/write')
def post():
    
    return render_template('posts.html')
    
    

@auth.route('write/edit/<int:id>')
def edit(id):
    
    return render_template('edit.html')
    

@auth.route('/write/delete/<int:id>')
def delete(id):
    
    return redirect(url_for('auth.post'))
