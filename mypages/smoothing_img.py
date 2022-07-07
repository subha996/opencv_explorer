import cv2 as cv
import streamlit as st
import numpy as np
import description as dscr
import st_code as code
import utils 
from PIL import Image

def run_smoothing_img(img):
    st.markdown('<h3 style="text-align: center; color: red;">Smoothing Images</h3>', unsafe_allow_html=True)
    st.write(dscr.smoothing_images)
    # https://docs.opencv.org/3.4/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html
    filter_types = ["Average Blur", "Gaussian Blur", "Median Blur", "Bilateral Filter"]
    filter = st.selectbox("Select the Filter Type", options=filter_types)
    if filter == "Average Blur":
        kernel_size = st.number_input("Kernel Size", min_value=1, 
                        step=1, value = 3, help="Please select a kernel size")
        with st.spinner("please hold on while processing your image..."):
            smooth_img = cv.blur(img, ksize=(int(kernel_size), int(kernel_size)))
        st.image(smooth_img, caption="Average Blur", channels="BGR")

        # putting download link
        st.markdown(utils.get_image_download_link(smooth_img), unsafe_allow_html=True)
        
        st.write("Following code is used to perfom average bluring.")
        st.code(code.code_smoothing_avg, language="python")
        
    elif filter == "Gaussian Blur":
        kernel_size = st.number_input("Kernal Size(Please enter odd number only.)", 
                        min_value=1, step=2, value = 3, 
                        help="Please select a kernel size, Odd Number only")
        # checking for odd input
        if int(kernel_size) % 2 != 0:
            # https://docs.opencv.org/3.4/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html
            col1, col2 = st.columns(2)
            sigma_x = col1.number_input("Sigma X", min_value=0.0, 
                            help="Please enter sigma x value. \n The standard deviation in `X`.")
            sigma_y = col2.number_input("Sigma Y", min_value=0.0, 
                            help="Please enter sigma y value. \n The standard deviation in `Y`.")
            with st.spinner("please hold on while processing your image..."):
                smooth_img = cv.GaussianBlur(src=img, ksize=(int(kernel_size), int(kernel_size)), 
                                            sigmaX=sigma_x, sigmaY=sigma_y)
            st.image(smooth_img, caption="Gaussian Blur", channels="BGR")
            # putting download link
            st.markdown(utils.get_image_download_link(smooth_img), unsafe_allow_html=True)
            
            st.write("Following code is used to perform Gaussian blur")
            st.code(code.code_smoothing_gaussian, language="python")
        else:
            st.warning("Please enter ODD number only for kernel size")
    
    elif filter == "Median Blur":
        # https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9
        kernel_size = int(st.number_input("Kernel Size", min_value = 1, step=2, help="Please enter kernel size"))
        # checking for odd
        if kernel_size%2 !=0:
            with st.spinner("please hold on while processing your image..."):
                smooth_img = cv.medianBlur(img, ksize=kernel_size)
            st.image(smooth_img, caption="Median Blur", channels="BGR")
            
            # putting download link
            st.markdown(utils.get_image_download_link(smooth_img), unsafe_allow_html=True)
            
            st.write("Following code is used to perform Median Blur")
            st.code(code.code_smoothing_median, language = "python")
    
    elif filter == "Bilateral Filter":
        col1, col2 = st.columns(2)
        diameter = int(col1.number_input("Diameter", step=2))
        sigma_color = col2.number_input("Sigma Color")
        sigma_space = col1.number_input("Sigma Space")
        # border = col2.select_box("Border", options)
        with st.spinner("please hold on while processing your image..."):
            smooth_img = cv.bilateralFilter(src=img,
                                            d = diameter,
                                            sigmaColor=sigma_color,
                                            sigmaSpace=sigma_space,
                                            borderType=cv.BORDER_REPLICATE)
        st.image(smooth_img, caption="Bilateral Filter", channels="BGR")
        
        # putting download link
        st.markdown(utils.get_image_download_link(smooth_img), unsafe_allow_html=True)
        
        st.write("Following code is used to perform Bilateral Filter")
        st.code(code.code_smoothing_bilateral, language="python")
    st.write(dscr.descr_smoothing)