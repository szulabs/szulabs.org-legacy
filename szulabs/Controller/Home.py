#!/usr/bin/env python
#-*- coding: utf-8 -*-

from web import Controller

class HomeHandler(Controller):
	def get(self):
		self.render('home/home.html')