# Image Darkening Automation

This Python script automates the process of darkening images using the Pillow (PIL) library. It adjusts brightness, modifies color channels, and saves the processed images.

## Usage
### Usage Example:

To use the program, simply place your input images in the `Image` directory and run the script. Processed images will be saved in the `Ready` directory. Images with an alpha channel (transparent areas) and images without an alpha channel will be processed simultaneously for improved efficiency.

```bash
python your_script.py
```

**Note:** Make sure you have the Pillow (`PIL`) library installed for image handling.

### Version 2.1 (Changes):

1. **Support for Images with Alpha Channel:** The program can now process images both with an alpha channel (transparent areas) and without it.

2. **Brightness Increase by 40%:** Image brightness is now increased by 40%, making the images brighter.

3. **Utilization of Multithreading:** To improve image processing performance, the program now employs multithreading. Images with alpha channels and without are processed concurrently in separate threads.

4. **Minor Bug Fixes:** During the update, minor bugs were fixed, and the code structure was enhanced for improved readability and reliability.

5. **Informative English Messages:** Progress and successful image processing messages are now displayed in English.

***Version 2.0 Release features:***

- Added the ability to process images in bulk within a specified input directory.
- Implemented a brightness adjustment feature to increase image brightness by 50%.
- Adjusted image brightness by -65%.
- Modified the red and green channels of images by subtracting fixed values (255 for red and 163 for green).
- Merged the channels back into an image and saved the processed images in the specified output directory with the same filenames as the original images, appended with "_fill.png."

## License
This project is licensed under the MIT License.

## Author
Ruslan-dev-Free-Fire

## Contact
banievro@gmail.com

