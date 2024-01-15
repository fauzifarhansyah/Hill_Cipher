import numpy as np

def encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    
    # Pastikan panjang plaintext adalah kelipatan dari ukuran matriks kunci
    if len(plaintext) % n != 0:
        raise ValueError("Panjang plaintext harus merupakan kelipatan dari ukuran matriks kunci")
    
    # Inisialisasi matriks plaintext
    plaintext_matrix = np.array([ord(char) - ord('a') for char in plaintext])
    
    # Ubah matriks plaintext menjadi matriks dengan ukuran sesuai kunci
    plaintext_matrix = plaintext_matrix.reshape(len(plaintext) // n, n)
    
    # Enkripsi menggunakan Hill Cipher
    encrypted_matrix = np.dot(plaintext_matrix, key_matrix) % 26
    
    # Ubah kembali matriks hasil enkripsi menjadi string
    ciphertext = ''.join([chr(char + ord('a')) for char in encrypted_matrix.flatten()])
    
    return ciphertext

# Contoh penggunaan
plaintext = "hellok"
key_matrix = np.array([[6, 24], [13, 16]])

try:
    ciphertext = encrypt(plaintext, key_matrix)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
except ValueError as e:
    print("Error:", e)