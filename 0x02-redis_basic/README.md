# Redis Basic Project

This project is part of the ALX Backend Storage curriculum and demonstrates the basic usage of Redis for caching, tracking, and storing data. The tasks involve implementing functions and decorators to interact with Redis, including tracking method calls, caching results with expiration times, and handling web page requests with caching.

## Project Structure

- **exercise.py**: Contains the `Cache` class with methods for storing and retrieving data from Redis. The methods are enhanced with decorators to count calls and store call history.
- **web.py**: Implements a `get_page` function that retrieves HTML content from a URL, caches it with an expiration time, and tracks the number of times the URL is accessed.
- **test_web.py**: A test script to validate the functionality of the `get_page` function in `web.py`.

## Files

### 1. `exercise.py`

This file contains the implementation of the `Cache` class, which provides methods for storing and retrieving data using Redis. The key features include:

- **Decorators**:
  - `@count_calls`: Tracks the number of times a method is called.
  - `@call_history`: Stores the history of inputs and outputs for a method.

- **Methods**:
  - `store(data)`: Stores the given data in Redis using a randomly generated key.
  - `get(key, fn=None)`: Retrieves data from Redis and optionally applies a conversion function.
  - `get_str(key)`: Retrieves data as a UTF-8 decoded string.
  - `get_int(key)`: Retrieves data as an integer.
  - `replay(method)`: Displays the history of calls for a given method.

### 2. `web.py`

This file contains the implementation of the `get_page` function, which:

- Fetches HTML content from a specified URL.
- Caches the result with a 10-second expiration time.
- Tracks the number of times a particular URL is accessed.

### 3. `test_web.py`

A test script to verify the functionality of the `get_page` function. It includes:

- Fetching content from a URL for the first time.
- Fetching content again to ensure it is retrieved from the cache.
- Waiting for the cache to expire and fetching the content again.

## How to Run

### Prerequisites

- Python 3.7 or higher
- Redis server
- `requests` module
