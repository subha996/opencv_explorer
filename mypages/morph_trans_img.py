import streamlit as st
import cv2 as cv
import numpy as np
import description as dscr
import st_code as code
import utils 
from PIL import Image

# https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
# https://docs.opencv.org/4.x/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f

def get_morphology_transformation_img(img, kernel_size, iterations, options):
    """
    Return morphological transformation from orginal image.
    https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
    """
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    if options == "MORPH_ERODE":
        op = cv.MORPH_ERODE
    elif options == "MORPH_DILATE":
        op = cv.MORPH_DILATE
    elif options == "MORPH_OPEN":
        op = cv.MORPH_OPEN
    elif options == "MORPH_CLOSE":
        op = cv.MORPH_CLOSE
    elif options == "MORPH_GRADIENT":
        op = cv.MORPH_GRADIENT
    elif options == "MORPH_TOPHAT":
        op = cv.MORPH_TOPHAT
    elif options == "MORPH_BLACKHAT":
        op = cv.MORPH_BLACKHAT
    elif options == "MORPH_HITMISS":
        op = cv.MORPH_HITMISS
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # HITMISS required grey image.

    return  cv.morphologyEx(img, 
                            op = op,
                            kernel=kernel, 
                            iterations=iterations)


def run_morph_trans_img(img):
    st.markdown('<h3 style="text-align: center; color: red;">Morphological Transformations</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    # list of morph types
    morphtypes = ["MORPH_ERODE", "MORPH_DILATE", 
                    "MORPH_OPEN", "MORPH_CLOSE", 
                    "MORPH_GRADIENT", "MORPH_TOPHAT", 
                    "MORPH_BLACKHAT", "MORPH_HITMISS"]
    morph_type = st.selectbox("Morph Type", morphtypes, help="Select which morphology transformation will apply.")
    iterations = col1.slider("choose Iterations", min_value=1, max_value=10, value = 3, step=1)
    kernel_size = col2.slider("Choose Kenel Size", min_value=1, max_value=10, value = 3, step=1)
    # Performing morph transformation.
    with st.spinner(text="Please wait while processing"):
        morphex_img = get_morphology_transformation_img(img, kernel_size, iterations, options=morph_type)
    # Showing the image.
    if morph_type == "MORPH_HITMISS": # solving morph hitmis bug
        st.image(morphex_img, caption="Morph Image") # without channel
    else:
        st.image(morphex_img, caption="Morph Images", channels="BGR")
    # putting download link
    st.markdown(utils.get_image_download_link(morphex_img), unsafe_allow_html=True)
    
    st.write("Following Code is Used to Change Morphology Transformation")
    st.code(code.code_image_morhpology, language="python")
    st.markdown('<h5 style="text-align: center; color: red;">About Morphological Transformations</h5>', unsafe_allow_html=True)
    st.write(dscr.descr_morph)