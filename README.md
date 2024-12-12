# Spotify App

Este é um projeto simples que se conecta à API do Spotify para buscar informações sobre músicas usando o ID da música e permite acessar informações da música, como nome, artista, álbum, data de lançamento e popularidade.

## Pré-requisitos

- Python 3.x
- Pip
- Conta no Spotify
- Credenciais de Desenvolvedor do Spotify

## Como configurar

### 1. Obter as credenciais do Spotify

1. Vá para o [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
2. Crie um novo aplicativo e anote as seguintes credenciais:
   - **CLIENT_ID**
   - **CLIENT_SECRET**
3. Defina o **REDIRECT_URI** como `http://localhost:8888/callback`.

### 2. Criar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e adicione as suas credenciais do Spotify:


CLIENT_ID=seu_client_id
CLIENT_SECRET=seu_client_secret
REDIRECT_URI=http://localhost:8888/callback
SCOPES=user-read-private playlist-read-private user-modify-playback-state

### 3 Instalar as dependencias
pip install -r requirements.txt

### 4 Executar o projeto

python main.py

python player.py

### 5 -Exemplo de Uso
ID de Música de Exemplo: 1jlG3KJ3gdYmhfuySFfpO1

### 6 - Estrutura do Projeto
main.py: Script do servidor que espera a conexão do cliente e solicita o ID da música.

player.py: Script do cliente que se conecta ao servidor, busca as informações da música na API do Spotify e envia de volta ao servidor.

utils.py: Contém a função para buscar o token de acesso e as informações da música na API do Spotify.

### 7 -Explicação
Ao rodar o servidor (main.py), ele aguarda a conexão do cliente.

Quando o cliente (player.py) se conecta, é solicitado o ID de uma música.

O cliente busca as informações da música na API do Spotify usando o token de acesso.

O cliente envia as informações da música de volta ao servidor, que então encerra a conexão.

Desafio
Este projeto foi desenvolvido como parte de um desafio de programação, que envolvia os seguintes passos:

1 - Autenticação

2 - Consumo da API do Spotify

3 - Uso de sockets