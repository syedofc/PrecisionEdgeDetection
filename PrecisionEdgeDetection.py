import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import time

# Create a Tkinter root window (hidden)
root = tk.Tk()
root.withdraw()

# Ask the user to select an image file
image_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg *.png *.jpeg *.BMP *.MIM")])

if not image_path:
    print("No image selected. Exiting...")
    exit()

# Load the selected image
image = cv2.imread(image_path)

# Measure start time
start_time = time.time()

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Invert the pixels in the binary image
inverted_image = cv2.bitwise_not(binary_image)

# Apply Laplacian filter
filtered_image = cv2.Laplacian(binary_image, cv2.CV_8U)

# Sharpen the image by adding Laplacian result to the original grayscale image
sharpened_image = cv2.addWeighted(binary_image, 1.5, filtered_image, -0.5, 0)

edges = cv2.Canny(sharpened_image, 50, 150)

# Apply dilation to connect the lines of the edges
kernel = np.ones((3, 3), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

# Find contours in the dilated edges image
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour based on contour area
largest_contour = max(contours, key=cv2.contourArea)

# Find the bounding rectangle of the largest contour
x, y, w, h = cv2.boundingRect(largest_contour)

# Calculate the center of the rectangle
center_x = x + (w // 2)
center_y = y + (h // 2)

# Calculate the center of the whole image
image_height, image_width = image.shape[:2]
center_x_image = image_width // 2
center_y_image = image_height // 2

# Draw a red axis line in the center of the image
cv2.line(image, (center_x_image, 0), (center_x_image, image_height), (0, 0, 255), 2)
cv2.line(image, (0, center_y_image), (image_width, center_y_image), (0, 0, 255), 2)

# Draw the largest contour on the original image
result = cv2.drawContours(image.copy(), [largest_contour], -1, (0, 255, 0), 2)

# Find the corners of the largest contour using approxPolyDP
epsilon = 0.1 * cv2.arcLength(largest_contour, True)
approx_corners = cv2.approxPolyDP(largest_contour, epsilon, True)

# Draw the red circles at the corners and blue dots at the centers
center_points = []
for corner in approx_corners:
    x_center = corner[0][0]
    y_center = corner[0][1]
    center_points.append((x_center, y_center))
    cv2.circle(result, tuple(corner[0]), 10, (0, 0, 255), 2)
    cv2.circle(result, (x_center, y_center), 5, (255, 0, 0), -1)

    # Display the coordinates near the blue dot
    cv2.putText(result, f"({x_center}, {y_center})", (x_center + 10, y_center + 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

# Print the coordinates of the corners with numbering
for i, corner in enumerate(approx_corners):
    x_corner = corner[0][0]
    y_corner = corner[0][1]
    print(f"{i + 1}. Corner: ({x_corner}, {y_corner})")

    # Optionally, you can draw circles and labels on the corners
    cv2.circle(result, tuple(corner[0]), 10, (0, 0, 255), 2)
    cv2.circle(result, (x_corner, y_corner), 5, (255, 0, 0), -1)
    cv2.putText(result, f"{i + 1}. Corner: ({x_corner}, {y_corner})", (x_corner + 10, y_corner + 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

# Calculate the total number of corners
total_corners = len(approx_corners)
print(f"Total number of corners: {total_corners}")

# Measure end time
end_time = time.time()

# Calculate processing time
processing_time = end_time - start_time

# Calculate rotation angle based on the center alignment
rotation_angle = np.arctan2(center_y_image - center_y, center_x_image - center_x) * 180 / np.pi

# Display the result
result = cv2.resize(result, (800, 600))
cv2.imshow("Result Image", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result image
result_image_path = 'result_image.jpg'  # Specify your desired path here
cv2.imwrite(result_image_path, result)

# Print a message to indicate where the image is saved
print(f"Result image saved at: {result_image_path}")

# Print the extracted information
print(f"Rotation (deg): {rotation_angle:.2f} degrees")
print(f"Processing Time: {processing_time:.4f} seconds")