#/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
from hashlib import md5

from szulabs.app import db



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
        # FIXME: it's unsafe
        hashed_password = self._hash_password(password, "will-be-removed")
        self.password = hashed_password

    def _hash_password(input, salt):
        hashed_input = md5("<%s|%s>" % input, salt).hexdigest()
        return hashed_input
