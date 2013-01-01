#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import render_template
from flask.blueprints import Blueprint


experiments_app = Blueprint("experiments", __name__,
                            template_folder="../templates")


@experiments_app.route("/experiments")
def experiments():
    return render_template("experiments.html")
