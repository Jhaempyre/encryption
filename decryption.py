from Crypto.Cipher import AES

# Function to unpad the data after decryption
def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

# Function to decrypt the content of an encrypted file using AES-256
def decrypt_text_file(file_name, key):
    with open(file_name, 'rb+') as file:
        encrypted_data = file.read()

        # Extract the initialization vector (IV) from the beginning of the file
        iv = encrypted_data[:AES.block_size]

        # Extract the ciphertext (encrypted data) from the file
        ciphertext = encrypted_data[AES.block_size:]

        # Create AES cipher object in CBC mode with the given key and IV
        cipher = AES.new(key, AES.MODE_CBC, iv)

        # Decrypt the ciphertext
        plaintext = cipher.decrypt(ciphertext)

        # Unpad the decrypted plaintext
        plaintext = unpad(plaintext)

        # Move file pointer to the beginning of the file
        file.seek(0)

        # Write the decrypted plaintext to the file
        file.write(plaintext)

        # Truncate the file to the size of the decrypted plaintext
        file.truncate(len(plaintext))

# Filename of the encrypted file to be decrypted
encrypted_file_name = 'example.txt'
key =b'\xd6\xd7q\xb8>s\xf5p\x93\xf6\xed\x83\x03\xb7\x86o\x13\xdc)\x9b%\xc3\x1ep\xd2\x9b\xc0SGvQo'
# Decrypt the encrypted file using the same key used for encryption
decrypt_text_file(encrypted_file_name, key)

print("File decrypted successfully.")
