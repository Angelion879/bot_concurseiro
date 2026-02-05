"""Scrapper functions to get information from the html and json content"""
import time
import re
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

def get_available_tenders(http_response, area):
    """returns a list with all available tenders in the determined area"""
    html_content = bs(http_response, 'html.parser')

    tenders = html_content.find_all("h4",string=re.compile(area))

    return tenders

def filter_tenders_by_role(tenders):
    """returns a filtered list of tenders based on the wanted role"""

    bbb = tenders[0].next_sibling.next_sibling.next_sibling.next_sibling
    ccc = bbb.select('li')[2].string
    return ccc


if __name__ == '__main__':
    response = http_request('https://blog.grancursosonline.com.br/concursos-2026/')
    #print(response.status_code)

    tender_list = get_available_tenders(response.content, "PC")
    aaa = filter_tenders_by_role(tender_list)
    print(aaa)
