from pathlib import Path
from src import scrap, messenger

base_dir = Path("tests/mocks")

class TestMessenger:
    """Contains the tests fot the messenger file features"""

    #boilerplate
    with open(base_dir/'mock_site.html', 'r', encoding='utf-8') as file:
        mock_website = file.read()

    AREA = "TJ"
    ROLE = "Oficial de Justiça"
    mock_soup = scrap.soup_maker(mock_website)
    available = scrap.get_available_tenders(mock_soup, AREA)
    filtered = scrap.filter_tenders_by_role(available, ROLE)

    def test_message_builder(self):
        """should return a string with the structured content"""
        EXPECTED = "## [Concurso TJ AL](https://exemple.com)\nSituação atual: comissão formada\n\n## [Concurso TJ PB](https://exemple.com)\nSituação atual: comissão formada"

        actual = messenger.message_builder(self.filtered)
        assert EXPECTED == actual
