from flask import Flask


def create_app(import_name=None, config=None):
    """Creates an application instance."""
    app = Flask(import_name or __name__)
    app.config.from_object("szulabs.settings")
    app.config.from_pyfile(config)
    return app
