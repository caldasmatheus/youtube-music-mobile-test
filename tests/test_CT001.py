import pytest

@pytest.mark.usefixtures("open_app")
class Test_CT001:

    def test_create_playlist(self, request):
        menu_page, library_page = request.getfixturevalue('open_app')
        menu_page.go_to_library_page()
        library_page.click_new_button()
        library_page.click_playlist_option()
        library_page.enter_title("Mix")
        library_page.enter_description("Playlist de teste")
        library_page.select_playlist_option(instance=4)
        library_page.select_playlist_option(instance=6)
        library_page.create_playlist()
        menu_page.go_to_home_page()
        menu_page.go_to_library_page()
        library_page.select_playlist_menu()
        playlist_name = library_page.verify_playlist("Mix")
        assert playlist_name.is_displayed(), f"A playlist '{playlist_name}' não foi encontrada na interface."