import cv2
import numpy as np
from matplotlib import pyplot as plt

def load_image(file_path):
    """Loads an image from the specified file path."""
    image = cv2.imread(file_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {file_path}")
    return image

def display_image(title, image):
    """Displays an image with a given title."""
    # Convert BGR to RGB for proper display using matplotlib
    if len(image.shape) == 3:  # Color image
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:  # Grayscale image
        image_rgb = image
    plt.imshow(image_rgb, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

def convert_to_grayscale(image):
    """Converts an image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def resize_image(image, width, height):
    """Resizes an image to the given width and height."""
    return cv2.resize(image, (width, height))

def apply_blur(image, kernel_size):
    """Applies Gaussian blur to the image with a given kernel size."""
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def detect_edges(image, low_threshold, high_threshold):
    """Applies Canny edge detection on the image."""
    return cv2.Canny(image, low_threshold, high_threshold)

def adjust_brightness_contrast(image, alpha, beta):
    """Adjusts the brightness and contrast of the image.
    alpha: Contrast control (1.0-3.0).
    beta: Brightness control (0-100).
    """
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

def rotate_image(image, angle):
    """Rotates the image by the specified angle (in degrees)."""
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))

def flip_image(image, flip_code):
    """Flips the image.
    flip_code: 0 for vertical, 1 for horizontal, -1 for both.
    """
    return cv2.flip(image, flip_code)

def draw_shapes(image):
    """Draws basic shapes on the image."""
    output = image.copy()
    # Draw a rectangle
    cv2.rectangle(output, (50, 50), (200, 200), (255, 0, 0), 2)
    # Draw a circle
    cv2.circle(output, (300, 300), 50, (0, 255, 0), -1)
    # Draw a line
    cv2.line(output, (100, 400), (400, 400), (0, 0, 255), 5)
    return output

def main():
    # File path to the input image
    file_path = 'example.jpg'  # Replace with your image file path

    try:
        # Load the image
        image = load_image(file_path)
        display_image("Original Image", image)

        # Convert to grayscale
        gray_image = convert_to_grayscale(image)
        display_image("Grayscale Image", gray_image)

        # Resize the image
        resized_image = resize_image(image, 200, 200)
        display_image("Resized Image", resized_image)

        # Apply Gaussian blur
        blurred_image = apply_blur(image, kernel_size=15)
        display_image("Blurred Image", blurred_image)

        # Edge detection
        edges = detect_edges(gray_image, 50, 150)
        display_image("Edge Detection", edges)

        # Adjust brightness and contrast
        bright_image = adjust_brightness_contrast(image, alpha=1.5, beta=50)
        display_image("Brightness and Contrast Adjusted", bright_image)

        # Rotate the image
        rotated_image = rotate_image(image, 45)
        display_image("Rotated Image", rotated_image)

        # Flip the image
        flipped_image = flip_image(image, flip_code=1)
        display_image("Flipped Image (Horizontal)", flipped_image)

        # Draw shapes
        shaped_image = draw_shapes(image)
        display_image("Image with Shapes", shaped_image)

    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
