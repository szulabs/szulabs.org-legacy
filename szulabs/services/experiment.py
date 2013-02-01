#/usr/bin/env python
#-*- coding: utf-8 -*-

from szulabs.models.experiment import Experiment


def get_experiments():
	experiments = Experiment.query.all()
	return experiments
