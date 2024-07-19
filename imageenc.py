from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(data):
    block_size = AES.block_size
    padding_length = block_size - (len(data) % block_size)
    return data + bytes([padding_length] * padding_length)

def encrypt_image(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        image_data = file.read()

    cipher = AES.new(key, AES.MODE_ECB)
    padded_image_data = pad(image_data)
    encrypted_image_data = cipher.encrypt(padded_image_data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_image_data)

    print("Image encrypted successfully.")

# Generate a random 256-bit key
key = get_random_bytes(32)

# Filename of the input image file
input_image_file = 'input_image.jpg'

# Filename of the output encrypted image file
output_encrypted_image_file = 'encrypted_image.enc'

# Encrypt the input image
encrypt_image(input_image_file, output_encrypted_image_file, key)
print(key)
