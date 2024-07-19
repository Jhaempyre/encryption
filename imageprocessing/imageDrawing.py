from PIL import Image

# Define the dimensions of the image
width, height = 4608, 3456  # Replace these with your actual dimensions

# Initialize a list to hold the pixel data
pixel_values = []

key = 789
# Read the pixel data from the file
with open('example.txt', 'r') as f:
    for line in f:
        # Extract the RGB values from each line
        parts = line.strip().split(': ')[1].split(', ')
        r_enc = int(parts[0].split('=')[1])
        g_enc = int(parts[1].split('=')[1])
        b_enc = int(parts[2].split('=')[1])
        r = r_enc^key
        g = g_enc^key
        b = b_enc^key
        pixel_values.append((r, g, b))

# Create a new image with the specified dimensions
image = Image.new("RGB", (width, height))

# Set the pixel values in the image
index = 0
for y in range(height):
    for x in range(width):
        if index < len(pixel_values):
            image.putpixel((x, y), pixel_values[index])
            index += 1

# Save the generated image
image.save("output_image.png")