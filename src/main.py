import os
import requests
from bs4 import BeautifulSoup as bs

import json

try:
    SITE = os.environ["ADDRESS"]
except KeyError:
    from keys import address
    SITE = address

res = requests.get(SITE)
soup = bs(res.content, 'html.parser')
#pages = soup.select('.page-link')

json_array_obj = soup.select('#_br_com_seatecnologia_in_buscadou_BuscaDouPortlet_params')[0].get_text().replace('\n','').replace('\t','')

json01 = json.loads(json_array_obj)

with open(f'output.json', 'w', encoding='utf-8') as file:
    json.dump(json01, file, indent=4, ensure_ascii=False)

print('done')
