#!/usr/bin/env python3
""" This module creates a top_students function """


def top_students(mongo_collection):
    """ Returns all students sorted by average score """
    # avg_scores = {}
    # all_docs = mongo_collection.find()
    # for doc in all_docs:
    #     name = doc.get("name")
    #     topics = [topic for topic in doc.get("topics")]
    #     scores = [topic.get("score") for topic in topics]
    #     avg_scores[name] = sum(scores) / len(scores)
    # print(avg_scores)

    pipeline = [{"$unwind": {"path": "$topics"}}, {"$group": {
        "_id": "$_id", "name": {"$first": "$name"}, "averageScore": {"$avg": "$topics.score"}}}, {"$sort": {"averageScore": -1}}]
    avg_scores = mongo_collection.aggregate(pipeline)
    return avg_scores
