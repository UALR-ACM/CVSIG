import cv2
import numpy as np
from matplotlib import pyplot as plt

#Loads an image into var img (-1 = IMREAD_UNCHANGED, 0 = IMREAD_GRAYSCALE, 1 = IMREAD_COLOR)
img = cv2.imread('lena.jpg', -1)
#img = cv2.imread('lena.jpg', 0)
#img = cv2.imread('lena.jpg', 1)

#draw a circle over the image
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

#add text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)


#image is the name of the window
cv2.imshow('image', img)

#save image
#cv2.imwrite('grayscale.jpg', img)

#use Matplot lib to display image in a different style of window
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()


#wait for keyboard input in milliseconds. If no key is pressed then proceed else loop. 0 is infinite.
cv2.waitKey(0)

#Destroy all windows opened. Can also use "cv2.destroyWindow('name of window')
cv2.destroyAllWindows()

