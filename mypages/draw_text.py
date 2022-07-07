import cv2 as cv
from cv2 import line
import streamlit as st
import numpy as np
# import description as dscr
# import st_code as code
import utils 
from PIL import Image
import st_code as code

# https://opencv-tutorial.readthedocs.io/en/latest/draw/draw.html#using-numpy
def run_draw_text(img):
    # getting coordinates of the image
    st.markdown('<div style="text-align: center; color: red;">Draw and Text</div>', unsafe_allow_html=True)
    xmin, ymin, xmax, ymax = 1, 1, int(img.shape[1]), int(img.shape[0])

    # getting options for drawing and text
    # col1, col2 = st.columns(2)


    dt_opt_list = ["Line", "Circle", "Rectangle", "Ellipse", "Text"]
    # input options.
    dt_opt = st.selectbox("Select the options for drawing and textig", dt_opt_list)

    if dt_opt == "Line":
        # select points 
        col1, col2,col3, col4 = st.columns(4)
        # NOTE: opencv shape: (height, width, channel) 
        p1x = int(col1.slider("Define point P1X(X1)", min_value=xmin, max_value=xmax,value=int(xmax/2 - 10), key="p1x", 
        help = "X position for point 1"))
        p1y = int(col2.slider("Define point P1Y(Y1)", min_value=ymin, max_value=ymax, value =int(ymax/2 -10), key="p1y",
        help = "Y position for point 1"))
        p2x = int(col3.slider("Define point P2X(X2)", min_value=xmin, max_value=xmax,value=int(xmax/2 + 10), key="p2x",
        help = "X position for point 2"))
        p2y = int(col4.slider("Define point P2Y(Y2)", min_value=ymin, max_value=ymax, value =int(ymax/2 + 10), key="p2y",
        help = "Y position for point 2"))
        # input color
        col1, col2, col3 = st.columns(3)
        B = col1.slider("Blue", min_value=0, max_value=255, key="blue_ln")
        G = col2.slider("Green", min_value=0, max_value=255, key="green_ln")
        R = col3.slider("Red", min_value=0, max_value=255, value=255, key="red_ln")
        # define thickness
        thickness = st.slider("Select Thickness of the image", min_value=1, max_value=50,value = 4, key="thickness_ln")
        # drwaing line
        with st.spinner("Drwaing your line..."):
            res = cv.line(img, pt1=(p1x,p1y),
                                pt2 =(p2x, p2y),
                                color=(B, G, R),
                                thickness= thickness)
        # shwoing the image
        st.image(res, caption="Draw on image", channels="BGR")

        # putting download link
        st.markdown(utils.get_image_download_link(res), unsafe_allow_html=True)
        # showing code
        st.code(code.code_draw_text_Line, language="python")

    elif dt_opt == "Circle":
        # getting input for the position of the circle
        col1, col2, col3, col4 = st.columns(4)
        
        cx = int(col1.slider("X Position of the circle", min_value=1, max_value=xmax,
        value=int(xmax/2),key="cx",
        help="`X` coordinate for circle radius"))
        
        cy = (col2.slider("Y Position of the circle", min_value=1, max_value=ymax,
        value = int(ymax/2), key="cy",
        help = "`Y` coordinate for circle radius."))
        
        # getting the radius and thickness
        radius = col3.slider("Radius", min_value=0, max_value=100, value=20, key="radius",
        help="Select the `Radius` of the circle.")
        thickness = col4.slider("Thickness", min_value=-1, max_value=50, value=4, key="thickness_cr",
        help="Select the `Thickness` of the circle.")
        # getting the color of the circle.
        col1, col2, col3 = st.columns(3)
        B = int(col1.slider("Blue", min_value=0, max_value=255, key="blue_cr"))
        G = int(col2.slider("Green", min_value=0, max_value=255, key="green_cr"))
        R = int(col3.slider("Red", min_value=0, max_value=255, value=255, key="red_cr"))
        # drwaing circle on the image.
        with st.spinner("Drwaing your line..."):
            res = cv.circle(img, 
                            center=(cx, cy),
                            radius=radius,
                            color=(B, G, R),
                            thickness=thickness)
        
        # showing the image
        st.image(res, caption="Circle Draw on Image", channels="BGR")

        # putting download link
        st.markdown(utils.get_image_download_link(res), unsafe_allow_html=True)
        # showing code
        st.code(code.code_draw_text_Circle, language="python")
    
    elif dt_opt == "Rectangle":
        # select points 
        col1, col2,col3, col4 = st.columns(4)
        # NOTE: opencv shape: (height, width, channel) 
        p1x = int(col1.slider("Define point P1X(X1)", min_value=xmin, max_value=xmax,value=int(xmax/2-10), key="p1x", 
        help = "X position for point 1"))
        p1y = int(col2.slider("Define point P1Y(Y1)", min_value=ymin, max_value=ymax, value =int(ymax/2-10), key="p1y",
        help = "Y position for point 1"))
        p2x = int(col3.slider("Define point P2X(X2)", min_value=xmin, max_value=xmax,value=int(xmax/2+10), key="p2x",
        help = "X position for point 2"))
        p2y = int(col4.slider("Define point P2Y(Y2)", min_value=ymin, max_value=ymax, value =int(ymax/2+10), key="p2y",
        help = "Y position for point 2"))
        # input color
        col1, col2, col3 = st.columns(3)
        B = col1.slider("Blue", min_value=0, max_value=255, key="blue_rc")
        G = col2.slider("Green", min_value=0, max_value=255, key="green_rc")
        R = col3.slider("Red", min_value=0, max_value=255, key="red_rc", value=255)
        # define thickness
        thickness = st.slider("Select Thickness of the image", min_value=1, max_value=50,  value=4, key="thickness_rc")

        # drawing rectangle
        with st.spinner("Drwaing your rectangle..."):
            res = cv.rectangle(img, 
                                pt1 = (p1x, p1y),
                                pt2 = (p2x, p2y),
                                color=(B, G, R),
                                thickness=thickness)
        st.image(res, channels="BGR", caption="Draw Rectangle")

        # putting download link
        st.markdown(utils.get_image_download_link(res), unsafe_allow_html=True)
        # showing code
        st.code(code.code_draw_text_Rectangle, language="python")

    elif dt_opt == "Ellipse":
        # https://www.geeksforgeeks.org/python-opencv-cv2-ellipse-method/
        # taking inputs parameters.
        
        # input parameters.
        col1, col2, col3, col4 = st.columns(4)
        x_cc = int(col1.slider("CenterCoordinates(X)", min_value=0, max_value=xmax, key="x_cc", value=int(xmax/2),
        help = "It is the center coordinates of ellipse. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value)."))
        y_cc = int(col2.slider("CenterCoordinates(Y)", min_value=0, max_value=ymax, key="y_cc", value=int(ymax/2),
        help="It is the center coordinates of ellipse. The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value)."))
        centerCoordinates = (x_cc, y_cc) # creating tupple of the position.

        # getting axislength
        x_ax = int(col3.slider("Axis Length(X)", min_value=0, max_value=xmax, key="x_ax", value=int(xmax/2-10),
        help="It contains tuple of two variables containing major and minor axis of ellipse (major axis length, minor axis length)."))
        y_ax = int(col4.slider("Axis Length(Y))", min_value=0, max_value=ymax, key="y_ax", value=int(ymax/2-10),
        help="It contains tuple of two variables containing major and minor axis of ellipse (major axis length, minor axis length)."))
        axesLength  = (x_ax, y_ax) # creating tuple for the axis lntgth.

        # getting stat and end angle.
        startAngle = int(col1.slider("Start angle", min_value=0, max_value= 360, value=0,
        help = "Starting angle of the elliptic arc in degrees"))
        endAngle = int(col2.slider("End angle", min_value=0, max_value= 360, value=360,
        help="Ending angle of the elliptic arc in degrees."))

        
        # getting the input angle degree
        angle = int(col3.slider("Rotation angle", min_value=0, max_value=360, key="ellipse_angle",
        help = "Ellipse rotation angle in degrees"))
        # define thickness
        thickness = col4.slider("Thickness", min_value=-1, max_value=50, key="thickness_rc", value=4,
        help="Thickness of the ellipse arc")
        # color.
        col1, col2, col3 = st.columns(3)
        B = col1.slider("Blue", min_value=0, max_value=255, key="blue_rc")
        G = col2.slider("Green", min_value=0, max_value=255, key="green_rc")
        R = col3.slider("Red", min_value=0, max_value=255, key="red_rc", value=255)
        
        # drawing the ellipse
        with st.spinner("Drawing your ellipse..."):
            res = cv.ellipse(img,
                            center=centerCoordinates,
                            axes=axesLength,
                            angle=angle,
                            startAngle=startAngle,
                            endAngle=endAngle,
                            color=(B, G, R),
                            thickness=thickness)

        #shwoing the image
        st.image(res, caption="Ellipse on Image", channels="BGR")
        
        # putting download link
        st.markdown(utils.get_image_download_link(res), unsafe_allow_html=True)
        # showing code
        st.code(code.code_draw_text_Ellipse, language="python")
    
    elif dt_opt == "Text":
        # https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
        # https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576
        text = st.text_input("Enter your text.")
        # define org
        col1, col2 = st.columns(2)
        x_org = col1.slider("org (X)", min_value=1, max_value=xmax, value=50, key="org x")
        y_org = col2.slider("org (Y)", min_value=1, max_value=ymax, value=50, key="org y")
        org = (x_org, y_org) #  making tuple of coordinate.
        
        col1, col2 = st.columns(2)
        # defining font of the text
        font_list = ["FONT_HERSHEY_SIMPLEX", "FONT_HERSHEY_PLAIN",
                    "FONT_HERSHEY_DUPLEX", "FONT_HERSHEY_COMPLEX",
                    "FONT_HERSHEY_TRIPLEX", "FONT_HERSHEY_COMPLEX_SMALL",
                    "FONT_HERSHEY_SCRIPT_SIMPLEX", "FONT_HERSHEY_SCRIPT_COMPLEX",
                    "FONT_ITALIC"]
        font_input = col1.selectbox("Select Font", font_list)
        # selct font face 
        if font_input == "FONT_HERSHEY_SIMPLEX":
            font = cv.FONT_HERSHEY_SIMPLEX
        elif font_input == "FONT_HERSHEY_PLAIN":
            font = cv.FONT_HERSHEY_PLAIN
        elif font_input == "FONT_HERSHEY_DUPLEX":
            font = cv.FONT_HERSHEY_DUPLEX
        elif font_input == "FONT_HERSHEY_COMPLEX":
            font = cv.FONT_HERSHEY_COMPLEX
        elif font_input == "FONT_HERSHEY_TRIPLEX":
            font = cv.FONT_HERSHEY_TRIPLEX
        elif font_input == "FONT_HERSHEY_COMPLEX_SMALL":
            font = cv.FONT_HERSHEY_COMPLEX_SMALL
        elif font_input == "FONT_HERSHEY_SCRIPT_SIMPLEX":
            font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
        elif font_input == "FONT_HERSHEY_SCRIPT_COMPLEX":
            font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
        elif font_input == "FONT_ITALIC":
            font = cv.FONT_ITALIC

        # define font scale
        font_scale = col2.slider("Font Scale", min_value=0, max_value=20, value=1)

        #define line thickness
        thickness = col1.slider("Thickness", min_value=1, max_value=50, value=2)

        #define line type
        line_type_list = ["FILLED", "LINE_4",
                        "LINE_8", "LINE_AA"]
        line_type_input = col2.selectbox("Line Type", line_type_list)
        if line_type_input == "FILLED":
            line_type = cv.FILLED
        elif line_type_input == "LINE_4":
            line_type = cv.LINE_4
        elif line_type_input == "LINE_8":
            line_type = cv.LINE_8
        elif line_type_input == "LINE_AA":
            line_type = cv.LINE_AA

        # color.
        col1, col2, col3 = st.columns(3)
        B = col1.slider("Blue", min_value=0, max_value=255, key="blue_rc")
        G = col2.slider("Green", min_value=0, max_value=255, key="green_rc")
        R = col3.slider("Red", min_value=0, max_value=255, key="red_rc")

        # putting text on Image"
        with st.spinner("Writing your text..."):
            res = cv.putText(img,
                            text=text,
                            org=org,
                            fontFace= font,
                            fontScale=font_scale,
                            lineType=line_type,
                            thickness=thickness,
                            color=(B, G, R))
        
        
        
        # shwing the image
        st.image(res, caption="Text on Image", channels="BGR")
        
        # putting download link
        st.markdown(utils.get_image_download_link(res), unsafe_allow_html=True)
        # showing code
        st.code(code.code_draw_text_Text, language="python")
