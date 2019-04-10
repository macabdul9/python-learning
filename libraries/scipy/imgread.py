import scipy.misc as sp
import matplotlib.pyplot as plt
img = sp.imread('cat.jpg')
#sp.imshow(img)
img = sp.imrotate(img, angle=90)
sp.imshow(img)