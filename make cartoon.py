import cv2
import numpy as np

def cartoonize_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to create a cartoon-like effect
    color = cv2.bilateralFilter(image, 9, 250, 250)

    # Combine the edges and color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# Specify the path to your input image
input_image_path = 'C:\\Users\\user\\Desktop\\newp\\venv\\resources\\cat.jfif'

# Cartoonize the image
cartoon_image = cartoonize_image(input_image_path)

# Display the original and cartoonized images
cv2.imshow('Original Image', cv2.imread(input_image_path))
cv2.imshow('Cartoonized Image', cartoon_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
