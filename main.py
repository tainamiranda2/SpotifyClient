import socket

def main():
    HOST = '127.0.0.1'
    PORT = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()

    print("Servidor aguardando conexão do cliente...")
    conn, addr = s.accept()
    print(f"Conectado ao cliente em {addr}")

    track_id = input("Digite o ID da música: ").strip()
    if not track_id:
        print("ID da música não pode ser vazio. Encerrando conexão.")
        conn.close()
        s.close()
        return

    conn.sendall(track_id.encode())

    response = conn.recv(4096)
    print("Informações da música recebidas do cliente:")
    print(response.decode())

    conn.close()
    s.close()
    print("Conexão encerrada.")

if __name__ == "__main__":
    main()
