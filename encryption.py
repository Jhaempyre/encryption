import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Function to pad the data to be a multiple of block size
def pad(data):
    block_size = AES.block_size
    padding_length = block_size - (len(data) % block_size)
    return data + bytes([padding_length] * padding_length)

# Function to unpad the data after decryption
def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Function to encrypt the content of a text file using AES-256
def encrypt_text_file(file_name, key):
    with open(file_name, 'rb+') as file:  # Open the file in read/write mode
        plaintext = file.read()

        # Pad the plaintext to be multiple of block size
        plaintext = pad(plaintext)

        # Generate a random initialization vector (IV)
        iv = get_random_bytes(AES.block_size)

        # Create AES cipher object in CBC mode with the given key and IV
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Encrypt the plaintext
        ciphertext = cipher.encrypt(plaintext)

        # Move file pointer to the beginning of the file
        file.seek(0)

        # Write the IV followed by the ciphertext to the file
        file.write(iv + ciphertext)

        # Truncate the file to the size of the encrypted data
        file.truncate(len(iv + ciphertext))

# Generate a random 256-bit key (replace this with your actual key)
key = get_random_bytes(32)

# Filename of the text file to be encrypted (in the same directory as the script)
file_name = 'example.txt'

# Encrypt the text file in-place
encrypt_text_file(file_name, key)
print(key)
print("Text file encrypted successfully.")
