import cv2 as cv
import example
import view
image = cv.imread('img.png')

# image is n-dimensional numpy array !
# print(type(image))

# lets know the shape of image
# it is a 3 dimensional 300x400x3
# print(image.shape)
# print(image)
#print(image.shape)
# cv.imshow(" ", image)
# cv.waitKey(0)
# cv.destroyAllWindows()

# print(image)

img = cv.cvtColor(image, cv.COLOR_BGR2RGB)


#view.viewImage(image, "image")
#print(image


#print(example.add(30 , 20))

cropped = image[0:200, 100:300]

bw = cv.cvtColor(cropped, cv.COLOR_BGR2RGB)
view.viewImage(bw, "cropped")