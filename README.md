# Spotify App

Este é um aplicativo simples que se conecta à API do Spotify para buscar informações sobre músicas usando o ID da música e permite acessar informações da música, como nome, artista, álbum, duração e popularidade.

## Pré-requisitos

- Python 3.x
- Pip
- Uma conta simples

## Como configurar

### 1. Obter as credenciais do Spotify

1. Vá para [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Crie um novo aplicativo e anote as seguintes credenciais:
   - **CLIENT_ID**
   - **CLIENT_SECRET**
3. Defina o **REDIRECT_URI** como `http://localhost:8888/callback`.

### 2. Criar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e adicione as suas credenciais:

```env
CLIENT_ID=seu_client_id
CLIENT_SECRET=seu_client_secret
REDIRECT_URI=http://localhost:8888/callback
SCOPES=user-read-private playlist-read-private user-modify-playback-state

comando para rodar
python main.py

id de exemplo = 1jlG3KJ3gdYmhfuySFfpO1