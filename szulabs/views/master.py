#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import render_template
from flask.blueprints import Blueprint


master_app = Blueprint("master", __name__, template_folder="../templates")


@master_app.route("/")
def home():
    return render_template("index.html")


@master_app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@master_app.route("/contactus")
def contactus():
    return render_template("contactus.html")


@master_app.route("/joinus")
def joinus():
    return render_template("joinus.html")
