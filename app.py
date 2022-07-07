import cv2 as cv
import streamlit as st
import utils 
from mypages.img_info import run_img_info
from mypages.hsv import hsv_run
from mypages.edge_dect import edgedetection_run
from mypages.hist_equ import run_hist_equ
from mypages.resize_img import run_resize_img
from mypages.grey_img import run_grey_img
from mypages.morph_trans_img import run_morph_trans_img
from mypages.smoothing_img import run_smoothing_img
from mypages.draw_text import run_draw_text

# setting the page icon
st.set_page_config(page_title='Open-CV Explorer',page_icon="screensicon\opencv-icon.png" ,layout = 'centered', initial_sidebar_state = 'auto')

# reading the image from user input.
# st.markdown('<div style="text-align: center; color: red;">Dilation</div>', unsafe_allow_html=True)
buffer = st.sidebar.file_uploader("Please Upload File", type=["jpg", "png"])

# providing different options for image processing.
options = ["Show Image Information", "Grey Image", 
            "Resize Image", "Draw and Text" ,"Morphological Transformations", 
            "Smoothing Images", "Color Detection(HSV)", 
            "Edge Detection", "Histogram Equalization",
        ]
opt = st.sidebar.selectbox("Select options from here.", options)

# keep = st.sidebar.checkbox("Keep Image on Memory", value=False, key="keep", 
#     help = "Check if you wamt to keep the image on memory and load on other page.")
# load = st.sidebar.checkbox("Load Previous keep Image", value = False, key="load",
#     help="Check if you wamt to load the previous saved image")
# keep = None # temporary variable
# load = None # temporary variable

# getting the image
if buffer is not None: 
    img = utils.buffer2array(buffer) # converting into array.
    st.sidebar.image(img, caption="Original Image")
    # converting image into BGR format
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR) # convert to RGB format
else:
    suflw = st.sidebar.checkbox("Use Sunflower Image !!", key="sunf", value=False)
    if suflw: 
        img = cv.imread("./images/sunflower.jpg")
        buffer = img.copy()
        st.sidebar.image(img, caption="Sunflower", channels="BGR")
    if buffer is None:
        st.markdown('<h2 style="text-align: center; color: red;">Open CV Explorer</h2>', unsafe_allow_html=True)
        st.sidebar.write("Nothing to show here, No file is uploaded")
        st.warning("Please Upload a Image file to Start")
        # shwoing sample image.
        st.image("./images/sunflower2.jpg", caption="Sunflowers face the rising Sun")
        st.write("Image information will appear here.")


# running as option chooser.
if buffer is not None:
    if opt == "Show Image Information":
        run_img_info(img)
    
    elif opt == "Grey Image": # for grey options from sidebar
        run_grey_img(img)
    
    elif opt == "Resize Image": # for resize options from sidebar
        run_resize_img(img)
    
    elif opt == "Draw and Text":
        run_draw_text(img)

    elif opt == "Morphological Transformations": # for morphological transformation from sidebar
        run_morph_trans_img(img)
        
    elif opt == "Smoothing Images": # for smoothing options from sidebar
        run_smoothing_img(img)
    
    elif opt == "Color Detection(HSV)": # for color detecting option from sidebar
        # main selection from user.
        col1, col2 = st.columns(2)
        manl = col1.checkbox("Manually enter color range", value = True)
        drop = col2.checkbox("From drop color", value=False)
        hsv_run(img, manl=manl, drop=drop)
    
    elif opt == "Edge Detection": # for edge detecting from sidebar
        col1, col2 = st.columns(2)
        sobel = col1.checkbox("Sobel Edge `Detection`", value = False)
        canny = col2.checkbox("Canny Edge Detection", value = False)
        if sobel and canny:
            st.warning("Please Select one at a time.")
        elif not sobel and not canny:
            st.warning("Please select option from above.")
        elif sobel:    
            edgedetection_run(img, "Sobel")
        elif canny:
            edgedetection_run(img, "Canny")
    
    elif opt == "Histogram Equalization": # for histogram equalization option from sidebar
        run_hist_equ(img)

else:
    pass

