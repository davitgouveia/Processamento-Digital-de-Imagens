import cv2
import numpy as np

# Read an image
img = cv2.imread('grama_nois_tres.jpeg')
print(img.shape)

blurred_image = cv2.GaussianBlur(img, (9, 9), 0)
hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

lower_hsv = np.array([18, 0, 0])
upper_hsv = np.array([74, 255, 255])

# Create a mask
mask = cv2.inRange(hsv, lower_hsv, upper_hsv)


# Invert the mask
inverted_mask = cv2.bitwise_not(mask)

# Segment the inverted region from the original image
segmented_image = cv2.bitwise_and(img, img, mask=inverted_mask)

cropped_image = segmented_image[120:650, 240:760]

cv2.imshow('RGB', img)
cv2.imshow('Segmentação', segmented_image)
cv2.imshow('Segmentação Cortada', cropped_image)

cv2.waitKey(0)



