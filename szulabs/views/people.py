#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import render_template

from szulabs import app


@app.route("/people/<username>")
def people(username):
    return render_template("people/" + username + ".html")
