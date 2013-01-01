from gears.compressors import SlimItCompressor, CSSMinCompressor
from gears_coffeescript import CoffeeScriptCompiler
from gears_less import LESSCompiler


_compilers = {
    ".coffee": CoffeeScriptCompiler.as_handler(),
    ".less": LESSCompiler.as_handler()
}

_compressors = {
    "text/css": CSSMinCompressor.as_handler(),
    "application/javascript": SlimItCompressor.as_handler()
}


gears_environment = lambda app: app.extensions["gears"]["environment"]
gears_environment.__doc__ = """Gets gears environments of the app instance."""


def setup_assets_compilers(app):
    """Set up compilers of assets."""
    env = gears_environment(app)
    for extension, compiler in _compilers.iteritems():
        env.compilers.register(extension, compiler)


def setup_assets_compressors(app):
    """Set up compressors of assets."""
    env = gears_environment(app)
    if not app.config["DEBUG"] or app.config["TESTING"]:
        #: turn off for debug but turn on for testing
        for mimetype, compressor in _compressors.iteritems():
            env.compressors.register(mimetype, compressor)
