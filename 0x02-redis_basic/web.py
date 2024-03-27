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
    # Check if the content is already cached
    cached_content = rc.get(f"cached:{url}")
    if cached_content:
        print("Content found in cache.")
        return cached_content.decode('utf-8')

    # If content is not cached, fetch it from the URL
    print("Fetching content from URL.")
    html_content = requests.get(url).text

    # Cache the HTML content with an expiration time of 10 seconds
    rc.setex(f"cached:{url}", 10, html_content)

    return html_content

if __name__ == "__main__":
    # Test the get_page function
    print(get_page('http://slowwly.robertomurray.co.uk'))
