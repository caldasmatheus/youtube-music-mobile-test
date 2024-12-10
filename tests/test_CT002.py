import pytest
from faker import Faker

@pytest.mark.usefixtures("open_app")
class Test_CT002:

    def test_add_music_playlist(self, request):
        faker = Faker('pt_BR')
        menu_page, library_page = request.getfixturevalue('open_app')
        menu_page.go_to_library_page()
        library_page.click_new_button()
        library_page.click_playlist_option()
        title = faker.sentence(nb_words=2)
        description = faker.paragraph(nb_sentences=1)
        library_page.enter_title(title)
        library_page.enter_description(description)
        library_page.select_playlist_option(instance=4)
        library_page.select_playlist_option(instance=6)
        library_page.create_playlist()
        library_page.click_add_a_song()
        library_page.search_song()
        library_page.add_song_in_playlist()
        menu_page.go_to_library_page()
        library_page.select_playlist_menu()
        library_page.select_playlist(title)
        song_msg = library_page.verify_song_in_playlist()
        assert song_msg != "Nothing saved yet", f"A mensagem '{song_msg}' foi encontrada na interface."