import cv2
import numpy as np

# Read an image
img = cv2.imread('foto no muro.jpeg')
print(img.shape)

blurred_image = cv2.GaussianBlur(img, (9, 9), 0)
hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)


# Mask da Roupa
lower_hsv_roupa = np.array([0, 0, 0])
upper_hsv_roupa = np.array([24, 255, 255])
maskRoupa = cv2.inRange(hsv, lower_hsv_roupa, upper_hsv_roupa)

# Mask da Pele
lower_hsv_pele = np.array([11, 0, 0])
upper_hsv_pele = np.array([24, 255, 255])
maskPele = cv2.inRange(hsv, lower_hsv_pele, upper_hsv_pele)

# Masks combinadas
combined_mask = cv2.bitwise_and(maskRoupa, maskPele)

inverted_mask = cv2.bitwise_not(combined_mask)

# Segmentando com as Masks
segmented_image = cv2.bitwise_and(img, img, mask=inverted_mask)


cv2.imshow('RGB', img)
cv2.imshow('HSV', hsv)
cv2.imshow('Segmentada', segmented_image)

cv2.waitKey(0)