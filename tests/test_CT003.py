import pytest

@pytest.mark.usefixtures("open_app")
class Test_CT003:

    def test_remove_song_from_playlist(self, request):
        menu_page, library_page = request.getfixturevalue('open_app')
        menu_page.go_to_library_page()
        library_page.click_new_button()
        library_page.click_playlist_option()
        library_page.enter_title("Musicas")
        library_page.enter_description("Playlist de musicas")
        library_page.select_playlist_option(instance=4)
        library_page.select_playlist_option(instance=6)
        library_page.create_playlist()
        library_page.click_add_a_song()
        library_page.search_song()
        library_page.add_song_in_playlist()
        menu_page.go_to_library_page()
        library_page.select_playlist_menu()
        library_page.select_playlist("Musicas")
        library_page.remove_music_song()
        library_page.remove_confirm_music()
        menu_page.go_to_home_page()
        menu_page.go_to_library_page()
        library_page.select_playlist_menu()
        library_page.select_playlist("Musicas")
        song_msg = library_page.verify_song_in_playlist()
        assert song_msg == "Nothing saved yet", f"A mensagem '{song_msg}' não foi encontrada na interface."
