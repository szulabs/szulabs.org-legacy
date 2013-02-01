#!/usr/bin/env python

import os.path

from flask.ext.script import Manager

from szulabs.app import create_app
from szulabs.extensions import db
from szulabs.context import create_category_db
from szulabs.utils.manage import get_config_location


app_root = os.path.dirname(os.path.realpath(__file__))
app_config = "app.conf"

app = create_app("szulabs.app", get_config_location(app_root, app_config))
manager = Manager(app)


@manager.command
def initdb():
    """Initialize database."""
    db.create_all()
    create_category_db()


if __name__ == "__main__":
    manager.run()
