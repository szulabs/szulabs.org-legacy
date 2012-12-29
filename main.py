#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web

from szulabs.controller.home import HomeHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler)]
        settings = dict(title=u"Szu Laboratory.",
                        template_path=os.path.join(
                            os.path.dirname(__file__),
                            "template"),
                        static_path=os.path.join(
                            os.path.dirname(__file__),
                            "static"),
                        xsrf_cookies=True,
                        cookie_secret="vnozin1623Y&RSxznoin2oiw4&/w512zv=",
                        login_url="/auth/login",
                        autoscape=None,
                        debug=False)
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    http_server = tornado.httpserver.HTTPServer(
        Application(),
        xheaders=True)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
