#!/usr/bin/env python

import os.path

from flask.ext.script import Manager

from szulabs.app import create_app
from szulabs.utils.manage import get_config_location


app_root = os.path.dirname(os.path.realpath(__file__))
app_config = "app.conf"

app = create_app("szulabs.app", get_config_location(app_root, app_config))
manager = Manager(app)


if __name__ == "__main__":
    manager.run()
