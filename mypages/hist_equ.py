from itertools import chain
import numpy as np
import cv2 as cv
import streamlit as st
import matplotlib.pyplot as plt
import utils
import st_code as code

def run_hist_equ(img):
    st.markdown('<h2 style="text-align: center; color: red;">Histogram Equalization</h2>', unsafe_allow_html=True)
    # getting  options from user
    col1, col2 = st.columns(2)
    equalizeHist = col1.checkbox("EqualizeHist", False, "equalizeHist")
    clahe_opt = col2.checkbox("Clahe", True, "clahe")

    # validating selection
    if equalizeHist and clahe_opt:
        st.warning("Please Select one options at a time")
    elif not equalizeHist and not clahe_opt:
        st.warning("Please Select one options from above.")

    elif equalizeHist:
        # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # getting the shape of the image.
        if len(img.shape) > 1 and img.shape[2] == 3: # detecting color images.
            B, G, R = cv.split(img)
            output_B = cv.equalizeHist(B)
            output_G = cv.equalizeHist(G)
            output_R = cv.equalizeHist(R)

            hist_img = cv.merge((output_B, output_G, output_R))
            # hist_img = cv.equalizeHist(img)
            st.image(hist_img, caption="EqualizeHist", channels="BGR")
            st.markdown(utils.get_image_download_link(hist_img), unsafe_allow_html=True)
            st.code(code.code_histo_equ, language="python")
        
        else : # whne single channel images has uploaded
            hist_img = cv.equalizeHist(img)
            st.image(hist_img, caption="EqualizeHist")
            st.markdown(utils.get_image_download_link(hist_img), unsafe_allow_html=True)
            st.code(code.code_histo_equ, language="python")
    
    elif clahe_opt:
        if len(img.shape) > 1 and img.shape[2] == 3: # detecting color images.
            # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            B, G, R = cv.split(img)

            col1, col2 = st.columns(2)
            clip_limit = float(col1.number_input("ClipLimit", min_value=0, max_value=100, value=5)) # input from user.
            grid = int(col2.number_input("Grid", min_value=1, max_value=100, value=7)) # input from user.
            tile_grid = (grid, grid) # creating grid tuple.
            clahe_ins = cv.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid)   
            output_B = clahe_ins.apply(B)
            output_G = clahe_ins.apply(G)
            output_R = clahe_ins.apply(R) 
            hist_img = cv.merge((output_B, output_G, output_R))
            st.image(hist_img, caption="Clahe", channels="BGR") 
            st.markdown(utils.get_image_download_link(hist_img), unsafe_allow_html=True)
            st.code(code.code_histo_equ_clahe, language="python")
