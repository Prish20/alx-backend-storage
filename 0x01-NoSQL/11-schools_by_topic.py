#!/usr/bin/env python3
"""
Script to find schools with a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    :param mongo_collection: The pymongo collection object
    :param topic: The topic searched for in the schools' topics
    :return: A list of schools having the specific topic
    """
    return list(mongo_collection.find({ "topics": topic }))
