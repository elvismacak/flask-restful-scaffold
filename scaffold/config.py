#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Config(object):

    DEBUG = False
    TESTING = False

    # flask-restful
    ERROR_404_HELP = False

    # flask-fixtures
    FIXTURES_DIRS = ['fixtures']

    # flask-login
    AUTH_HEADER_NAME = 'Token'

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'mysql://user:passwd@host/dbname?charset=utf8'

    # log
    LOGGER_LEVEL = 'info'
    LOGGER_PATH = '/var/log/restful-scaffold'
    LOGGER_FILE = 'restful-scaffold.log'

    # flask-mail
    MAIL_SERVER = 'mail-server.com'
    MAIL_PORT = 25
    MAIL_USERNAME = 'user'
    MAIL_PASSWORD = 'passwd'
    MAIL_DEFAULT_SENDER = 'test@example.com'

    # celery
    CELERY_DEFAULT_EXCHANGE = 'restful-scaffold'
    CELERY_DEFAULT_EXCHANGE_TYPE = "direct"
    CELERY_DEFAULT_QUEUE = 'restful-scaffold-report'
    CELERY_DEFAULT_ROUTING_KEY = 'restful-scaffold-report'
    CELERY_TIMEZONE = 'UTC'
    CELERY_ENABLE_UTC = True
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACKS_LATE = True
    CELERY_BROKER_URL = 'amqp://user:passwd@host:5672//'
    CELERY_RESULT_BACKEND = 'db+mysql://user:passwd@host/dbname?charset=utf8'


class DevConfig(Config):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

    LOGGER_LEVEL = 'debug'
    LOGGER_PATH = '/tmp'

    MAIL_DEFAULT_SENDER = 'test-dev@example.com'

    CELERY_BROKER_URL = 'amqp://user:passwd@host:5672//'
    CELERY_RESULT_BACKEND = 'db+mysql://user:passwd@host/dbname?charset=utf8'


class TestConfig(Config):

    DEBUG = True
    TESTING = True

    FIXTURES_DIRS = ['fixtures', 'test/fixtures']

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

    LOGGER_LEVEL = 'debug'
    LOGGER_PATH = '/tmp'

    MAIL_DEFAULT_SENDER = 'test-test@example.com'

    CELERY_BROKER_URL = 'amqp://user:passwd@host:5672//'
    CELERY_RESULT_BACKEND = 'db+mysql://user:passwd@host/dbname?charset=utf8'
