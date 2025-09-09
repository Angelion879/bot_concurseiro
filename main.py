import os
import requests

try:
    SITE = os.environ["ADDRESS"]
except KeyError:
    from keys import address
    SITE = address

res = requests.get(SITE)
