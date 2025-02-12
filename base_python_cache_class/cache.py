class Cache():
    def __init__(self):
        self.cache = {}
        self.log = []

    def _get(self, key):
        return self.cache.get(key, None)


    def _set(self, key, value):
        self.cache[key] = value
        return True


    def _delete(self, key):
        if key in self.cache:
            del self.cache[key]
            return True
        else:
            print("Key not Present")
            return False


    def get(self, key):
        self.log.append(("GET", key))


    def set(self, key, value):
        self.log.append(("SET", key, value))


    def delete(self, key):
        self.log.append(("DELETE", key))


    def begin(self):
        if self.log:
            raise RuntimeError("ERROR: TRANSACTION ALREADY STARTED")
        self.log = [("START")]


    def commit(self):
        for action in self.log:
            if action[0] == "GET":
                self._get(action[1])
            elif action[0] == "SET":
                self._set(action[1],action[2])
            elif action[0] == "DELETE":
                self._delete(action[1])
        self.log = []


    def rollback(self):
        self.log = []
