#!/usr/bin/eny python
#-*- coding: utf-8 -*-

import urllib
import hashlib

from flask import render_template

from szulabs import app

request_url = "http://www.gravatar.com/avatar/"
default_size = 50
members_email = ['tonyseek@gmail.com', 'chow1937@gmail.com',
                 'gatesanye@gmail.com', 'shonenada@gmail.com', ]


@app.route("/team")
def team():
    members = []
    for email in members_email:
        avatar_url = (request_url + hashlib.md5(email.lower()).hexdigest() +
                      "?" + urllib.urlencode({'s': str(default_size)}))
        members.append({'email': email, 'avatar': avatar_url})
    return render_template("team.html", members=members)
