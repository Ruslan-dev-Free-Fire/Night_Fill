from PIL import Image, ImageEnhance
import os
import multiprocessing


def process_image(input_image_path, output_image_path):
    # Open the image using Pillow
    image = Image.open(input_image_path)

    # Increase brightness by 40%
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.1)  # Increase by 40%

    # Check for the presence of an alpha channel
    if image.mode == 'RGBA':
        r, g, b, a = image.split()
        r = r.point(lambda i: i - 255)
        g = g.point(lambda i: i - 163)
        image = Image.merge('RGBA', (r, g, b, a))
    elif image.mode == 'RGB':
        r, g, b = image.split()
        r = r.point(lambda i: i - 255)
        g = g.point(lambda i: i - 163)
        image = Image.merge('RGB', (r, g, b))
    else:
        # If the image has a different mode (e.g., grayscale), save it without modifications
        pass

    # Save the processed image
    image.save(output_image_path)

    print(f"{input_image_path} 画像が処理され、{output_image_path} として保存されました。")


def main():
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

    # Separate images into two groups: with alpha channels and without
    images_with_alpha = []
    images_without_alpha = []

    for filename in input_files:
        input_image_path = os.path.join(input_folder, filename)
        output_image_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_fill.png")

        image = Image.open(input_image_path)
        if 'A' in image.getbands():
            images_with_alpha.append((input_image_path, output_image_path))
        else:
            images_without_alpha.append((input_image_path, output_image_path))

    # Create processes for processing images with alpha channels
    with multiprocessing.Pool() as pool:
        pool.starmap(process_image, images_with_alpha)
        pool.starmap(process_image, images_without_alpha)


if __name__ == "__main__":
    main()
