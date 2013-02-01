#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import render_template
from flask.blueprints import Blueprint

from szulabs.services import experiment


experiments_app = Blueprint("experiments", __name__,
                            template_folder="../templates")


@experiments_app.route("/experiments")
def experiments():
    experiments = experiment.get_experiments()
    return render_template("experiments.html", experiments=experiments)
