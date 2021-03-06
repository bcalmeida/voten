from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
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

# Routes
@app.route('/')
def index():
    # To avoid caching on the browser. Useful for development
    # return make_response(open('templates/index.html').read())
    return send_file("templates/index.html")


###########################
## RESTful API endpoints ##
###########################
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

    resp = jsonify({'poll': poll_json})
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/poll', methods=['POST'])
def create_poll():
    # Check if POST data has a json
    # TODO: Use request.get_json and catch exception
    new_poll_json = request.json
    if new_poll_json is None:
        abort(400)

    # Check input
    # TODO: Refactor input arguments checking
    if 'description' not in new_poll_json:
        abort(400)
    if 'candidates' not in new_poll_json:
        abort(400)

    # Create new poll and add it to the db
    new_poll = Poll(new_poll_json['description'])
    db.session.add(new_poll)
    db.session.commit()

    # Create corresponding candidates and add it to the db
    for new_candidate_json in new_poll_json['candidates']:
        new_candidate = Candidate(new_candidate_json['description'], new_poll.id)
        db.session.add(new_candidate)
    db.session.commit()

    # Return 201, HTTP code for 'Created'
    return jsonify({'poll_id': new_poll.id}), 201

@app.route('/poll/<int:poll_id>', methods=['POST'])
def vote_on_poll(poll_id):
    # Check if POST data has a json
    # TODO: Use request.get_json and catch exception
    vote_json = request.json
    if vote_json is None:
        abort(400)

    # Check input
    if 'candidate_description' not in vote_json:
        abort(400)

    # Update candidate with said description, in this poll
    candidates = db.session.query(Candidate).filter_by(poll_id=poll_id).all()
    for candidate in candidates:
        if candidate.description == vote_json['candidate_description']:
            candidate.votes += 1
            db.session.commit()
            return ('', 200)

    # Said candidate is not present in this poll
    abort(400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.after_request
def add_cors(resp):
    """ Ensure all responses have the CORS headers. This ensures any failures are also accessible
        by the client. """
    resp.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin','*')
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET'
    resp.headers['Access-Control-Allow-Headers'] = request.headers.get(
        'Access-Control-Request-Headers', 'Authorization' )
    return resp

# Start server
if __name__ == '__main__':
    app.run()
