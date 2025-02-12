# Transactional Cache API with Django & SQLite

This project provides a transaction-safe cache API using Django and SQLite. It allows users to perform atomic transactions on cached data, ensuring consistency, isolation, and rollback capabilities

## Features

    -Transaction-safe cache with begin(), commit(), and rollback()
    -Atomic operations to prevent partial updates
    -Persistent storage using SQLite
    -Simple REST API for easy integration
    -Keys must be hashable (strings, numbers, tuples, etc.)
    -Values can be any type (string, number, JSON, etc.)

Note: If the project needs to support non-hashable keys, they must be converted to a string before storage.

## Starting Project
1. Clone the Repository

```
git clone https://github.com/RaymondRJones/Transaction-Based-Cache.git
```

2. Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies

```
pip install -r requirements.txt
```

4. Apply Database Migrations

```
python manage.py migrate
```

5. Start the Django Server

```
python manage.py runserver
```

Why Use a Transaction-Safe Cache?

Most caching systems (e.g., Redis, Memcached) provide fast but volatile storage. However, they lack transaction safety, meaning:

    If a process crashes, partially applied changes remain.
    No built-in rollback mechanism.
    Concurrent modifications can lead to inconsistent state.

This solution allows you to use a cache with ACID-like transactions, ensuring:

    Atomicity: Either all changes are applied or none.
    Consistency: No partial updates.
    Isolation: Transactions are independent.
    Durability: Data persists in SQLite.

This makes it ideal for use cases where data integrity is critical.
API Endpoints & Example Queries
1. Start a Transaction

`curl -X POST http://127.0.0.1:8000/api/cache/begin/`

2. Set a Key (Inside a Transaction)

`curl -X POST http://127.0.0.1:8000/api/cache/set/ \
     -H "Content-Type: application/json" \
     -d '{"key": "username", "value": "john_doe"}'`

3. Get a Key

`curl -X GET "http://127.0.0.1:8000/api/cache/get/?key=username"`

4. Delete a Key

```
curl -X POST http://127.0.0.1:8000/api/cache/delete/ \
     -H "Content-Type: application/json" \
     -d '{"key": "username"}'
```

5. Commit the Transaction

`curl -X POST http://127.0.0.1:8000/api/cache/commit/`

6. Rollback the Transaction (Undo All Uncommitted Changes)

`curl -X POST http://127.0.0.1:8000/api/cache/rollback/`

Running Tests

To verify everything works, run:

```
cd base_python_cache_class
pytest test_cache.py
```

