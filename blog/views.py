from flask import Blueprint, redirect, render_template, flash, url_for, request
from . import db
from .models import BlogContent, User, Contact
from flask_login import login_required, login_user, logout_user, current_user


views = Blueprint('views', __name__)


@views.route('/')
def home():
    
    article = BlogContent.query.order_by(BlogContent.date).all()
    return render_template("home.html", user = current_user, articles = article)
    

@views.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        full_name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        new_message = Contact(full_name=full_name, email=email,subject=subject, message=message)
        db.session.add(new_message)
        db.session.commit()
        flash('message sent', category = 'success')
        redirect(url_for('views.contact'))
        
    
    return render_template('contact.html', user = current_user)
    

@views.route('/about')
def about():
    
    return render_template('about.html')
