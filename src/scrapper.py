"""Scrapper functions to get information from the html and json content"""
import time
import requests
from bs4 import BeautifulSoup as bs

def http_request(page_url):
    """handles the http request"""

    try:
        res = requests.get(page_url, timeout=5)
    except TimeoutError:
        print("We got timed out! Trying again in 10s!")
        time.sleep(10)
        http_request(page_url)

    return res


if __name__ == '__main__':
    response = http_request('https://blog.grancursosonline.com.br/concursos-2026/')
    print(response.status_code)
