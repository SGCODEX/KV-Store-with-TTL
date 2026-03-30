import time

class KVStore:
    def __init__(self):
        self.store = {}

    def set(self, key, value, ttl=None):
        expiry = None

        if ttl is not None:
            expiry = time.time() + ttl  # seconds

        self.store[key] = {
            "value": value,
            "expiry": expiry
        }

        return True

    def get(self, key):
        if key not in self.store:
            return None

        data = self.store[key]

        # Lazy expiration check
        if data["expiry"] is not None and time.time() > data["expiry"]:
            del self.store[key]
            return None

        return data["value"]

    def delete(self, key):
        if key in self.store:
            del self.store[key]
            return True

        return False