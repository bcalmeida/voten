from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
#import sqlite3
import os

# Create the application object
app = Flask(__name__)

# Config
app.config.from_object(os.environ['APP_SETTINGS'])

# Create the SQLAlchemy object
db = SQLAlchemy(app)

# Import db schema
from models import *

# Login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# Routes
@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != "admin" or request.form['password'] != "admin":
            error = "Invalid credentials. Please try again."
        else:
            session['logged_in'] = True
            flash("You were just logged in!")
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You were just logged out!")
    return redirect(url_for('welcome'))

# Connect to the database
# Returns the connection object
# def connect_db():
#     return sqlite3.connect(app.database)

# Start server
if __name__ == '__main__':
    app.run()
