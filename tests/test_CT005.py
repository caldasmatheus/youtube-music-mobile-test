import pytest

@pytest.mark.usefixtures("open_app")
class Test_CT005:

    def test_delete_playlist(self, request):
        menu_page, library_page = request.getfixturevalue('open_app')
        menu_page.go_to_library_page()
        library_page.click_new_button()
        library_page.click_playlist_option()
        playlist_name = library_page.enter_title("Delete Playlist")
        library_page.enter_description("Playlist de teste a ser deletada")
        library_page.create_playlist()
        menu_page.go_to_home_page()
        menu_page.go_to_library_page()
        library_page.select_playlist_menu()
        library_page.playlist_options()
        library_page.click_delete_playlist()
        library_page.confirm_delete_playlist()
        menu_page.go_to_home_page()
        menu_page.go_to_library_page()
        assert playlist_name is None, f"A playlist '{playlist_name}' foi encontrada na interface."