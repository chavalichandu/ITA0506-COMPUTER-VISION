import cv2

img = cv2.imread('image.jpg')

# Crop region
crop = img[50:200, 50:200]

# Paste to another location
img[250:400, 250:400] = crop

cv2.imshow("Crop & Paste", img)
cv2.waitKey(0)
cv2.destroyAllWindows()