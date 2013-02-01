#/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime
from hashlib import md5

from szulabs.extensions import db

from szulabs.settings import SALT


class People(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(32))
    nickname = db.Column(db.String(16))
    truename = db.Column(db.String(5))
    created = db.Column(db.DateTime)
    
    __salt__ = SALT

    def __init__(self, email):
        self.email = email
        self.created = datetime.utcnow()

    def setNickname(self, nickname):
        self.nickname = nickname

    def setTruename(self, truename):
        self.truename = truename

    def setPassword(self, password):
        hashed_password = self.__hash_password(password, self.__salt__)
        self.password = hashed_password

    def __hash_password(input, salt):
        hashed_input = md5("<%s|%s>" % input, salt).hexdigest()
        return hashed_input

    def __repr__(self):
        return "<Email %r>" % self.email
