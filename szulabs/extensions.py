from flask.ext.babel import Babel, get_locale
from flask.ext.bcrypt import Bcrypt
from flask.ext.gears import Gears
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from gears.compressors import SlimItCompressor, CSSMinCompressor
from gears_coffeescript import CoffeeScriptCompiler


# ----------------
# Flask Extensions
# ----------------

babel = Babel()
bcrypt = Bcrypt()
gears = Gears()
login_manager = LoginManager()
db = SQLAlchemy()


# -------------
# i18n and l10n
# -------------

def setup_i18n(app):
    """Sets up locale and translation utility."""
    app.context_processor(lambda: {"locale": get_locale().__dict__})


# ------------------
# Assets Managements
# ------------------

assets_compilers = {
    ".coffee": CoffeeScriptCompiler.as_handler()
}

assets_compressors = {
    "text/css": CSSMinCompressor.as_handler(),
    "application/javascript": SlimItCompressor.as_handler()
}


def gears_environment(app):
    """Gets gears environments of the app instance."""
    return app.extensions["gears"]["environment"]


def setup_assets_compilers(app):
    """Set up compilers of assets."""
    env = gears_environment(app)
    for extension, compiler in assets_compilers.iteritems():
        env.compilers.register(extension, compiler)


def setup_assets_compressors(app):
    """Set up compressors of assets."""
    env = gears_environment(app)
    #: turn off for debug mode but turn on for testing mode
    if not app.config["DEBUG"] or app.config["TESTING"]:
        for mimetype, compressor in assets_compressors.iteritems():
            env.compressors.register(mimetype, compressor)
