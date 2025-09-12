import os
import requests
from bs4 import BeautifulSoup as bs

import page_flipper as pf

try:
    SITE = os.environ["ADDRESS"]
except KeyError:
    from keys import address
    SITE = address

res = requests.get(SITE)
soup = bs(res.content, 'html.parser')
pages = soup.select('.page-link')

titles = soup.select('#_br_com_seatecnologia_in_buscadou_BuscaDouPortlet_params')

print(titles)
