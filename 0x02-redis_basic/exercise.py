#!/usr/bin/env python3
"""
This module contains the Cache class for storing data in Redis.
"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialize a Cache instance, storing a Redis client instance
        and flushing the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.

        Returns:
            str: The randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
