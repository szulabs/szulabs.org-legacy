from flask import Flask

from szulabs.views.master import master_app
from szulabs.views.people import people_app
from szulabs.views.team import team_app
from szulabs.views.experiments import experiments_app


def create_app(import_name=None, config=None):
    """Creates an application instance."""
    app = Flask(import_name or __name__)

    app.config.from_object("szulabs.settings")
    app.config.from_pyfile(config)

    app.register_blueprint(master_app)
    app.register_blueprint(people_app)
    app.register_blueprint(team_app)
    app.register_blueprint(experiments_app)

    return app
