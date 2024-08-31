# 0x01. NoSQL

## Task 0: List All Databases

This task involves creating a script to list all databases in MongoDB.

**File:** `0-list_databases`

**Usage:**

The script can be executed with the following command:

```bash
cat 0-list_databases | mongo
```

### Task 1: Create or Use a Database

This task involves creating a script to create or switch to a database named `my_db` in MongoDB.

**File:** `1-use_or_create_database`

**Usage:**

The script can be executed with the following command:

```bash
cat 1-use_or_create_database | mongo
```

## Task 2: Insert Document

This task involves creating a script to insert a document into the `school` collection in the `my_db` database.

**File:** `2-insert`

**Usage:**

The script can be executed with the following command:

```bash
cat 2-insert | mongo my_db
```

## Task 3: List All Documents

This task involves creating a script to list all documents in the `school` collection within the `my_db` database.

**File:** `3-all`

**Usage:**

The script can be executed with the following command:

```bash
cat 3-all | mongo my_db
```

## Task 4: List All Matches

This task involves creating a script to list all documents in the `school` collection within the `my_db` database where the `name` field is `"Holberton school"`.

**File:** `4-match`

**Usage:**

The script can be executed with the following command:

```bash
cat 4-match | mongo my_db
```

## Task 5: Count Documents

This task involves creating a script to count the number of documents in the `school` collection within the `my_db` database.

**File:** `5-count`

**Usage:**

The script can be executed with the following command:

```bash
cat 5-count | mongo my_db
```

## Task 6: Update Document

This task involves creating a script to update documents in the `school` collection within the `my_db` database by adding an `address` field to documents where the `name` field is `"Holberton school"`.

**File:** `6-update`

**Usage:**

The script can be executed with the following command:

```bash
cat 6-update | mongo my_db
```

### Task 7: Delete by Match

This task involves creating a script to delete documents in the `school` collection within the `my_db` database where the `name` field is `"Holberton school"`.

**File:** `7-delete`

**Usage:**

The script can be executed with the following command:

```bash
cat 7-delete | mongo my_db
```

### Task 8: List All Documents in Python

This task involves writing a Python function that lists all documents in a MongoDB collection. The function should return an empty list if no documents are found.

**File:** `8-all.py`
**File:** `8-main.py`

**Function Prototype:**

```python
def list_all(mongo_collection):
    """
    Lists all documents in a collection
    :param mongo_collection: The pymongo collection object
    :return: A list of documents or an empty list if none are found
    """
```

**Usage:**

```python
./8-main.py
```

## Task 9: Insert a Document in Python

This task involves writing a Python function that inserts a new document into a MongoDB collection using keyword arguments and returns the `_id` of the newly inserted document.

**File:** `9-insert_school.py`
**File:** `9-main.py`

**Function Prototype:**

```python
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    :param mongo_collection: The pymongo collection object
    :param kwargs: Keyword arguments representing the document fields
    :return: The _id of the inserted document
    """
```

**Usage:**

```python
./9-main.py
```

## Task 10: Change School Topics

This task involves writing a Python function that changes the list of topics for a school document based on its name.

**File:** `10-update_topics.py, 10-main.py`

**Function Prototype:**

```python
def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    :param mongo_collection: The pymongo collection object
    :param name: The school name to update
    :param topics: The list of topics approached in the school
    """
```

**Usage:**

```python
./10-main.py
```

## Task 11: Where Can I Learn Python?

This task involves writing a Python function that returns a list of schools that have a specific topic.

**File:** `11-schools_by_topic.py, 11-main.py`

**Function Prototype:**

```python
def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of school having a specific topic
    :param mongo_collection: The pymongo collection object
    :param topic: The topic searched for in the schools' topics
    :return: A list of schools having the specific topic
    """
```

**Usage:**

```python

./11-main.py
```

### Task 12: Log Stats

This task involves writing a Python script that provides statistics about Nginx logs stored in MongoDB.

**File:** `12-log_stats.py`

**Usage:**

First, download and restore the data:

```bash
curl -o dump.zip -s "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-webstack/411/dump.zip"
unzip dump.zip
mongorestore dump
```

```python
./12-log_stats.py
```
