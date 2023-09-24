from PIL import Image, ImageEnhance
import os

# Directory paths for input and saved images
input_folder = r"C:\Night_Fill\Image"
output_folder = r"C:\Night_Fill\Ready"

# Check for the presence of the output_folder folder and create it if it does not exist
if not os.path.exists(input_folder):
    os.makedirs(input_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of files in the input directory
input_files = os.listdir(input_folder)

# Iterate through all files in the directory
for filename in input_files:
    # Create full paths to the input and output files
    input_image_path = os.path.join(input_folder, filename)
    output_image_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_fill.png")

    # Open the image using Pillow
    image = Image.open(input_image_path)

    # Increase brightness by 50%
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(0.75)  # Increase by 50%

    # Adjust brightness by -65%
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1 - 0.01 * 5)

    # Modify the red channel by -255
    r, g, b = image.split()
    r = r.point(lambda i: i - 255)

    # Modify the green channel by -163
    g = g.point(lambda i: i - 163)

    # Merge the channels back into an image
    image = Image.merge('RGB', (r, g, b))

    # Save the darkened image
    image.save(output_image_path)

    print(f"画像 {filename} が正常に暗くなり、{os.path.basename(output_image_path)} として保存されました。")