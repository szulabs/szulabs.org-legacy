#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import render_template
from flask.blueprints import Blueprint


people_app = Blueprint("people", __name__, template_folder="../templates")


@people_app.route("/people/<username>")
def people(username):
    return render_template("people/" + username + ".html")
