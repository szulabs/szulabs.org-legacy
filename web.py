#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado
import json
from datetime import date, datetime

httperror = tornado.web.HTTPError
asynchronous = tornado.web.asynchronous
auth = tornado.web.authenticated

''' make json able to encode datetime '''
def __default(obj):
	if isinstance(obj, datetime):
		return obj.strftime('%Y-%m-%d %H:%M:%S')
	elif isinstance(obj, date):
		return obj.strftime('%Y-%m-%d')
	else:
		raise TypeError('%r is not JSON serializable' % obj)

def json_encode(o):
	return json.dumps(o, default=__default)

class Controller( tornado.web.RequestHandler ):
    
    def get(self):
    	self.render("errors/404.html")

    def post(self):
    	self.render("errors/404.html")


