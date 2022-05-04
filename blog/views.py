from flask import Blueprint, redirect, render_template, flash, url_for


views = Blueprint('views', __name__)


@views.route('/')
def home():
    
    render_template('home.html')
    

@views.route('/contact')
def contact():
    
    render_template('contact.html')
    

@views.route('/about')
def about():
    
    render_template('about.html')
