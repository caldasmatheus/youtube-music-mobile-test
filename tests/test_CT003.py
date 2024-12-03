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

        initial_song = library_page.verify_song_in_playlist()
        assert initial_song is not None, "A playlist não contém músicas para excluir."
        library_page.playlist_options()
        library_page.click_element_by_text("Remover da playlist")
        success_notification = library_page.wait_element(
            ("android:id/message"), timeout=5
        )
        assert "música foi removida" in success_notification.text.lower(), "A notificação de sucesso não foi exibida."

        updated_song = library_page.verify_song_in_playlist()
        assert updated_song != initial_song, "A música ainda está na playlist."
