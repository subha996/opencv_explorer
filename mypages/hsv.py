import streamlit as st
import cv2 as cv
import numpy as np
import description, st_code
import utils

def hsv_run(img, manl, drop):
    # img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    st.markdown('<h3 style="text-align: center; color: red;">Color Detection</h3>', unsafe_allow_html=True)
    # img is defined.
    # creating color range dictionary
    # https://stackoverflow.com/questions/36817133/identifying-the-range-of-a-color-in-hsv-using-opencv
    color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
                'white': [[180, 18, 255], [0, 0, 231]],
                'red1': [[180, 255, 255], [159, 50, 70]],
                'red2': [[9, 255, 255], [0, 50, 70]],
                'green': [[89, 255, 255], [36, 50, 70]],
                'blue': [[128, 255, 255], [90, 50, 70]],
                'yellow': [[35, 255, 255], [25, 50, 70]],
                'purple': [[158, 255, 255], [129, 50, 70]],
                'orange': [[24, 255, 255], [10, 50, 70]],
                'gray': [[180, 18, 230], [0, 0, 40]]}

    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    col1, col2 = st.columns(2)

    # if manl and drop:
    #     st.warning("Please select one option at a time.")
    if manl and drop:
        st.warning("Please Select one option at a time")
        
    elif not manl and not drop:
        st.warning("Please Select option")
        
    elif  drop :
        manl = False
        color = st.selectbox("Select the Color", 
                            options=list(color_dict_HSV.keys()))
        upper_range = np.array(color_dict_HSV[color][0])
        lower_range = np.array(color_dict_HSV[color][1])

        # creating mask
        mask = cv.inRange(hsv_img, lower_range, upper_range)

        # performing bitwise operation on mask
        res_img = cv.bitwise_and(img, img, mask=mask)

        st.image(res_img, caption="Hsv Color image", channels="BGR")

        # putting download link
        st.markdown(utils.get_image_download_link(res_img), unsafe_allow_html=True)

        st.code(st_code.code_color_detection, language="python")
        st.write("Color Picker")
        src =  "https://www.tydac.ch/color/" # rendering third part website.
        st.components.v1.iframe(src, width=800, height=600, scrolling=True)
    
    elif manl:
        drop = False
        
        # getting lower hsv range from user
        st.write("Enter Lower HSV value")
        col1, col2, col3  = st.columns(3)
        hl = int(col1.slider("Hue (H)", min_value=0, max_value=179, value=179, key="hl")) # hue lower
        sl = int(col2.slider("Saturation(S)", min_value=0, max_value=255, value=255, key="sl")) # saturation lower
        vl = int(col3.slider("Value(V)", min_value=0, max_value=255, value=255, key="vl")) # value lower

        # getting upper hsv range from user
        st.write("Enter Highr HSV Value")
        col1, col2, col3  = st.columns(3)
        hu = int(col1.slider("Hue (H)", min_value=0, max_value=179, value=179, key="hu")) # hue upper
        su = int(col2.slider("Saturation(S)", min_value=0, max_value=255, value=255, key="su")) # saturation upper
        vu = int(col3.slider("Value(V)", min_value=0, max_value=255, value=255, key="vu")) # value upper


        # creating array of range
        lower_range = np.array([hl, sl, vl])
        upper_range = np.array([hu, su, vu])
        

        # creating mask
        with st.spinner("Please hold on while processing..."):
            mask = cv.inRange(hsv_img, lower_range, upper_range)
            res_img = cv.bitwise_and(img, img, mask=mask)

        st.image(res_img, caption="Hsv Color image", clamp=False, channels="BGR")
        # putting download link
        st.markdown(utils.get_image_download_link(res_img), unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        col1.write("Lower H: " + str(hl))
        col2.write("Lower S: " + str(sl))
        col3.write("Lower V: " + str(vl))

        col1.write("Higher H: " + str(hu))
        col2.write("Higher S: " + str(su))
        col3.write("Higer V: " + str(vu))
        # putting code
        st.code(st_code.code_color_detection, language="python")
        st.write("Color Picker")
        src =  "https://www.tydac.ch/color/" # rendering third part website.
        st.components.v1.iframe(src, width=800, height=600, scrolling=True)
    else:
        pass
    
    

        