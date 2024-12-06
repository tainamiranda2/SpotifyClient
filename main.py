from auth import get_authorization_code, get_access_token
from playlists import fetch_playlists
from player import play_playlist
from urllib.parse import urlencode

def main():
    print("=== SportyClient CLI ===")
    code = get_authorization_code()
    token = get_access_token(code)
    
    if token:
        playlists = fetch_playlists(token)
        if playlists:
            choice = int(input("Escolha uma playlist pelo número: ")) - 1
            selected_playlist = playlists[choice]
            print(f"Tocando: {selected_playlist['name']}")
            play_playlist(token, selected_playlist["uri"])

if __name__ == "__main__":
    main()
