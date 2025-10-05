import time
import redis


def main():
    r = redis.Redis()
    try:
        r.ping()
    except redis.ConnectionError:
        print("Could not connect to Redis server.")
        return
    print("Connected to Redis server.")

    while True:
        item = r.brpop("judgelet:tasks", timeout=5)
        if not item:
            time.sleep(0)
        else:
            print(f"Processing task: {item[1].decode()}")
