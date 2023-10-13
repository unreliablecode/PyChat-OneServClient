import socket

# Konfigurasi server
host = '0.0.0.0'  # Gunakan alamat IP komputer pertama
port = 12345

# Buat socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Menunggu koneksi dari komputer kedua di {host}:{port}")

# Terima koneksi dari komputer kedua
client_socket, client_address = server_socket.accept()
print(f"Terhubung dengan {client_address}")

while True:
    # Terima pesan dari komputer kedua
    message = client_socket.recv(1024).decode()
    if not message:
        break
    print(f"Komputer kedua: {message}")

    # Kirim balasan
    response = input("Anda: ")
    client_socket.send(response.encode())

# Tutup koneksi
client_socket.close()
server_socket.close()
