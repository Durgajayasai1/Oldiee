import streamlit as st
from PIL import Image
from zeroscratches import EraseScratches
import numpy as np
import io

st.title("Oldiee 😎")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Original Image", use_container_width=True)
    eraser = EraseScratches()

    with st.spinner("Removing scratches..."):
        result = eraser.erase(image)
        result_img = Image.fromarray(result)

    st.image(result_img, caption="Restored Image", use_container_width=True)

    img_buffer = io.BytesIO()
    result_img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    st.download_button(
        label="Download 📷",
        data=img_buffer,
        file_name="restored_image.png",
        mime="image/png"
    )