from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db


# Models for the polls
# Poll-Candidate relationship is one-to-many, like User-Post
class Poll(db.Model):

    __tablename__ = "polls"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    candidates = relationship("Candidate", backref="poll")

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<poll: %s>' % self.description


class Candidate(db.Model):

    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    votes = db.Column(db.Integer, nullable=False)
    poll_id = db.Column(db.Integer, ForeignKey('polls.id'))

    def __init__(self, description, poll_id):
        self.description = description
        self.votes = 0
        self.poll_id = poll_id

    def __repr__(self):
        return '<candidate: %s>' % self.description


# Old models, used for users and posts
class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return "<title: %s --- description: %s>" % (self.title, self.description)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<user: %s>' % self.name

