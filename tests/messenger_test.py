from src import scrap, messenger


class TestMessenger:
    """Contains the tests fot the messenger file features"""

    with open('tests\\mocks\\mock_site.html', 'r', encoding='utf-8') as file:
        mock_website = file.read()

    #boilerplate
    AREA = "TJ"
    ROLE = "Oficial de Justiça"
    available = scrap.get_available_tenders(mock_website, AREA)
    filtered = scrap.filter_tenders_by_role(available, ROLE)

    def test_message_builder(self):
        """should return a string with the structured content"""
        EXPECTED = "## [Concurso TJ AL](https://exemple.com)\nSituação atual: comissão formada\n\n## [Concurso TJ PB](https://exemple.com)\nSituação atual: comissão formada"

        actual = messenger.message_builder(self.filtered)
        assert EXPECTED == actual
