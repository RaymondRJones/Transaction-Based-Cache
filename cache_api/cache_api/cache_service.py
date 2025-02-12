from cache_app.models import CacheEntry
from django.db import transaction

class TransactionalCache:
    def __init__(self):
        self.log = []

    def get(self, key):
        self.log.append(("GET", key))
        try:
            return CacheEntry.objects.get(key=key).value
        except CacheEntry.DoesNotExist:
            return None

    def set(self, key, value):
        self.log.append(("SET", (key, value)))

    def delete(self, key):
        self.log.append(("DELETE", key))

    def begin(self):
        if self.log:
            raise RuntimeError("ERROR: TRANSACTION ALREADY STARTED")
        self.log = [("START")]

    def commit(self):
        if not self.log:
            raise RuntimeError("ERROR: NO TRANSACTION STARTED")
        with transaction.atomic():
            for action in self.log:
                if action[0] == "SET":
                    CacheEntry.objects.update_or_create(key=action[1][0], defaults={"value": action[1][1]})
                elif action[0] == "DELETE":
                    CacheEntry.objects.filter(key=action[1]).delete()
        self.log = []

    def rollback(self):
        if not self.log:
            raise RuntimeError("ERROR: NO TRANSACTION TO ROLLBACK")
        self.log = []

