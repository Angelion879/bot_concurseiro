from src import main, scrap

class TestMain:
    """Contains the tests fot the main file functions"""

    with open('tests\\mocks\\mock_site.html', 'r', encoding='utf-8') as file:
        mock_website = file.read()

    #boilerplate
    AREA = "TJ"
    ROLE = "Oficial de Justiça"
    available = scrap.get_available_tenders(mock_website, AREA)
    filtered = scrap.filter_tenders_by_role(available, ROLE)

    def test_there_is_new_content(self):
        """should return TRUE if the content collected is DIFFERENT from the previously saved"""
        not_updated = "tests\\mocks\\mock_non_updated.txt"
        actual = main.there_is_new_content(not_updated, self.filtered)

        assert actual is True

    def test_there_is_no_new_content(self):
        """should return FALSE if the content collected is the SAME from the previously saved"""
        updated = "tests\\mocks\\mock_updated.txt"
        actual = main.there_is_new_content(updated, self.filtered)

        assert actual is False

    def test_update_doc_with_tenders_info(self):
        """should update document with new acquired content"""
        testing_file = "tests\\mocks\\mock_non_updated.txt"

        with open(testing_file, "r", encoding='utf-8') as file:
            not_updated = file.read()
            file.close()
        main.update_doc_with_tenders_info(testing_file, self.filtered)

        with open(testing_file, "r", encoding='utf-8') as f:
            updated = f.read()
            f.close()

        assert not_updated != updated

    # returning not_updated file to original state
        with open(testing_file, "w", encoding='utf-8') as ending:
            ending.write(not_updated)
            ending.close()
