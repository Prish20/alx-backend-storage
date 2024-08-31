#!/usr/bin/env python3
"""
Script to update topics in a MongoDB document
"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    :param mongo_collection: The pymongo collection object
    :param name: The school name to update
    :param topics: The list of topics approached in the school
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
