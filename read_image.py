# Python Code to Read Different Types of Images in Computer Vision

import cv2
import numpy as np

# 1. Reading Grayscale Images
def read_grayscale_image(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

# 2. Reading Binary Images (after thresholding)
def read_binary_image(filepath):
    image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return binary_image

# 3. Reading Color Images
def read_color_image(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR)

# 4. Reading Multi-Spectral Images
def read_multi_spectral_image(filepath, bands):
    # Assuming bands are provided as separate files
    return [cv2.imread(f"{filepath}_band{i}.tif", cv2.IMREAD_GRAYSCALE) for i in range(bands)]

# 5. Reading Hyper-Spectral Images
def read_hyper_spectral_image(filepath):
    # Example with numpy loading a .npy file containing hyperspectral data
    return np.load(filepath)

# 6. Reading Depth Images
def read_depth_image(filepath):
    return cv2.imread(filepath, cv2.IMREAD_UNCHANGED)

# 7. Reading Thermal Images
def read_thermal_image(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

# 8. Reading Panoramic Images
def read_panoramic_image(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR)

# 9. Reading Time-Series Images (Video)
def read_time_series_images(filepath):
    video_frames = []
    cap = cv2.VideoCapture(filepath)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        video_frames.append(frame)
    cap.release()
    return video_frames

# 10. Reading Annotated Images (Assuming annotations are stored separately)
def read_annotated_image(filepath, annotations):
    image = cv2.imread(filepath, cv2.IMREAD_COLOR)
    for annotation in annotations:
        cv2.rectangle(image, annotation["start_point"], annotation["end_point"], (255, 0, 0), 2)
    return image

# 11. Reading Medical Images (e.g., DICOM files)
def read_medical_image(filepath):
    import pydicom
    ds = pydicom.dcmread(filepath)
    return ds.pixel_array

# 12. Reading Synthetic Images
def read_synthetic_image(filepath):
    return cv2.imread(filepath, cv2.IMREAD_COLOR)

# 13. Reading Point Cloud Images
def read_point_cloud(filepath):
    # Assuming a .ply file
    import open3d as o3d
    return o3d.io.read_point_cloud(filepath)

# 14. Reading Sparse Images
def read_sparse_image(filepath):
    return cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)

# 15. Reading Dense Optical Flow Images
def read_dense_optical_flow(video_filepath):
    cap = cv2.VideoCapture(video_filepath)
    ret, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    flow_images = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        flow_images.append(flow)
        prev_gray = gray
    cap.release()
    return flow_images
