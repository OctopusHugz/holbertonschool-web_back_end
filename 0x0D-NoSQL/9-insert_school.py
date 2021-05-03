#!/usr/bin/env python3
""" This module creates an insert_school function """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based on kwargs """
    new_doc = {}
    for k, v in kwargs.items():
        new_doc[k] = v
    new_insert = mongo_collection.insert_one(new_doc)
    return new_insert.inserted_id
