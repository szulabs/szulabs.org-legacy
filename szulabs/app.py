from flask import Flask

from szulabs.extensions import babel, bcrypt, gears, login_manager, db
from szulabs.extensions import (setup_i18n, setup_assets_compilers,
                                setup_assets_compressors, setup_database)
from szulabs.account.views import account_app
from szulabs.team.views import team_app


def create_app(import_name=None, config=None):
    """Creates an application instance."""
    app = Flask(import_name or __name__)

    #: prepare configuration
    app.config.from_object("szulabs.settings")
    app.config.from_pyfile(config)

    #: initialize extensions
    babel.init_app(app)
    bcrypt.init_app(app)
    setup_i18n(app)
    gears.init_app(app)
    setup_assets_compilers(app)
    setup_assets_compressors(app)
    login_manager.init_app(app)
    db.init_app(app)
    setup_database(app)

    #: register blueprints
    app.register_blueprint(account_app)
    app.register_blueprint(team_app)

    return app
