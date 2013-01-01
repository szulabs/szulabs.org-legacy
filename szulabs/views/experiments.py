#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import render_template

from szulabs import app


@app.route("/experiments")
def experiments():
    return render_template("experiments.html")
