#!/usr/bin/env python3
"""
This module contains the Cache class for storing and retrieving data in Redis.
"""

import redis
import uuid
from typing import Callable, Optional, Union


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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str,
                                                    bytes, int, float, None]:
        """
        Retrieve data from Redis,
        optionally converting it using the provided function.

        Args:
            key (str): The key to retrieve data for.
            fn (Optional[Callable]): A function to apply to the retrieved data.

        Returns:
            Union[str, bytes, int,
            float, None]: The retrieved data, possibly transformed by fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 decoded string.

        Args:
            key (str): The key to retrieve data for.

        Returns:
            Optional[str]: The retrieved
            data decoded as a string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer.

        Args:
            key (str): The key to retrieve data for.

        Returns:
            Optional[int]: The retrieved data converted to an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)
