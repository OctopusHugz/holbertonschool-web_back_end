#!/usr/bin/env python3
""" This module creates a top_students function """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    pipeline = [
        {"$unwind": {"path": "$topics"}},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(pipeline)
