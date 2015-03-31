from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask import jsonify, abort, make_response
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps
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

## RESTful API endpoints ##
@app.route('/poll/<int:poll_id>', methods=['GET'])
def get_poll(poll_id):
    poll = db.session.query(Poll).filter_by(id=poll_id).first()
    if poll is None:
        abort(404)

    candidates = db.session.query(Candidate).filter_by(poll_id=poll_id).all()
    candidates_jsons = [{'description': candidate.description, 'votes': candidate.votes} for candidate in candidates]

    poll_json = {
        'description': poll.description,
        'candidates': candidates_jsons
    }

    return jsonify({'poll': poll_json})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

# Start server
if __name__ == '__main__':
    app.run()
