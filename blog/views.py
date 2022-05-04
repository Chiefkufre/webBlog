from flask import Blueprint, redirect, render_template, flash, url_for


views = Blueprint('views', __name__)


@views.route('/')
def home():
    
    return render_template("home.html")
    

@views.route('/contact')
def contact():
    
    return render_template('contact.html')
    

@views.route('/about')
def about():
    
    return render_template('about.html')
