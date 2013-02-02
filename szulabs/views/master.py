#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import render_template
from flask.blueprints import Blueprint

from szulabs import texts


master_app = Blueprint("master", __name__, template_folder="../templates")


@master_app.route("/")
def home():
    return render_template("index.html", content=texts.home)


@master_app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html", content=texts.aboutus)


@master_app.route("/contactus")
def contactus():
    return render_template("contactus.html", content=texts.contactus)


@master_app.route("/joinus")
def joinus():
    return render_template("joinus.html", content=texts.joinus)
