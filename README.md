# PrecisionEdgeDetection

This repository contains Python code for precise edge detection and image measurement, designed to enhance geometric accuracy in image processing applications.

## Features
- *Edge Detection*: Utilizes advanced filters such as Canny, Sobel, and Prewitt for high-precision edge detection.
- *Contour Detection*: Identifies and traces the largest contour in an image, allowing for accurate boundary analysis.
- *Corner Detection*: Detects and labels the corners of the detected contour, with coordinate labeling.
- *Image Alignment and Rotation Calculation*: Calculates the center of the detected object and measures the angle of rotation based on alignment with the image center.
- *Graphical Visualization*: Displays the detected edges, contours, and corner points overlaid on the original image, with coordinates labeled.
- *Real-Time Performance Tracking*: Displays key metrics such as processing time, corner count, and rotation angle.
- *Image Saving*: Saves the final processed image with annotated edges, corners, and alignment.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/syedofc/PrecisionEdgeDetection.git

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

Dependencies include:
- **OpenCV**
- **Tkinter**
- **NumPy**

## Usage
1. Run the script:

   ```bash
   python Speed_aug.py

2. Select an image from your local system through the GUI, and view the processed results, including edge detection, contour detection, and corner labeling.

3. The processed image will be saved as result_image.jpg in the specified directory.

## Future Enhancements
- **Adding machine learning models for adaptive edge detection and feature recognition**
- **Extending the system for various image resolutions and complex geometric structures.**

## Key Justifications
- *Edge Detection*: The code uses cv2.Canny() to detect edges, which is aligned with the README.
- *Contour and Corner Detection*: The code finds the largest contour and approximates corners, then labels them, which fits into the corner detection feature in the README.
- *Real-World Measurements*: The code calculates rotation angle based on the center alignment of the object and image, which supports the real-world measurement aspect.
- *GUI and Image Saving*: You’ve used Tkinter for image selection and saved the final output, matching the description of user-friendly interaction and result saving.
- *Performance*: The script calculates processing time and displays the total number of corners, rotation angle, and time, which ties into the performance tracking feature.

## License
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
