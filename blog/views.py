from flask import Blueprint, redirect, render_template, flash, url_for, request
from . import db
from .models import BlogContent, User, Contact


views = Blueprint('views', __name__)


@views.route('/')
def home():
    
    return render_template("home.html")
    

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
        
    
    return render_template('contact.html')
    

@views.route('/about')
def about():
    
    return render_template('about.html')
