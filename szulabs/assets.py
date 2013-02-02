from gears.compressors import SlimItCompressor, CSSMinCompressor
from gears_coffeescript import CoffeeScriptCompiler


compilers = {
    ".coffee": CoffeeScriptCompiler.as_handler()
}

compressors = {
    "text/css": CSSMinCompressor.as_handler(),
    "application/javascript": SlimItCompressor.as_handler()
}


gears_environment = lambda app: app.extensions["gears"]["environment"]
gears_environment.__doc__ = """Gets gears environments of the app instance."""


def setup_assets_compilers(app):
    """Set up compilers of assets."""
    env = gears_environment(app)
    for extension, compiler in compilers.iteritems():
        env.compilers.register(extension, compiler)


def setup_assets_compressors(app):
    """Set up compressors of assets."""
    env = gears_environment(app)
    #: turn off for debug but turn on for testing
    if not app.config["DEBUG"] or app.config["TESTING"]:
        for mimetype, compressor in compressors.iteritems():
            env.compressors.register(mimetype, compressor)
