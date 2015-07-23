#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from flask import Flask
from flask.ext.script import Manager, Server, prompt_bool, Shell
from flask.ext.fixtures import load_fixtures as fixtures_loader, load_fixtures_from_files

from scaffold.app import create_app
from scaffold.extensions import db

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command("runserver", Server())


@manager.shell
def _shell_context():
    return dict(app=manager.app)


@manager.command
def init():
    db.create_all()


@manager.command
def reset():
    db.drop_all()
    db.create_all()


@manager.command
def load_fixtures():
    fixtures_files = ['user.json', 'category.json', 'book.json']
    load_fixtures_from_files(db, fixtures_files)


if __name__ == "__main__":
    manager.run()
