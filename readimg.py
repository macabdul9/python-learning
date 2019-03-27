import numpy
import cv2

import matplotlib.pyplot as plt

image = cv2.imread('img.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(image)

cv2.imwrite('wimg.jpg', image)