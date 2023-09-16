import cv2
import numpy as np

# Read an image
img = cv2.imread('foto no espelho.jpeg')
print(img.shape)

blurred_image = cv2.GaussianBlur(img, (9, 9), 0)
hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

lower_hsv = np.array([13, 0, 180])
upper_hsv = np.array([124, 255, 255])

# Create a mask
mask = cv2.inRange(hsv, lower_hsv, upper_hsv)


# Invert the mask
inverted_mask = cv2.bitwise_not(mask)

# Segment the inverted region from the original image
segmented_image = cv2.bitwise_and(img, img, mask=inverted_mask)

cropped_image = segmented_image[180:1024, 140:730]

cv2.imshow('RGB', img)
cv2.imshow('Segmentacao', segmented_image)
cv2.imshow('Segmentacao Cortada', cropped_image)

cv2.waitKey(0)