#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask.ext.restful import fields


user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'mail': fields.String,
    'description': fields.String,
}

book_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'cate_id': fields.Integer,
    'category': fields.String(attribute=lambda x: x.category.name),
    'description': fields.String,
}

category_fields = {
    'id': fields.Integer,
    'name': fields.String,
}
