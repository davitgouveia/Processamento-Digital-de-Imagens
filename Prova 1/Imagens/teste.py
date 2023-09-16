

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('foto na grama.jpeg')
assert img is not None, "file could not be read, check with os.path.exists()"

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blurred_image = cv.GaussianBlur(gray, (21, 21), 0)

ret, thresh = cv.threshold(blurred_image,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

plt.imshow(thresh),plt.colorbar(),plt.show()