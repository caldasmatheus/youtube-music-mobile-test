import pytest
from faker import Faker

@pytest.mark.usefixtures("open_app")
class Test_CT001:

    def test_create_playlist(self, request):
        faker = Faker('pt_BR')
        menu_page, library_page = request.getfixturevalue('open_app')
        menu_page.go_to_library_page()
        library_page.click_new_button()
        library_page.click_playlist_option()
        title = faker.sentence(nb_words=2)
        description = faker.paragraph(nb_sentences=1)
        library_page.enter_title(title)
        library_page.enter_description(description)
        library_page.create_playlist()
        menu_page.go_to_home_page()
        menu_page.go_to_library_page()
        library_page.select_playlist_menu()
        playlist_name = library_page.verify_playlist(title)
        assert playlist_name.is_displayed(), f"A playlist '{playlist_name}' não foi encontrada na interface."