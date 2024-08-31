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
