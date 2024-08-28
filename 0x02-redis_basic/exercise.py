#!/usr/bin/env python3
"""
This module contains the Cache class for storing and retrieving data in Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


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
        Retrieve data from Redis
        and optionally convert it using the provided function.

        Args:
            key (str): The key to retrieve from Redis.
            fn (Optional[Callable])
            : A function to convert the data to the desired type.

        Returns:
            Union[str, bytes, int,
            float, None]: The retrieved data or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis and convert it to a UTF-8 string.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            Optional[str]: The retrieve
            d string or None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            Optional[int]: The retrieved
            integer or None if the key does not exist.
        """
        return self.get(key, int)


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs of a method.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = "{}:inputs".format(method.__qualname__)
        output_key = "{}:outputs".format(method.__qualname__)

        # Store input arguments as strings in Redis
        self._redis.rpush(input_key, str(args))

        # Call the actual method
        result = method(self, *args, **kwargs)

        # Store the result in Redis
        self._redis.rpush(output_key, result)

        return result

    return wrapper


# Apply the decorator to the store method
Cache.store = call_history(Cache.store)
