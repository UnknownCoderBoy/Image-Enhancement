import cv2
import numpy as np
import streamlit as st

st.set_page_config(page_title="Image Enhancement")

st.title("Image Enhancement Techniques")

selectbox = st.sidebar.selectbox(
    "Which operation do you want to perform?",
    ("Adjusted Brightness & Contrast", "Image Blurring", "Image Sharpening", "Invert Image Color")
)

if selectbox == "Adjusted Brightness & Contrast":
	st.subheader(selectbox)
	image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"], key="bc")

	if image_file is not None:

		image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

		col1, col2 = st.columns(2)
		with col1:
			brightness = st.slider("Select a brightness", min_value=0, max_value=180, value=0, step=5)
			st.image(image, channels="BGR", caption="Original Image")

		with col2:
			contrast = st.slider("Select a contrast", min_value=1, max_value=5, value=1, step=1)
			adjusted_image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
			st.image(adjusted_image, channels="BGR", caption="Result Image")


if selectbox == "Image Blurring":
	st.subheader(selectbox)
	option = st.radio(
			"Select Image",
			["Balloons", "Taj Mahal"],)

	if option == "Balloons":
			image = cv2.imread("Balloons.png")
	if option == "Taj Mahal":
			image = cv2.imread("Taj-Mahal.jpg")

	blur_amount = st.slider("Select Blur Amount", min_value=1, max_value=15, value=5, step=2)
	filtered_image = cv2.medianBlur(image, blur_amount)
	filtered_image2 = cv2.GaussianBlur(image, (blur_amount, blur_amount), 0)
	filtered_image3 = cv2.boxFilter(image, -1, (blur_amount, blur_amount))
	filtered_image4 = cv2.bilateralFilter(image, blur_amount, 75, 75)
	col1, col2 = st.columns(2)
	with col1:
		st.image(filtered_image, channels="BGR", caption="Median Blur")
		st.image(filtered_image3, channels="BGR", caption="BoxFilter Blur")

	with col2:
		st.image(filtered_image2, channels="BGR", caption="Gaussian Blur")
		st.image(filtered_image4, channels="BGR", caption="Bilateral Filter Blur")


if selectbox == "Image Sharpening":
	st.subheader(selectbox)
	image_sharp = st.file_uploader("Upload Images", type=["png","jpg","jpeg"], key="sharp")

	if image_sharp is not None:

		image = cv2.imdecode(np.fromstring(image_sharp.read(), np.uint8), cv2.IMREAD_COLOR)

		kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
		sharpened_image = cv2.filter2D(image, -1, kernel)

		col1, col2 = st.columns(2)
		with col1:
			st.image(image, channels="BGR", caption="Original Image")

		with col2:
			st.image(sharpened_image, channels="BGR", caption="Result Image")

if selectbox == "Invert Image Color":
	st.subheader(selectbox)
	image_inv = st.file_uploader("Upload Images", type=["png","jpg","jpeg"], key="inv")

	if image_inv is not None:

		image = cv2.imdecode(np.fromstring(image_inv.read(), np.uint8), cv2.IMREAD_COLOR)

		inverse_image = 255 - image

		col1, col2 = st.columns(2)
		with col1:
			st.image(image, channels="BGR", caption="Original Image")

		with col2:
			st.image(inverse_image, channels="BGR", caption="Result Image")
