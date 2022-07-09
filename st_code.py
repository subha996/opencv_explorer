code_image_information = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")
height, width, channels = img.shape  # return (height, width, channels)

"""

code_image_grey = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")

# changing color of an image
gery_img = cv.cvtColor(img, 
                        cv.COLOR_BGR2GRAY)

# showing the image 
cv.imshow("image", gery_img)

# waiting for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows() # destroy all windows

"""

code_image_resize_1 = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")

# resizing an image
resized_img = cv.resize(img, 
                        dsize = (width, height), 
                        interpolation=cv.INTER_AREA)

# showing the image 
cv.imshow("resize_image", resized_img)

# waiting for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows() # destroy all windows
"""

code_image_resize_2 = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")

# resizing an image
resized_img = cv.resize(img, 
                        fx, 
                        fy, 
                        interpolation=cv.INTER_AREA)

# showing the image 
cv.imshow("resize_image", resized_img)

# waiting for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows() # destroy all windows
"""

code_image_morhpology = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")

kernel_size = (kernel, kernel) # tuple of integers. usually range 1 to 10, 
iterations = 3 # some integer vlaue. usually range 1 to 5
morph_img = cv.morphologyEx(img, 
                            op = morph_options, # select from `Morph Type` drop down menu.
                            kernel=kernel_size, 
                            iterations=iterations)

# showing the image 
cv.imshow("morph_image", morph_img)

# waiting for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows() # destroy all windows

"""

code_smoothing_avg = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")


smooth_img = cv.blur(img, 
                    ksize=(kernel_size, kernel_size))

# showing the image 
cv.imshow("Smooth img", smooth_img)

# waiting for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows() # destroy all windows

"""

code_smoothing_gaussian = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")


smooth_img = cv.GaussianBlur(src=img, 
                             ksize=(int(kernel_size), int(kernel_size)), 
                             sigmaX=sigma_x, sigmaY=sigma_y)

# showing the image 
cv.imshow("Smooth img", smooth_img)

# waiting for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows() # destroy all windows
"""
code_smoothing_median = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")

kernel = (kernel_size, kernel_size) # tuple of integers
smooth_img = cv.medianBlur(src=img, 
                             ksize=kernel,)

# showing the image 
cv.imshow("Smooth img", smooth_img)

# waiting for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows() # destroy all windows
"""

code_smoothing_bilateral = """
import cv2 as cv

# reading the image file
img = cv.imread("./filePath")

kernel = (kernel_size, kernel_size) # tuple of integers
smooth_img = cv.bilateralFilter(src=img,
                            d = diameter,
                            sigmaColor=sigma_color,
                            sigmaSpace=sigma_space,
                            borderType=cv.BORDER_REPLICATE)

# showing the image 
cv.imshow("Smooth img", smooth_img)

# waiting for a key to be pressed
cv.waitKey(0)
cv.destroyAllWindows() # destroy all windows
"""

code_color_detection = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# converting image into hsv color space
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# defining color range of yellow color
lower_yellow = np.array([25, 50, 70])
upper_yellow = np.array([35, 255, 255])

# creating mask for the image
mask = cv.inRange(hsv_img, lower_range, upper_range) 

# performing bitwise operation on image
res_img = cv.bitwise_and(img, img, mask=mask)

# showing the image
cv.imshow("Original Image", img)
cv.imshow("Result Image(only yellow)", res_img)

cv.waitKey(0)
cv.destroyAllWindows()

"""

code_draw_text_Line = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# defining starting and ending point of the line
pt1 = (50, 75) # (x, y) starting point :: any desired number within range of image pixcel.
pt2 = (100, 80) # (x, y) ending point

# color of the line, tuple of three integer range from 0 to 255
color = (0, 255, 0) # (B, G, R) :: Green color line.

# thickness of the line
thickness = 4 # any integer between above 0

# drwaing line on the image.
line = cv.line(img, pt1 = (p1x,p1y),
             pt2 = (p2x, p2y),
             color = color,
             thickness = thickness)

# showing the image
cv.imshow("Result Image", line)

cv.waitKey(0)
cv.destroyAllWindows()

"""

code_draw_text_Circle = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# defining center point of the circle on the image.
center = (50, 100) # tuple of integers, :: any integer within height and width.

# defining radius of the circle on the image
radius = 4 # any integer above or equal 0

# defining color of the circle on the image
color = (255, 0, 0) # (B, G, R), tuple of three integer range from 0 to 255 

# defining thickness of the circle on the image
thickness = 2 # any integer above or equal 0, -1 will fill the circle.

# drwaing circle on the image.
circle = cv.circle(img, 
                center=center,
                radius=radius,
                color=color,
                thickness=thickness)

# showing the image
cv.imshow("Result Image", circle)

cv.waitKey(0)
cv.destroyAllWindows()

"""

code_draw_text_Rectangle = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# defining first point (top left corner of the rectangle)
pt1 = (50, 80) # any integer within height and width.

# defining second point (bottom left corner)
pt2 = (80, 100) # any integer within height and width

# defining color of the circle on the image
color = (255, 0, 0) # (B, G, R), tuple of three integer range from 0 to 255

# defining thickness of the circle on the image
thickness = 2 # any integer above or equal 0, -1 will fill the circle.

# drawing rectangle
rectangle = cv.rectangle(img, 
                    pt1 = pt1,
                    pt2 = pt2,
                    color=color,
                    thickness=thickness)

# showing the image
cv.imshow("Result Image", rectangle)

cv.waitKey(0)
cv.destroyAllWindows()

"""

