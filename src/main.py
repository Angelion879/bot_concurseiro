import os
import requests
from bs4 import BeautifulSoup as bs

try:
    SITE = os.environ["ADDRESS"]
except KeyError:
    from keys import address
    SITE = address

res = requests.get(SITE)
soup = bs(res.text, 'html.parser')

tags = soup.select('.page-link')

print(tags[-2].get_text())
