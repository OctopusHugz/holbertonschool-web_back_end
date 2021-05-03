#!/usr/bin/env python3
""" This module creates a list_all function """


def list_all(mongo_collection):
    """ Lists all documents in a collection """
    count = mongo_collection.count()
    if count == 0:
        return []
    all_documents = mongo_collection.find()
    return all_documents
