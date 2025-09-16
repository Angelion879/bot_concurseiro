"""Gets url of all pages available and return in a list"""
import time
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

SITE = 'https://www.in.gov.br/consulta/-/buscar/dou?q="Concurso+público"&s=todos&exactDate=dia&sortType=0&delta=20&artType=Edital'

chrome_options = Options()
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)
driver.get(SITE)

def get_total_page_num():
    """grabs the amount of pages available"""
    res = requests.get(SITE, timeout=5)
    soup = bs(res.content, 'html.parser')
    total_page_num = soup.select('.page-link')[-2].get_text()

    return int(total_page_num)

def create_page_link_list():
    """generates url to flip through the pages"""
    page_number = get_total_page_num()
    page_url = SITE
    link_list = []

    for i in range(page_number):
        try:
            driver.get(page_url)
            link_list.append(page_url)

            next_page_button = driver.find_element(By.ID, 'rightArrow')
            next_page_button.click()
            time.sleep(3)

            soup = bs(driver.page_source, 'html.parser')
            page_url = soup.find('input', id='URL').get('value')
        except:
            print('list ended')

    return link_list

if __name__ == '__main__':
    a = get_total_page_num()

    print(a)
