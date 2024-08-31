#!/usr/bin/env python3
"""
Script to list all documents in a MongoDB collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection
    :param mongo_collection: The pymongo collection object
    :return: A list of documents or an empty list if none are found
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
