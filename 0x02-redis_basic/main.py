#!/usr/bin/env python3
"""
Main file to test the Cache class and the replay function.
"""

from exercise import Cache, replay

def main():
    cache = Cache()

    # Store some data
    cache.store("foo")
    cache.store("bar")
    cache.store(42)

    # Replay the history of store calls
    replay(cache.store)

if __name__ == "__main__":
    main()
