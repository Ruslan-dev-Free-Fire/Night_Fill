Image Darkening Automation
This Python script automates the process of darkening images using the Pillow (PIL) library. It adjusts brightness, modifies color channels, and saves the processed images.

Usage
Install the Pillow (PIL) library using pip install Pillow if it's not already installed.

Modify the input_folder and output_folder variables with the paths to your source and destination directories in the script darken_images.py.

Run the darken_images.py script to process all the images in the specified input directory and save the darkened versions in the output directory.

Example:

python
Copy code
python darken_images.py
Configuration
You can customize the image darkening process by modifying the script's parameters within the loop. The script currently applies a fixed set of modifications to each image. To adjust these modifications, you can modify the following lines of code within the loop:

python
Copy code
# Increase brightness (0.75 = 75% brightness)
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(0.75)  # Increase by 50%

# Adjust brightness (-65%)
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(1 - 0.01 * 5)

# Modify the red channel (-255)
r, g, b = image.split()
r = r.point(lambda i: i - 255)

# Modify the green channel (-163)
g = g.point(lambda i: i - 163)
Automatic Folder Creation
The script checks for the existence of the specified input_folder and output_folder directories. If they do not exist, the script will create them automatically to ensure a smooth image processing workflow.

License
This project is licensed under the MIT License.

Author
Ruslan-dev-Free-Fire

Contact
banievro@gmail.com

