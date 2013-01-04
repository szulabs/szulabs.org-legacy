#!/usr/bin/env python
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages


install_requires = [l.strip() for l in open("requirements.txt", "r")]


metadata = {"name": "SZU Labs",
            "version": "0.0.1",
            "packages": find_packages(),
            "author": "Lyd.",
            "author_email": "shonenada@gmail.com",
            "url": "https://github.com/szulabs/szulabs.org/",
            "zip_safe": False,
            "platforms": "any",
            "package_data": {"templates": ["*.html"],
                             "assets": ["*.jpg", "*.png", "*.css", "*.less",
                                        "*.js", "*.coffee", "favicon.ico"]},
            "install_requires": install_requires,
            "description": "A laboratory of StuCampus in SZU."}


if __name__ == "__main__":
    setup(**metadata)
