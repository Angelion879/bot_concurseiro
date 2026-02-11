from src import scrapper as s


class TestScrapper:
    """Contains the tests fot the scrapper features"""
    with open('tests\\mocks\\mock_site.html', 'r', encoding='utf-8') as file:
        mock_website = file.read()

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
