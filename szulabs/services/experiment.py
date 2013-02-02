#/usr/bin/env python
#-*- coding: utf-8 -*-

from szulabs.models.experiment import Experiment


def get_experiments():
    experiments = Experiment.query.all()
    return experiments


def parse_authors_string(raw_string):
    """Parse raw string in database to a list"""
    command = "authors_list = " + raw_string
    exec(command)
    return authors_list
