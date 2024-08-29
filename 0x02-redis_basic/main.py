#!/usr/bin/env python3
"""
Main file to test the Cache class, call_history, and count_calls decorators.
"""

from exercise import Cache

def main():
    cache = Cache()

    # Store some data and check the inputs and outputs stored in Redis
    s1 = cache.store("first")
    print(s1)
    s2 = cache.store("secont")
    print(s2)
    s3 = cache.store("third")
    print(s3)

    inputs = cache._redis.lrange(f"{cache.store.__qualname__}:inputs", 0, -1)
    outputs = cache._redis.lrange(f"{cache.store.__qualname__}:outputs", 0, -1)

    print("inputs: {}".format(inputs))
    print("outputs: {}".format(outputs))

if __name__ == "__main__":
    main()
