#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import render_template

from szulabs import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/contactus")
def contactus():
    return render_template("contactus.html")


@app.route("/joinus")
def joinus():
    return render_template("joinus.html")
