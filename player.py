import requests

def play_playlist(access_token, playlist_uri):
    url_devices = "https://api.spotify.com/v1/me/player/devices"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url_devices, headers=headers)
    if response.status_code == 200:
        devices = response.json()['devices']
        if devices:
            device_id = devices[0]['id']
            play_url = f"https://api.spotify.com/v1/me/player/play?device_id={device_id}"
            data = {"context_uri": playlist_uri}
            response_play = requests.put(play_url, headers=headers, json=data)
            if response_play.status_code == 204:
                print("Reprodução iniciada!")
            else:
                print("Erro ao iniciar reprodução:", response_play.json())
        else:
            print("Nenhum dispositivo disponível para reprodução.")
    else:
        print("Erro ao obter dispositivos:", response.json())
