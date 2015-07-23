#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from sqlalchemy import or_
from flask import current_app
from flask.ext.login import current_user, login_required
from flask.ext.restful import Resource, reqparse, abort, marshal_with

from extensions import db, logger
import models
import marshals
import utils


class Resource(Resource):
    method_decorators = [login_required]


class UserListAPI(Resource):

    @marshal_with(marshals.user_fields, envelope='result')
    def get(self):
        return current_user


class BookListAPI(Resource):
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('name', required=True)
    post_parser.add_argument('cate_id', type=int, required=True)
    post_parser.add_argument('description', required=False)

    @marshal_with(marshals.book_fields, envelope='result')
    def get(self):
        return models.Book.query.all()

    @marshal_with(marshals.book_fields, envelope='result')
    def post(self):
        args = self.post_parser.parse_args()

        book = models.Book()
        for attr, value in args.iteritems():
            if value is not None:
                book.__setattr__(attr, value)
        db.session.add(book)
        db.session.commit()
        return book


class BookAPI(Resource):
    put_parser = reqparse.RequestParser()
    put_parser.add_argument('name', required=False)
    put_parser.add_argument('cate_id', required=False)
    put_parser.add_argument('description', required=False)

    @marshal_with(marshals.book_fields, envelope='result')
    def get(self, book_id):
        book = models.Book.query.filter_by(id=book_id).scalar()
        if not book:
            abort(404)
        return book

    @marshal_with(marshals.book_fields, envelope='result')
    def delete(self, book_id):
        book = models.Book.query.filter_by(id=book_id).scalar()
        if not book:
            abort(404)
        db.session.delete(book)
        return book

    @marshal_with(marshals.book_fields, envelope='result')
    def put(self, book_id):
        args = self.put_parser.parse_args()

        book = models.Book.query.filter_by(id=book_id).scalar()
        if not book:
            abort(404)

        for attr, value in args.iteritems():
            if value is not None:
                book.__setattr__(attr, value)
        db.session.commit()
        return book


class CategoryListAPI(Resource):
    post_parser = reqparse.RequestParser()
    post_parser.add_argument('name', required=True)

    @marshal_with(marshals.category_fields, envelope='result')
    def get(self):
        return models.Category.query.all()

    @marshal_with(marshals.category_fields, envelope='result')
    def post(self):
        args = self.post_parser.parse_args()

        category = models.Category()
        for attr, value in args.iteritems():
            if value is not None:
                category.__setattr__(attr, value)
        db.session.add(category)
        db.session.commit()
        return category
