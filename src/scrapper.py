"""Scrapper functions to get information from the html and json content"""
import json
import requests
from bs4 import BeautifulSoup as bs

def get_json_content(page_url):
    """gets the html page, pulls and returns the json content related to the results"""
    try:
        resp = requests.get(page_url, timeout=5)
    except TimeoutError:
        print("We got timed-out! Try again later!")

    soup = bs(resp.content, 'html.parser')
    json_obj = soup.select('#_br_com_seatecnologia_in_buscadou_BuscaDouPortlet_params'
                             )[0].get_text().replace('\n','').replace('\t','')
    json_array = json.loads(json_obj)['jsonArray']

    return json_array

def json_array_handler(json_array):
    """generator to return a dict per time"""
    for j_dict in json_array:
        yield j_dict

def filter_through_content(json_dict,area):
    """filters and returns the title and link for the desired content"""
    institution = json_dict['hierarchyStr']

    if area in institution:
        title = json_dict['artType']
        link = "https://www.in.gov.br/web/dou/-/"+json_dict['urlTitle']

        return [title,link]

if __name__ == '__main__':
    pass
