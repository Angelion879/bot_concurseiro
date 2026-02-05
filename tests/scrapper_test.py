from pytest import *
from src import scrapper as s


class TestScrapper:
    """Contains the tests fot the scrapper features"""
    with open('tests\\mock_site.html', 'r', encoding='utf-8') as file:
        mock_website = file.read()

    def test_get_available_tenders(self):
        """should return a list with available tenders filtered by an determined area"""

        EXPECTED = '[<h4><a href="https://exemple.com" rel="noopener" target="_blank">Concurso TRT PI</a></h4>, <h4><a href="https://exemple.com" rel="noopener" target="_blank">Concurso TRT RS</a></h4>, <h4><a href="https://exemple.com" rel="noopener" target="_blank">Concurso TRT MT</a></h4>, <h4><a href="https://exemple.com" rel="noopener" target="_blank">Concurso TRT PR</a></h4>]'

        actual = s.get_available_tenders(self.mock_website, "TRT")
        assert EXPECTED == str(actual)
