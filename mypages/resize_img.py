import streamlit as st
import cv2 as cv
import numpy as np
import description as dscr
import st_code as code
import utils 
from PIL import Image


def get_resize_img(resize_option, img, size: tuple, fx: float, fy: float, interpolation):
    """
    Rsize the image to the given size or given scaling factor.

    """
    if interpolation == "INTER_NEAREST":
        inter = cv.INTER_NEAREST
    elif interpolation == "INTER_LINEAR":
        inter = cv.INTER_LINEAR
    elif interpolation == "INTER_CUBIC":
        inter = cv.INTER_CUBIC
    elif interpolation == "INTER_AREA":
        inter = cv.INTER_AREA
    elif interpolation == "INTER_LANCZOS4":
        inter = cv.INTER_LANCZOS4
    elif interpolation == "INTER_LINEAR_EXACT":
        inter = cv.INTER_LINEAR_EXACT
    elif interpolation == "INTER_NEAREST_EXACT":
        inter = cv.INTER_NEAREST_EXACT
    # elif interpolation == "INTER_MAX":
    #     inter = cv.INTER_MAX
    # elif interpolation == "WARP_FILL_OUTLIERS":
    #     inter = cv.WARP_FILL_OUTLIERS
    # elif interpolation == "WARP_INVERSE_MAP":
    #     inter = cv.WARP_INVERSE_MAP

    if resize_option == "wh":
        return cv.resize(
            img, 
            dsize=size,
            interpolation=inter
        )
    elif resize_option == "scf":
        return cv.resize(img, 
                        None, 
                        fx=fx, 
                        fy=fy, 
                        interpolation=inter)


def run_resize_img(img):
    # # validating if load is checked
    # if load: 
    #     img = utils.get_keep_image()
    # else:
    #     img = img

    st.markdown('<h2 style="text-align: center; color: red;">Resize Image</h2>', unsafe_allow_html=True)
    st.write("Original size:-" +  "\n" + "Width: " + str(img.shape[1]) + " Height: " + str(img.shape[0]))
    col1, col2 = st.columns(2)
    wh = col1.checkbox("Resize with Width and Height", value=True, key="wh")
    scf = col2.checkbox("Resize with Scaling Factor", value=False, key = "scf")
    if wh and scf:
        st.warning("Plase selcet one option at a time")
    elif not wh and not scf:
        st.warning("Please select Resize option from above.")
    elif wh: # user chose width and height
        scf = False
        st.write("Resize image by specifying the width and height")
        interpolation_types = ["INTER_NEAREST", "INTER_LINEAR", 
                                "INTER_CUBIC", "INTER_AREA", 
                                "INTER_LANCZOS4", "INTER_LINEAR_EXACT", 
                                "INTER_NEAREST_EXACT", 
                                # "INTER_MAX", "WARP_FILL_OUTLIERS", "WARP_INVERSE_MAP"]
        ]       
        col1, col2 = st.columns(2)
        width = col1.number_input("Width", value=100, step=1, help = "Enter Width to resize")
        heigth = col2.number_input("Height", value=100, step=1, help= "Enter Height to resize")
        # https://docs.opencv.org/4.x/da/d54/group__imgproc__transform.html#gga5bb5a1fea74ea38e1a5445ca803ff121ac97d8e4880d8b5d509e96825c7522deb
        interpolation = st.selectbox("Interpolation", options=interpolation_types, 
                                help="Select the Interpolation will be apply.")
        with st.spinner("please hold on while processing your image..."):
            resize_image = get_resize_img("wh", img, 
                            (int(width), int(heigth)),
                            fx=None, fy=None, 
                            interpolation=interpolation)
        st.image(resize_image, caption="Resize Image", channels="BGR")
        
        # saving the image if keep is checked
        # utils.keep_image(keep, resize_image) # saving the modified image if keep is checked.
        
        col1, col2, col3 = st.columns(3) 
        col1.write("Image Width(x): " + str(resize_image.shape[1]))
        col2.write("Image Height(Y): " + str(resize_image.shape[0]))
        col3.write("Image Channels: " + str(resize_image.shape[2]))
        
        # putting download link
        st.markdown(utils.get_image_download_link(resize_image), unsafe_allow_html=True)
        
        st.write("Following Code is Used to Resize an Image")
        st.code(code.code_image_resize_1, language="python")
        st.markdown('<h5 style="text-align: center; color: red;">About Resizing an Image</h5>', unsafe_allow_html=True)
        st.write(dscr.descr_resize)
    
    elif scf:
        wh = True
        st.write("Resize image by specifying the width and height")
        interpolation_types = ["INTER_NEAREST", "INTER_LINEAR", 
                                "INTER_CUBIC", "INTER_AREA", 
                                "INTER_LANCZOS4", "INTER_LINEAR_EXACT", 
                                "INTER_NEAREST_EXACT", 
                                # "INTER_MAX", "WARP_FILL_OUTLIERS", "WARP_INVERSE_MAP"
                                ]
        col1, col2 = st.columns(2)
        fx = col1.number_input("fx", value = 0.5, step=0.01, help="Select the X axis scale factor")
        fy = col2.number_input("fy", value = 0.5, step=0.01, help="Select the Y axis scale factor")
        interpolation = st.selectbox("Interpolation", options=interpolation_types, 
                                    help="Select the Interpolation will be apply.")
        with st.spinner("please hold on while processing your image..."):
            resize_image = get_resize_img("scf", img, None, fx=float(fx), fy=float(fy), interpolation=interpolation)
        st.image(resize_image, "Resize Image", channels="BGR")
        
        # saving the image if keep is checked
        # utils.keep_image(keep, resize_image) # saving the modified image if keep is checked.
        
        col1, col2, col3 = st.columns(3) 
        col1.write("Image Width(x): " + str(resize_image.shape[1]))
        col2.write("Image Height(Y): " + str(resize_image.shape[0]))
        col3.write("Image Channels: " + str(resize_image.shape[2]))
        
        st.markdown(utils.get_image_download_link(resize_image), unsafe_allow_html=True)
        
        st.write("Following Code is Used to Resize an Image")
        st.code(code.code_image_resize_2, language="python")
        st.markdown('<h5 style="text-align: center; color: red;">About Resizing an Image</h5>', unsafe_allow_html=True)
        st.write(dscr.descr_resize) 
    else:
        # st.image(img, "Original Shape")
        pass
