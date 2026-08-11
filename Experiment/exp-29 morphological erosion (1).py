import cv2
import numpy as np

img = cv2.imread('image.jpg', 0)   # grayscale

if img is None:
    print("Error: Image not found")
    exit()

kernel = np.ones((5,5), np.uint8)