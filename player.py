import socket
from utils import fetch_track 
from dotenv import load_dotenv
import os
import base64
import requests

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_access_token(client_id, client_secret):
    string = client_id + ':' + client_secret
    string_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode('ascii')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {base64_string}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {'grant_type': 'client_credentials'}

    response = requests.request('POST', url=url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception("Falha ao obter token de acesso:", response.json())

def client_main():
    try:
        access_token = get_access_token(CLIENT_ID, CLIENT_SECRET)

        HOST = '127.0.0.1'
        PORT = 5000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))

        data = s.recv(1024)
        track_id = data.decode('utf-8').strip()
        print(f"ID da música recebido do servidor: {track_id}")

        track_data = fetch_track(track_id, access_token)
        formatted_response = "\n".join([f"{key}: {value}" for key, value in track_data.items()])
        print("Enviando as informações da música de volta ao servidor...")

        s.sendall(formatted_response.encode())

        s.close()
    except Exception as e:
        print(f"Erro no cliente: {e}")

if __name__ == "__main__":
    client_main()
