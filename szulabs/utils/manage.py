import os.path


def get_config_location(app_root, filename):
    """Create a development configuration if it is not exists."""
    config_location = os.path.join(app_root, filename)
    if not os.path.exists(config_location):
        #: create new empty file if not exists
        open(config_location, "w").close()
    return config_location
