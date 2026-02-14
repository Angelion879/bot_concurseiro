from pathlib import Path
from src import scrap as s

base_dir = Path("tests/mocks")

class TestScrapper:
    """Contains the tests fot the scrapper features"""
    with open(Path(base_dir/'mock_site.html').resolve(), 'r', encoding='utf-8') as file:
        mock_website = file.read()

    with open(Path(base_dir/'mock_tender_page.html').resolve(), 'r', encoding='utf-8') as file2:
        mock_tender_page = file2.read()

    def test_get_available_tenders(self):
        """should return a list with available tenders filtered by an determined area"""
        AREA = "TRT"
        EXPECTED = '[<h4><a href="https://exemple.com" rel="noopener" target="_blank">Concurso TRT PI</a></h4>, <h4><a href="https://exemple.com" rel="noopener" target="_blank">Concurso TRT RS</a></h4>, <h4><a href="https://exemple.com" rel="noopener" target="_blank">Concurso TRT MT</a></h4>, <h4><a href="https://exemple.com" rel="noopener" target="_blank">Concurso TRT PR</a></h4>]'

        actual = s.get_available_tenders(self.mock_website, AREA)
        assert EXPECTED == str(actual)


    def test_filter_tenders_by_role(self):
        """should return a list of tenders (and their data) that have the chosen role"""
        AREA = "TJ"
        ROLE = "Oficial de Justiça"
        EXPECTED = [['Concurso TJ AL', 'Situação atual: comissão formada', 'https://exemple.com'],
                    ['Concurso TJ PB', 'Situação atual: comissão formada', 'https://exemple.com']]

        testing_tenders = s.get_available_tenders(self.mock_website, AREA)
        actual = s.filter_tenders_by_role(testing_tenders, ROLE)
        assert EXPECTED == actual

    def test_multiple_roles_with_selected(self):
        """Should return TRUE when role IS found in tender's page"""
        actual = s.handle_tender_with_multiple_roles(self.mock_tender_page, "Oficial de Justiça")

        assert actual is True

    def test_multiple_roles_without_selected(self):
        """Should return FALSE when role is NOT found in tender's page"""
        actual = s.handle_tender_with_multiple_roles(self.mock_tender_page, "Perito Criminal")

        assert actual is False
