#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
from flask.ext.celery import Celery
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from flask.ext.restful import Api
from flask.ext.login import LoginManager


celery = Celery()
mail = Mail()
db = SQLAlchemy()
cors = CORS(resources={r"/api/*": {"origins": "*"}})
login_manager = LoginManager()
login_manager.session_protection = None  # disable session for restful
api = Api(prefix='/api', catch_all_404s=True)
logger = logging.getLogger('scaffold')
