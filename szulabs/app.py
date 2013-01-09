from flask import Flask
from flask.ext.babel import Babel, get_locale
from flask.ext.gears import Gears

from szulabs.assets import setup_assets_compilers, setup_assets_compressors
from szulabs.account.views import account_app
from szulabs.team.views import team_app


#: flask extensions
babel = Babel()
gears = Gears()


def create_app(import_name=None, config=None):
    """Creates an application instance."""
    app = Flask(import_name or __name__)

    #: prepare configuration
    app.config.from_object("szulabs.settings")
    app.config.from_pyfile(config)

    #: initialize extensions
    babel.init_app(app)
    setup_i18n(app)
    gears.init_app(app)
    setup_assets_compilers(app)
    setup_assets_compressors(app)

    #: register blueprints
    app.register_blueprint(account_app)
    app.register_blueprint(team_app)

    return app


def setup_i18n(app):
    """Sets up locale and translation utility."""
    app.context_processor(lambda: {"locale": get_locale().__dict__})
