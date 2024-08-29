#!/usr/bin/env python3
"""
This module contains the Cache class for storing and retrieving data in Redis,
along with decorators for counting method calls and storing call history.
"""

import redis
import uuid
import functools
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a method is called.
    The count is stored in Redis using the method's qualified name as the key.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that increments
        the call count each time the method is called.
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator that stores the
    history of inputs and outputs for a method in Redis.
    The inputs are stored in a list with the key "<method.__qualname__>:inputs"
    The outputs are stored in
    a list with the key "<method.__qualname__>:outputs"
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function that stores inputs and outputs in Redis.
        """
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store the input arguments in the inputs list
        self._redis.rpush(input_key, str(args))

        # Execute the original function and store the output
        result = method(self, *args, **kwargs)

        # Store the output in the outputs list
        self._redis.rpush(output_key, str(result))

        return result

    return wrapper


class Cache:
    def __init__(self):
        """
        Initialize a Cache instance, storing a Redis client instance
        and flushing the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
            Optional[int]: The retrieved dat
            a converted to an integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)