code_draw_text_Ellipse = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# defining center coordinates of the ellipse
centerCoordinates = (50, 80) # tuple of integers.

# defining axes lenght
axisLength = (80, 40) # tuple of integers 

# defining angle of the ellipse
angle = 45 # degrees integer

# defining start and end angle
startAngle = 0 # any integer
endAngle = 0 # any integer

# defining color of the ellipse on the image
color = (255, 0, 0) # (B, G, R), tuple of three integer range from 0 to 255

# defining thickness of the ellipse on the image
thickness = 2 # any integer above or equal 0, -1 will fill the ellipse.


# drawing the ellipse
rellipse = cv.ellipse(img,
                center=centerCoordinates,
                axes=axesLength,
                angle=angle,
                startAngle=startAngle,
                endAngle=endAngle,
                color=color,
                thickness=thickness)

# showing the image
cv.imshow("Result Image", rectangle)

cv.waitKey(0)
cv.destroyAllWindows()

"""


code_draw_text_Text = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# defining text, have to be string.
text = "Your name" # any string that come in your mind.

# defining org, bottom left corner of the text in the image.
org = (50, 80) #x, y

# defining font type
# https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#ga0f9314ea6e35f99bb23f29567fc16e11
font = cv.FONT_HERSHEY_SIMPLEX # others font can be found in doc page.

# defining fontscale, higer number will lead bigger text size.
fontscale = 5 # any integer number.

# defining line type
# https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#gaf076ef45de481ac96e0ab3dc2c29a777
linetype = cv.FILLED # other line type can be found doc page.

# defining color of the text on the image
color = (255, 0, 0) # (B, G, R), tuple of three integer range from 0 to 255

# defining thickness of the text on the image
thickness = 2 # any integer above or equal 0

# putting text on image.
text = cv.putText(img,
                text=text,
                org=org,
                fontFace= font,
                fontScale=font_scale,
                lineType=line_type,
                thickness=thickness,
                color=(B, G, R))


# showing the image
cv.imshow("Result Image", text)

cv.waitKey(0)
cv.destroyAllWindows()
"""


code_edge_detection_sobel = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# transforming image into blur and greyscale
# open cv  requir grey image to perform edge detection.
img_gery = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_grey, (3, 3), 0 ) # 3x3 kernel filter, sigmax=0

# defining kernel depth
ddpeth = cv.CV_64F 

dx = 1 # order of the derivative x 1 or 0
dy = 0 # order of the derivative y 1 or 0

# defining kernel size
ksize = 3 # any integer

# performing edge detection on X axis
edge_x = cv.Sobel(img_blur,
                ddepth=cv.CV_64F,
                dx=dx, 
                dy=dy,
                ksize=kernel_size
                )

# inorder to  perform y axis edge detection 
# change dx to 0 and dy is 1.
dx = 0
dy = 1

# performing edge detection on X axis
edge_y = cv.Sobel(img_blur,
                ddepth=cv.CV_64F,
                dx=dx, 
                dy=dy,
                ksize=kernel_size
                )


# Showing images.
cv.imshow("Original Image", img)
cv.imshow("X axis edge detection", edge_x) 
cv.imshow("Y axis edge detection", edge_y)

cv.waitKey(0)
cv.destroyAllWindows()

"""

code_edge_detection_canny = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# transforming image into blur and greyscale
# open cv  requir grey image to perform edge detection.
img_gery = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_grey, (3, 3), 0 ) # 3x3 kernel filter, sigmax=0

# defining threshold for edge detection
threshold1 = 100 # any integer value
threshold2 = 200 # any integer value 

edge = cv.Canny(img_blur, 
                threshold1=threshold1,
                threshold2=threshold2)

# Showing images.
cv.imshow("Original Image", img)
cv.imshow("X axis edge detection", edge) 

cv.waitKey(0)
cv.destroyAllWindows()

"""

# code_denoising = """


# """

code_histo_equ = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# histogram equalization required grayscale image as input
grey = cv.cvtColor(img, cv.COLOR_BGR2GREY)

# performing equalization
hist_equ = cv.equalizeHist(grey)

# showing the image
cv.imshow("Hist equa image", hist_equ)

cv.waitKey(0)
cv.destroyAllWindows()

"""
code_histo_equ_clahe = """
import cv2 as cv
import numpy as np

# reading the image file
img = cv.imread("./filePath")

# histogram equalization required grayscale image as input
grey = cv.cvtColor(img, cv.COLOR_BGR2GREY)

# create a CLAHE object 
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) # can set any parameter
clahe_img = clahe.apply(grey)

# showing the image
cv.imshow("Clahe image", clahe_img)

cv.waitKey(0)
cv.destroyAllWindows()

"""

code_threshold = """

# reading the the image
img = cv.imread("./filePath")

# threhlding can not work on color image, so convert it to grayscale.
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# thresholding
ret, thresh = cv.threshold(grey,
                            thresh=127, # can be any value between 0 and 255
                            maxval=255, # can be any value between 0 and 255
                            type=cv.THRESH_BINARY) # other type of thresholding can be found in doc page.


# showing the image
cv.imshow("Threshold image", thresh)

cv.waitKey(0)
cv.destroyAllWindows()

"""