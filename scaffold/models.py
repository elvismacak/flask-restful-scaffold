#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import time

from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    mail = db.Column(db.String(64), nullable=False, unique=True)
    token = db.Column(db.String(64), nullable=False)
    description = db.Column(db.TEXT)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.TEXT)
    cate_id = db.Column(db.Integer, db.ForeignKey("category.id"))

    category = db.relationship("Category", uselist=False)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)


del db
