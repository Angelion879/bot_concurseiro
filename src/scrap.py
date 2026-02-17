"""Scrapper functions to get information from the html and json content"""
import time
import re
import requests
from bs4 import BeautifulSoup as bs

URL = 'https://blog.grancursosonline.com.br/concursos-2026/'

def scrapper(area, role):
    """handles the other functions and their needs"""

    tenders_soup = visit_page(URL)
    tender_list = get_available_tenders(tenders_soup, area)
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

def soup_maker(html_content):
    """creates the soup with html content"""

    soup = bs(html_content, 'html.parser')

    return soup

def visit_page(url):
    """unifies the process of getting the html content from a web page"""

    page_resp = http_request(url)
    page_soup = soup_maker(page_resp.content)

    return page_soup

def get_available_tenders(tender_soup, area):
    """returns a list with all available tenders in the determined area"""

    tenders = tender_soup.find_all("h4", string=re.compile(area))

    return tenders


def filter_tenders_by_role(tenders, role):
    """returns a filtered list of tenders based on the wanted role"""

    filtered = []
    MULTIPLE = "diversos"

    for i, item in enumerate(tenders):
        tender_data = tenders[i].next_sibling.next_sibling.next_sibling.next_sibling
        # work around tender metadata
        data_list = tender_data.select('li')
        tender_page_url = item.select('a')[0].get('href', None)

        tender_status = data_list[0].string
        targets = [data_list[2].string, data_list[3].string]
        role_found = False

        if any(role in t for t in targets):
            role_found = True
        elif any(MULTIPLE in t.lower() for t in targets):
            page_soup = visit_page(tender_page_url)
            if tender_with_multiple_roles_has_selected(page_soup, role):
                role_found = True

        if role_found:
            filtered.append([
                item.string, # tender title
                tender_status,
                tender_page_url
            ])

    return filtered

def tender_with_multiple_roles_has_selected(page_soup, role):
    """when the tender does not have the roles in the description, visit its page to check"""

    is_role_there = page_soup.find(string=re.compile(role))

    return True if is_role_there else False


if __name__ == '__main__':
    aaa = scrapper("PC", "Perito Criminal")
    print(aaa)
