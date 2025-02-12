import pytest
from cache import Cache

def test_basic_set_get():
    cache = Cache()
    cache.set("A", 100)
    cache.commit()
    assert cache._get("A") == 100

def test_set_get_transaction():
    cache = Cache()
    cache.begin()
    cache.set("X", 200)
    assert cache._get("X") is None
    cache.commit()
    assert cache._get("X") == 200

def test_delete():
    cache = Cache()
    cache.set("B", 500)
    cache.commit()
    cache.begin()
    cache.delete("B")
    assert cache._get("B") == 500
    cache.commit()
    assert cache._get("B") is None

def test_rollback():
    cache = Cache()
    cache.set("C", 300)
    cache.commit()
    cache.begin()
    cache.set("C", 999)
    assert cache._get("C") == 300
    cache.rollback()
    assert cache._get("C") == 300

def test_rollback_delete():
    cache = Cache()
    cache.set("D", 700)
    cache.commit()
    cache.begin()
    cache.delete("D")
    assert cache._get("D") == 700
    cache.rollback()
    assert cache._get("D") == 700

def test_begin_while_transaction_active():
    cache = Cache()
    cache.begin()
    with pytest.raises(RuntimeError, match="ERROR: TRANSACTION ALREADY STARTED"):
        cache.begin()

def test_commit_clears_log():
    cache = Cache()
    cache.begin()
    cache.set("E", 1000)
    cache.commit()
    assert cache.log == []

def test_rollback_clears_log():
    cache = Cache()
    cache.begin()
    cache.set("F", 2000)
    cache.rollback()
    assert cache.log == []

