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
            return redirect(url_for("auth.login"))
            
    return render_template('sign_up.html', user= current_user)
    

@auth.route('/write', methods=['GET','POST'])
@login_required
def write():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')
        
        if len(title) < 1:
            flash('You forgot to write a title', category='error')
        elif len(content) < 1:
            flash('You can\'t make an empty post', category='error')
            return redirect(url_for('auth.write'))
        
        else:
            new_content = BlogContent(title=title, author=author, content=content)
            db.session.add(new_content)
            db.session.commit()
            flash('Post submit. Go to home to see your new post', category='success')
            return redirect(url_for('auth.write'))
        
    article = BlogContent.query.order_by(BlogContent.date).all()
    return render_template('posts.html', user=current_user, articles = article)
    
    

@auth.route('write/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    post = BlogContent.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.author = request.form.get('author')
        post.content = request.form.get('content')
        db.session.commit()
        flash('Article updated', category='success')
        return redirect('/write')
    
    return render_template('edit.html', post=post)
    

@auth.route('/write/delete/<int:id>')
def delete(id):
    post = BlogContent.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('Article deleted', category='success')
    return redirect('/write')
    
