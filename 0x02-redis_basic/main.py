#!/usr/bin/env python3
"""
Main file to test the Cache class.
"""

import redis
from exercise import Cache


def main():
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))


if __name__ == "__main__":
    main()
