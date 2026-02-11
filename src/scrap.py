"""Scrapper functions to get information from the html and json content"""
import time
import re
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://blog.grancursosonline.com.br/concursos-2026/'

def scrapper(area, role):
    """handles the other functions and their needs"""

    http_res = http_request(URL)
    tender_list = get_available_tenders(http_res.content, area)
    filtered_list = filter_tenders_by_role(tender_list, role)

    return filtered_list

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
    tenders = html_content.find_all("h4", string=re.compile(area))

    return tenders


def filter_tenders_by_role(tenders, role):
    """returns a filtered list of tenders based on the wanted role"""

    filtered = []

    for i, item in enumerate(tenders):
        tender_data = tenders[i].next_sibling.next_sibling.next_sibling.next_sibling
        data_list = tender_data.select('li')

        if (role in data_list[2].string) or (role in data_list[3].string):
            filtered.append([
                item.string,
                data_list[0].string,
                item.select('a')[0].get('href', None)
            ])
    return filtered


if __name__ == '__main__':
    aaa = scrapper("PC", "Perito Criminal")
    print(aaa)
