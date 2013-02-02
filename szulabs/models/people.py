#/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
from hashlib import md5

from szulabs.extensions import db


class People(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(32))
    nickname = db.Column(db.String(16))
    truename = db.Column(db.String(5))
    created = db.Column(db.DateTime)


    def __init__(self, email):
        self.email = email
        self.created = datetime.utcnow()

    def change_password(self, password):
        """TODO: change the 2nd password to a dynamic salt"""
        hashed_password = self.hash_password(password, password)
        self.password = hashed_password

    def hash_password(input, salt):
        hashed_input = md5("<%s|%s>" % input, salt).hexdigest()
        return hashed_input

    def __repr__(self):
        return "<Email %r>" % self.email
