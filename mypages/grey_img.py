import streamlit as st
import cv2 as cv
import numpy as np
import description as dscr
import st_code as code
import utils 
from PIL import Image

def convert_grey(img):
    """function to convert color image to grey image"""
    return cv.cvtColor(img, 
                        cv.COLOR_BGR2GRAY)


def run_grey_img(img):
    # # validating if load is checked
    # if load: 
    #     img = utils.get_keep_image()
    # else:
    #     img = img

    st.markdown('<h3 style="text-align: center; color: red;">Grey Image</h3>', unsafe_allow_html=True)
    with st.spinner("please hold on while processing your image..."):
        grey_image = convert_grey(img) # transforming into grey image.
    st.image(grey_image, caption="Grey Image")
    
    # saving the image if keep is checked
    # utils.keep_image(keep, img)
    
    col1, col2, col3 = st.columns(3) 
    col1.write("Image Width(x): " + str(img.shape[1]))
    col2.write("Image Height(Y): " + str(img.shape[0]))
    col3.write("Image Channels: " + str(img.shape[2]))
    st.markdown(utils.get_image_download_link(grey_image), unsafe_allow_html=True)
    st.write("Following Code is Used to Convert an Image into Grey Image.")
    st.code(code.code_image_grey, language="python")
    st.markdown('<h5 style="text-align: center; color: red;">About Grey Image.</h5>', unsafe_allow_html=True)
    st.write(dscr.descr_grey, language="python")