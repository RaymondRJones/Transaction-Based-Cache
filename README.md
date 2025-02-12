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

## Video Explanation

[Video Link](https://www.loom.com/share/your-video-link)


## Starting Project
1. Clone the Repository

```
git clone https://github.com/RaymondRJones/Transaction-Based-Cache.git
```

2. Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate
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

## API Endpoints & Example Queries

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

