# Computer_Vision
Computer Vision Fundamentals.

# Types of Images in Computer Vision

In computer vision, images can be categorized based on their type, structure, and representation. Below are the main types of images used in this domain:

## 1. Grayscale Images
- **Description**: Contains intensity information without color.
- **Pixel Value**: Single value per pixel, typically ranging from 0 (black) to 255 (white) for 8-bit images.
- **Applications**: Object detection, edge detection, medical imaging.

## 2. Binary Images
- **Description**: Black-and-white images where each pixel is either 0 (black) or 1 (white).
- **Pixel Value**: Two possible values (0 or 1).
- **Applications**: Document analysis, segmentation, thresholding.

## 3. Color Images
- **Description**: Contains color information for each pixel.
- **Pixel Value**: Multiple channels (e.g., RGB: Red, Green, Blue).
- **Types**:
  - **RGB Images**: Uses Red, Green, and Blue channels.
  - **HSV/HSL Images**: Hue, Saturation, and Value/Lightness representation.
  - **CMYK Images**: Cyan, Magenta, Yellow, and Key (Black) for printing.
- **Applications**: Image classification, scene understanding, facial recognition.

## 4. Multi-Spectral Images
- **Description**: Contains information across a wider range of wavelengths beyond the visible spectrum.
- **Pixel Value**: Multiple channels, each representing a different spectral band.
- **Applications**: Remote sensing, satellite imagery, agriculture.

## 5. Hyper-Spectral Images
- **Description**: Captures hundreds of spectral bands across a wide range of wavelengths.
- **Pixel Value**: High-dimensional spectral data for each pixel.
- **Applications**: Environmental monitoring, mineral exploration, medical imaging.

## 6. Depth Images (3D Images)
- **Description**: Encodes depth information (distance from the camera) for each pixel.
- **Pixel Value**: Distance values, often measured in meters or millimeters.
- **Applications**: 3D reconstruction, robotics, AR/VR, autonomous vehicles.

## 7. Thermal Images
- **Description**: Captures heat radiation emitted by objects.
- **Pixel Value**: Intensity values corresponding to temperature.
- **Applications**: Surveillance, medical diagnostics, industrial inspections.

## 8. Panoramic Images
- **Description**: Wide-field-of-view images stitched from multiple images.
- **Pixel Value**: Standard RGB or grayscale data.
- **Applications**: Virtual tours, environment mapping.

## 9. Time-Series Images
- **Description**: Sequences of images captured over time (video or temporal data).
- **Pixel Value**: Multiple images (frames) with pixel data.
- **Applications**: Video analysis, motion tracking, behavior analysis.

## 10. Annotated Images
- **Description**: Images with metadata like bounding boxes, masks, or labels.
- **Pixel Value**: Pixel data plus annotations (e.g., objects or regions).
- **Applications**: Training data for machine learning, object detection.

## 11. Medical Images
- **Description**: Images captured using specialized medical equipment.
- **Types**:
  - X-rays
  - CT scans
  - MRI
  - Ultrasound
- **Applications**: Diagnosis, treatment planning, medical research.

## 12. Synthetic Images
- **Description**: Computer-generated images or augmented data.
- **Applications**: Simulations, model training, AR/VR.

## 13. Point Cloud Images
- **Description**: Representation of 3D objects as a collection of points.
- **Pixel Value**: Each point has coordinates (x, y, z) and sometimes additional features like color.
- **Applications**: 3D modeling, robotics, autonomous navigation.

## 14. Sparse Images
- **Description**: Images with most pixel values set to zero, typically used in applications like sparse feature extraction.
- **Pixel Value**: Non-zero values are sparse in the overall pixel grid.
- **Applications**: Medical imaging, astronomy (e.g., sparse stars in a night sky).

## 15. Dense Optical Flow Images
- **Description**: Represents the motion between two consecutive frames of a video.
- **Pixel Value**: Each pixel contains a vector (dx, dy) representing motion in the x and y directions.
- **Applications**: Video analysis, motion tracking.
