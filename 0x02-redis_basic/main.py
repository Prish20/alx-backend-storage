#!/usr/bin/env python3
"""
Main file to test the Cache class and the count_calls decorator.
"""

from exercise import Cache

def main():
    cache = Cache()

    # Store some data and check the call count
    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))  # Should print b'1'

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))  # Should print b'3'

if __name__ == "__main__":
    main()
