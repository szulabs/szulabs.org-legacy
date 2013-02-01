#/usr/bin/env python

from szulabs.extensions import db


class Experiment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    description = db.Column(db.Text)
    author = db.Column(db.String(100)) # format: [author1_id, author2_id, ...]
    url = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Name %r>" % self.name
