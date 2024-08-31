#!/usr/bin/env python3
"""
Script to insert a new document in a MongoDB collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    :param mongo_collection: The pymongo collection object
    :param kwargs: Keyword arguments representing the document fields
    :return: The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
