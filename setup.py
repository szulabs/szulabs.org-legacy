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
            "package_dir": {"templates": "szulabs/templates",
                            "assets": "szulabs/assets"},
            "package_data": {"templates": ["*.html", "people/*.html"],
                              "assets": ["images/*.jpg", "images/*.png",
                                         "styles/*.css", "styles/*.less",
                                         "scripts/*.js", "scripts/*.coffee",
                                         "favicon.ico"]},
            "install_requires": install_requires,
            "description": "A laboratory of StuCampus in SZU.",
            "classifiers": ["Programming Language :: Python",
                            "Operating System :: OS Independent",
                            "Environment :: Web Environment",
                            "Framework :: Flask",
                            "Topic :: Internet :: WWW/HTTP",
                            "Topic :: Internet :: WWW/HTTP :: WSGI"
                            ]
            }


if __name__ == "__main__":
    setup(**metadata)
