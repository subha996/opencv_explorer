import streamlit as st
import numpy as np
import cv2 as cv
import utils
from PIL import Image
from io import BytesIO
import base64
import st_code as code

# solbel
# https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#gacea54f142e81b6758cb6f375ce782c8d
# https://learnopencv.com/edge-detection-using-opencv/


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


def edgedetection_run(img, option):
    # img = cv.cvtColor(img, cv.COLOR_RGB2BGR) # converting to BGR format.
    if option == "Sobel":
        # transforming image into blur and greyscale
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.GaussianBlur(img, (3, 3), 0 ) # 3x3 kernel filter, sigmax=0

        # taking input from user for edge axis.
        col1, col2, col3 = st.columns(3)
        sobelx_intput = col1.checkbox("Select for X axis", value=True, key="sobelx")
        sobely_input = col2.checkbox("Select for Y axis", value=False, key="sobely")
        # validating axis input
        if not (sobelx_intput or sobely_input):
            st.warning("Please select axis option.")

        kernel_size = int(col3.number_input("Selectc Kernel size", min_value=1, max_value=31, step=2))
        # getting the edge
        if sobelx_intput and sobely_input: # when both select.
            st.write("Performing for `Both` axis.")
            edge = cv.Sobel(img,
                            ddepth=cv.CV_64F,
                            dx=1, 
                            dy=1,
                            ksize=kernel_size
                            )
            st.image(edge, caption="Edge detection image.",  clamp=True)
            
            # showing the code
            st.code(code.code_edge_detection_sobel, language="python")
            # putting download link
            # st.markdown(get_image_download_link(edge), unsafe_allow_html=True)
        
        elif sobelx_intput: # when x axis is select.
            st.write("Performing `X` axis edge detection.")
            edge = cv.Sobel(img,
                            ddepth=cv.CV_64F,
                            dx=1,
                            dy=0,
                            ksize=kernel_size,
            )
            st.image(edge, caption="Edge detection image.",  clamp=True)
            # showing the code
            st.code(code.code_edge_detection_sobel, language="python")
            # putting download link
            # st.markdown(get_image_download_link(edge), unsafe_allow_html=True)
        
        elif sobely_input: # whne y axis is select.
            st.write("Performing `Y` axis edge detection.")
            edge = cv.Sobel(img,
                            ddepth=cv.CV_64F,
                            dx=0, 
                            dy=1,
                            ksize=kernel_size
                            )
            st.image(edge, caption="Edge detection image.",  clamp=True)
            # showing the code
            st.code(code.code_edge_detection_sobel, language="python")
            # putting download link
            # st.markdown(get_image_download_link(edge), unsafe_allow_html=True)
    
    elif option == "Canny":
        # transforming image into blur and greyscale
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.GaussianBlur(img, (3, 3), 0 ) # 3x3 kernel filter, sigmax=0
        col1, col2 = st.columns(2)
        thersh1 = col1.slider("First threshold for the hysteresis procedure",
                             min_value=1,
                             max_value=1000,
                             value=100,
                             key= "thresh1"
                             )
        thersh2 = col2.slider("Second threshold for the hysteresis procedure",
                            min_value=1,
                            max_value=1000,
                            key="thresh2")
        edge = cv.Canny(img, threshold1=thersh1,
                            threshold2=thersh2)
        st.image(edge, clamp=True) 
        # showing the code 
        st.code(code.code_edge_detection_canny, language="python")
        # putting download link
        # st.markdown(get_image_download_link(edge), unsafe_allow_html=True)