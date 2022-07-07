import numpy as np
from PIL import Image
import cv2 as cv
import base64
from io import BytesIO
import os

def get_image_download_link(img):

    """
    Generates a link allowing the PIL image to be downloaded
    in:  PIL image
    out: href string
    """
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}" download ="result.jpg">Download Image</a>'
    return href

# convert streamlit file buffer to nd array
def buffer2array(bufferfile):
    img = Image.open(bufferfile)
    return np.array(img)
 
def keep_image(keep, img):
    """  Function to save image file.
    """
    if keep:
        keep_path = os.path.join("keep", "keep_image.jpg")
        cv.imwrite(keep_path, img)

def get_keep_image():
    """Function to load keep image file from local dir
    """
    keep_path = os.path.join("keep", "keep_image.jpg")
    return cv.imread(keep_path, -1) # loading with untouched.
