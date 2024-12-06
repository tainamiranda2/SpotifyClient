import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlencode
# Carregar variáveis do .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPES = os.getenv("SCOPES")

def get_authorization_code():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
    }
    auth_url = f"https://accounts.spotify.com/authorize?{urlencode(params)}"
    print("Abra o link abaixo para autorizar o aplicativo e cole o código aqui:")
    print(auth_url)
    code = input("Código de autorização: ")
    return code

def get_access_token(code):
    token_url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Erro ao obter token:", response.json())
        return None
