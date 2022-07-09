from xml.dom.expatbuilder import theDOMImplementation
import streamlit as st
import cv2 as cv
import st_code as code


# reading the img
# img = cv.imread("./images/avg2.jpg")

def thresholding(img):
    # heading
    st.markdown('<h3 style="text-align: center; color: red;">Thresholding</h3>', unsafe_allow_html=True)

    # columns
    col1, col2 = st.columns(2)

    keep_color = col1.checkbox("Keep color image", value=False, key="keep color")
    t_type_input  = col2.selectbox("Select the threshold type", 
                            options=["THRESH_BINARY", "THRESH_BINARY_INV",
                            "THRESH_TRUNC", "THRESH_TOZERO", "THRESH_TOZERO_INV"])

    thresh_value = col1.slider("Threshold Value", min_value=0, max_value=255, value=140, key="thres", help="Select the threshold value")
    max_value = col2.slider("Max value", min_value=0, max_value=255, value=255, key="max_", help="Max value, will be put if pixel value is above threshold value")

    # select the threshold type
    if  t_type_input == "THRESH_BINARY":
        thresh_type = cv.THRESH_BINARY
    elif t_type_input == "THRESH_BINARY_INV":
        thresh_type = cv.THRESH_BINARY_INV
    elif t_type_input == "THRESH_TRUNC":
        thresh_type = cv.THRESH_TRUNC
    elif t_type_input == "THRESH_TOZERO":
        thresh_type = cv.THRESH_TOZERO
    elif t_type_input == "THRESH_TOZERO_INV":
        thresh_type = cv.THRESH_TOZERO_INV

    # threshlding
    if keep_color: # user choose to keep the color image
        # spliting each channel
        B, G, R = cv.split(img)
        retB, thresB = cv.threshold(src=B,
                                    type=thresh_type,
                                    thresh=int(thresh_value),
                                    maxval=int(max_value))
        retG, thresG = cv.threshold(src=G,
                                    type=thresh_type,
                                    thresh=int(thresh_value),
                                    maxval=int(max_value))

        retR, thresR = cv.threshold(src=R,
                                    type=thresh_type,
                                    thresh=int(thresh_value),
                                    maxval=int(max_value))
        # merging the imgae
        thres_img = cv.merge((thresB, thresG, thresR))
        st.image(thres_img, caption="Thresholded image", channels="BGR")
        st.write("Follwing code can be used to threshold the image:")
        st.code(code.code_threshold, language="python")
    else: # user choose to keep the gray image
        grey  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        ret, thres = cv.threshold(src=grey,
                                    type=thresh_type,
                                    thresh=int(thresh_value),
                                    maxval=int(max_value))
        st.image(thres, caption="Thresholded image")
        st.write("Follwing code can be used to threshold the image:")
        st.code(code.code_threshold, language="python")




