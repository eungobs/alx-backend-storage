#!/usr/bin/env python3
"""
Module to define the get_page function
"""
import redis
import requests

# Connect to Redis
rc = redis.Redis()

def get_page(url: str) -> str:
    """Fetch HTML content from a URL and cache it"""
    # Increment the count for this URL
    rc.incr(f"count:{url}")

    # Get the current count
    count = rc.get(f"count:{url}")

    # Fetch HTML content from the URL
    html_content = requests.get(url).text

    # Cache the HTML content with an expiration time of 10 seconds
    rc.setex(f"cached:{url}", 10, html_content)

    return html_content

if __name__ == "__main__":
    # Test the get_page function
    print(get_page('http://slowwly.robertomurray.co.uk'))
