from ctypes import util
import streamlit as st
import cv2 as cv
import numpy as np
import description as dscr
import st_code as code
import utils 
from PIL import Image
import os

def img_informaton(img):
    """
    return shape, size 
    """
    return img.shape, img.size


def run_img_info(img):
    
    # main page starting.
    st.markdown('<h3 style="text-align: center; color: red;">Uploaded Image Information.</h3>', unsafe_allow_html=True)
    # getting image information, shape, size
    shape, size = img_informaton(img)
    st.write("Image Information:")
    st.write("Shape:", str(shape))
    st.write("Size:", str(size) + "(Total pixels)")
    col1, col2, col3 = st.columns(3) 
    col1.write("Image Width(x): " + str(img.shape[1]))
    col2.write("Image Height(Y): " + str(img.shape[0]))
    col3.write("Image Channels: " + str(img.shape[2]))
    st.image(img, caption="Original Image", channels="BGR")
    
    st.markdown(utils.get_image_download_link(img), unsafe_allow_html=True)
    
    # showing the code in webpage.
    st.write("Following code is used to Read an Image file.")
    st.code(code.code_image_information, language="python")
    st.markdown('<h5 style="text-align: center; color: red;">About a Digital Image</h5>', unsafe_allow_html=True)
    st.write(dscr.descr_image_info)
    # saving the image if keep is checked
    # utils.keep_image(keep, img)