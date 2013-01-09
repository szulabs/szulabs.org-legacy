from flask.ext.babel import Babel, get_locale
from flask.ext.gears import Gears
from flask.ext.sqlalchemy import SQLAlchemy


#: flask extensions
babel = Babel()
gears = Gears()
db = SQLAlchemy()


def setup_i18n(app):
    """Sets up locale and translation utility."""
    app.context_processor(lambda: {"locale": get_locale().__dict__})
