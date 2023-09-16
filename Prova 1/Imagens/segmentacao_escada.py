import cv2
import numpy as np

# Read an image
img = cv2.imread('foto na escada.jpeg')
print(img.shape)

blurred_image = cv2.GaussianBlur(img, (9, 9), 0)
hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)


# Mask da escada
lower_hsv_escada = np.array([8, 0, 0])
upper_hsv_escada = np.array([180, 255, 255])
maskescada = cv2.inRange(hsv, lower_hsv_escada, upper_hsv_escada)
inverted_mask_escada = cv2.bitwise_not(maskescada)

# Mask da Pele
lower_hsv_pele = np.array([19, 0, 0])
upper_hsv_pele = np.array([180, 255, 255])
maskPele = cv2.inRange(hsv, lower_hsv_pele, upper_hsv_pele)

# Mask da Roupa
lower_hsv_roupa = np.array([0, 0, 0])
upper_hsv_roupa = np.array([19, 255, 255])
maskroupa = cv2.inRange(hsv, lower_hsv_roupa, upper_hsv_roupa)

# Masks combinadas
combined_mask = cv2.bitwise_or(inverted_mask_escada, maskroupa)

combined_mask2 = cv2.bitwise_and(maskPele, combined_mask)

inverted_mask = cv2.bitwise_not(combined_mask2)

# Segmentando com as Masks
segmented_image = cv2.bitwise_and(img, img, mask=inverted_mask)


cv2.imshow('inverted_mask_escada', maskescada)
cv2.imshow('maskroupa', maskroupa)


cv2.waitKey(0)