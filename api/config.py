# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
