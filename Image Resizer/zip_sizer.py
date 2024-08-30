import cv2
import zipfile
import glob
import os

# Extract images from the zip file
with zipfile.ZipFile("sample_images (1).zip", 'r') as zip_ref:
    zip_ref.extractall("extracted_images")

# Get the list of extracted image paths
image_paths = glob.glob("extracted_images/*.jpg")

# Resize and save each image
for path in image_paths:
    img = cv2.imread(path)
    resized_img = cv2.resize(img, (100, 100))  # Resize to 100x100
    cv2.imwrite("resized_" + os.path.basename(path), resized_img)
