#!/usr/bin/env python
#-*- coding: utf-8 -*-

import setuptools


metadata = {"name": "SZU Labs",
            "version": "0.0.1",
            "packages": ["szulabs"],
            "author": "Lyd.",
            "author_email": "shonenada@gmail.com",
            "url": "https://github.com/szulabs/szulabs.org/",
            "zip_safe": False,
            "platforms": "any",
            "install_requires": [l.strip() for l in open("requirements.txt", "r")],
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
    setuptools.setup(**metadata)
