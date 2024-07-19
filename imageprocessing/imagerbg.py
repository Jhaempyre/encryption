from PIL import Image

# Open the image file
image_path = "input_image.jpg"  # Replace with your image file path
image = Image.open(image_path)

key = 789
# Get the dimensions of the image
width, height = image.size
print(width, height)

# Get pixel information
pixel_values = []
for y in range(height):
    for x in range(width):
        # Get the RGB values of the pixel at position (x, y)
        r, g, b = image.getpixel((x, y))
        r_enc = r^key
        g_enc = g^key
        b_enc = b^key
        pixel_values.append((r_enc,g_enc,b_enc))

# Write the pixel values to a file
with open('example.txt', 'w') as f:
    for i, pixel in enumerate(pixel_values):
        value = f"Pixel {i+1}: R={pixel[0]}, G={pixel[1]}, B={pixel[2]}\n"  # Add newline
        f.write(value)