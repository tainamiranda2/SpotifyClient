import requests

def fetch_track(track_id, access_token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return {
            "Name": data.get("name"),
            "Artist": ", ".join([artist["name"] for artist in data["artists"]]),
            "Album": data["album"]["name"],
            "Release Date": data["album"]["release_date"],
        }
    else:
        raise Exception(f"Erro ao buscar música: {response.status_code} - {response.text}")
