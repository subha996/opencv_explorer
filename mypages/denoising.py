# https://docs.opencv.org/4.x/d5/d69/tutorial_py_non_local_means.html
import cv2 as cv
from cv2 import hconcat
from cv2 import CV_8UC3
import numpy as np


# reading an image
img = cv.imread("./images/salt_noise.jpg")

img = cv.cvtColor(img, CV_8UC3)
dst = cv.fastNlMeansDenoisingColored(img,None,
                                    templateWindowSize=7,
                                    searchWindowSize=21,
                                    h=10,
                                    hColor=10)

cv.imshow("original", img)
cv.imshow("Denoising", dst)

cv.waitKey(0)
cv.destroyAllWindows()

### INACTIVE ##################