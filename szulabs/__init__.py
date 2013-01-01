#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

from szulabs.views import home
from szulabs.views import experiments
from szulabs.views import people
from szulabs.views import team
