import cv2
import numpy as np
import tkinter as tk
from tkinter import Scale

# Initialize HSV range values
hue_min, saturation_min, value_min = 24, 0, 0
hue_max, saturation_max, value_max = 180, 255, 255

# Function to update the segmented image
def update_segmentation():
    global hue_min, saturation_min, value_min, hue_max, saturation_max, value_max
    
    lower_hsv = np.array([hue_min, saturation_min, value_min])
    upper_hsv = np.array([hue_max, saturation_max, value_max])
    
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    inverted_mask = cv2.bitwise_not(mask)
    segmented_image = cv2.bitwise_and(img, img, mask=inverted_mask)
    
    # Crop the segmented image (if needed)
    cropped_image = segmented_image[120:650, 240:760]
    
    cv2.imshow('Segmentacao', segmented_image)

# Function to update HSV range values
# Function to update HSV range values
def update_hsv_values(_=None):  # Add _ as a default argument to ignore the argument passed by Scale widget
    global hue_min, saturation_min, value_min, hue_max, saturation_max, value_max
    hue_min = hue_min_scale.get()
    saturation_min = saturation_min_scale.get()
    value_min = value_min_scale.get()
    hue_max = hue_max_scale.get()
    saturation_max = saturation_max_scale.get()
    value_max = value_max_scale.get()
    
    update_segmentation()


# Read an image
img = cv2.imread('foto na escada.jpeg')
print(img.shape)

blurred_image = cv2.GaussianBlur(img, (9, 9), 0)
hsv = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

# Create the main window
root = tk.Tk()
root.title('HSV Segmentation')

# Create HSV range sliders
hue_min_scale = Scale(root, label='Hue Min', from_=0, to=180, orient='horizontal', command=update_hsv_values)
hue_min_scale.set(hue_min)

saturation_min_scale = Scale(root, label='Saturation Min', from_=0, to=255, orient='horizontal', command=update_hsv_values)
saturation_min_scale.set(saturation_min)

value_min_scale = Scale(root, label='Value Min', from_=0, to=255, orient='horizontal', command=update_hsv_values)
value_min_scale.set(value_min)

hue_max_scale = Scale(root, label='Hue Max', from_=0, to=180, orient='horizontal', command=update_hsv_values)
hue_max_scale.set(hue_max)

saturation_max_scale = Scale(root, label='Saturation Max', from_=0, to=255, orient='horizontal', command=update_hsv_values)
saturation_max_scale.set(saturation_max)

value_max_scale = Scale(root, label='Value Max', from_=0, to=255, orient='horizontal', command=update_hsv_values)
value_max_scale.set(value_max)

# Place sliders on the GUI
hue_min_scale.pack()
saturation_min_scale.pack()
value_min_scale.pack()
hue_max_scale.pack()
saturation_max_scale.pack()
value_max_scale.pack()

# Initialize the segmentation
update_segmentation()

# Start the GUI main loop
root.mainloop()