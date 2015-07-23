#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import logging


from flask import Flask, current_app
from flask.ext.restful import abort

from extensions import celery, db, cors, login_manager, api, logger
from models import User
import restful
import utils
import config


@login_manager.header_loader
def load_user(token):
    user = User.query.filter_by(token=token).scalar()

    if not user:
        abort(401)

    return user


def init_logger(app):
    logger.propagate = False

    level_string = app.config['LOGGER_LEVEL'].upper()
    log_level = getattr(logging, level_string, None)
    logger.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(filename)s@%(lineno)d - %(levelname)s - %(message)s')

    log_dir = app.config['LOGGER_PATH']
    log_file = app.config['LOGGER_FILE']
    log_file = os.path.join(log_dir, log_file)

    file_logger = logging.FileHandler(log_file)
    file_logger.setLevel(logging.DEBUG)
    file_logger.setFormatter(formatter)
    logger.addHandler(file_logger)


def init_api(api, app):
    api.app = app
    api.add_resource(restful.UserListAPI, '/user')  # GET

    api.add_resource(restful.BookListAPI, '/book')  # GET, POST
    api.add_resource(restful.BookAPI, '/book/<book_id>')  # GET, PUT, DELETE

    api.add_resource(restful.CategoryListAPI, '/category')  # GET


def create_app(config=None):
    app = Flask('scaffold', instance_relative_config=True)
    if config is not None:
        app.config.from_object(config)

    init_logger(app)
    logger.info('starting %s' % app.name)
    db.init_app(app)
    cors.init_app(app)
    celery.config_from_object(app.config)
    login_manager.init_app(app)
    api.init_app(app)
    init_api(api, app)
    logger.info('started %s' % app.name)

    return app
