#/usr/bin/env python
#-*- coding: utf-8 -*-

from szulabs.models.people import People


def get_members():
    members = People.query.all()
    return members
