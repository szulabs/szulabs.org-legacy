#!/usr/bin/eny python
#-*- coding: utf-8 -*-

import urllib
import hashlib

from flask import render_template
from flask.blueprints import Blueprint

from szulabs.services import people


team_app = Blueprint("team", __name__, template_folder="../templates")


request_url = "http://www.gravatar.com/avatar/"
default_size = 50


@team_app.route("/team")
def team():
    members = []
    team_members = people.get_members()
    for member in team_members:
        avatar_url = (request_url + hashlib.md5(member.email.lower())
        	          .hexdigest() + "?" + urllib
        	          .urlencode({'s': str(default_size)}))
        members.append({'email': member.email, 'avatar': avatar_url, 
        	            'nickname': member.nickname, 'id':member.id})
    return render_template("team.html", members=members)
