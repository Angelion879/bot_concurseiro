from pytest import *
from src import scrapper, main


class TestMain:
    """Contains the tests fot the main file functions"""

    with open('tests\\mocks\\mock_site.html', 'r', encoding='utf-8') as file:
        mock_website = file.read()

    #boilerplate
    AREA = "TJ"
    ROLE = "Oficial de Justiça"
    available = scrapper.get_available_tenders(mock_website, AREA)
    filtered = scrapper.filter_tenders_by_role(available, ROLE)
