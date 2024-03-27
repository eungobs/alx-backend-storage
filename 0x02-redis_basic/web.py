#!/usr/bin/env python3
"""
create a web cache
"""
import redis
import requests

rc = redis.Redis()

def get_page(url: str) -> str:
    """ get a page and cache value """
    rc.incr(f"count:{url}")
    count = rc.get(f"count:{url}")
    rc.setex(f"cached:{url}", 10, requests.get(url).text)
    return rc.get(f"cached:{url}").decode('utf-8')

if __name__ == "__main__":
    print(get_page('http://slowwly.robertomurray.co.uk'))
