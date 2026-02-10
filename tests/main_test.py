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

    def test_there_is_new_content(self):
        """should return TRUE if the content collected is DIFFERENT from the previously saved"""
        not_updated = "tests\\mocks\\mock_non_updated.txt"
        actual = main.there_is_new_content(not_updated, self.filtered)

        assert True == actual

    def test_there_is_no_new_content(self):
        """should return FALSE if the content collected is the SAME from the previously saved"""
        updated = "tests\\mocks\\mock_updated.txt"
        actual = main.there_is_new_content(updated, self.filtered)

        assert False == actual
