


dilation_descr = """
Dilation is one of morphological image processing operation, 
Dilation is a technique where we expand the image. It adds the number of pixels to the boundaries of objects in an image.
"""


smoothing_images = """

"""
descr_image_info = """
Image can be considered as a matrix size of width by height, each element called a pixel, \
each with finite, discrete quantities of numeric representation for its intensity. \
The matrix elements are arranged in an array of rows and columns that correspond   \ 
to the vertical and horizontal positions of the pixels in the image.
[More About Image](https://en.wikipedia.org/wiki/Digital_image)

"""
descr_grey = """
In digital images, grayscale means that the value of each pixel \
represents only the intensity information of the light. Simply specifying Black and White Imgae. \ 
In grayscale images, the value of each pixel is related to the number of bits of data used to represent the pixel.  \
The value of the gray image is usually represented by 8 bits, that is, the combination of eight binary numbers represents \
the pixel value of a pixel. 
[More About Image](https://en.wikipedia.org/wiki/Grayscale)
"""

descr_resize = """
 To resize an image, scale it along each axis (`height` and `width`), considering the specified scale factors or \
 just set the desired height and width.  

When resizing an image:
* It is important to keep in mind the original aspect ratio of the image (i.e. width by height), if you want to maintain the same in the resized image too.
* Reducing the size of an image will require resampling of the pixels. 
* Increasing the size of an image requires reconstruction of the image. This means you need to interpolate new pixels.

There are two options are available to resize an image 
* Resize with by specifying `Width` and `Height`.
* Resize with `Scaling Factor`.

[More About Resizing](https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html)
"""

descr_morph = """

Morphological Transformations are image processing methods that transform images based on shapes.
These transformations use a structuring element applied to the input image, \
and the output image is generated. Morphological operations have various uses, \
including removing noise from images, locating intensity bumps and holes in an image and \
joining disparate elements in images. 

There are two main types of Morphological Transformations, `Erosion`(`MORPH_ERODE`) and `Dilation`(`MORPH_DILATE`)  \
along with many other operations. you can explore various operation from `Morph Type` drop down menu from avobe.


[More About Morphological Transformations](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html)
"""
descr_smoothing = """
Smoothing an image or Blurring is another image transformation technique is widely used in Image Processing.
Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful for removing noise. \
It actually removes high frequency content (eg: noise, edges) from the image. So edges are blurred a little bit in this \
operation (there are also blurring techniques which don't blur the edges). OpenCV provides four main types of blurring techniques.

There are mainly 4 types of blurring methods, 
* Average Blur 
* Gaussian Blur
* Median Blur
* Bilateral Filter

Note that `kernel` size must be `ODD` number to choose.
"""

descr_color_detection = """

"""

descr_edge_detection = """

"""

descr_denoising = """

"""

descr_histo_equ = """

"""