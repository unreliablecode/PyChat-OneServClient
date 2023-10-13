import socket

# Konfigurasi client
host = 'localhost'  # Ganti dengan alamat IP komputer pertama
port = 12345

# Buat socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print(f"Terhubung dengan komputer pertama di {host}:{port}")

while True:
    # Kirim pesan
    message = input("Anda: ")
    client_socket.send(message.encode())

    # Terima balasan
    response = client_socket.recv(1024).decode()
    print(f"Komputer pertama: {response}")

# Tutup koneksi
client_socket.close()
