#!/usr/bin/env python3
"""
Script to return all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    :param mongo_collection: The pymongo collection object
    :return: A list of students sorted by average score,
    each with an 'averageScore' key
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
