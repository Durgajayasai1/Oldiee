import streamlit as st
from PIL import Image
import numpy as np
import io

try:
    from zeroscratches import EraseScratches
except ImportError as e:
    st.error("Could not import `zeroscratches`. Make sure it's installed or included properly.")
    st.stop()

st.title("Oldiee 😎")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="🖼️ Original Image", use_container_width=True)

        eraser = EraseScratches()

        with st.spinner("🧼 Removing scratches..."):
            result = eraser.erase(image)

            if isinstance(result, np.ndarray) and result.ndim == 3 and result.shape[2] == 3:
                result_img = Image.fromarray(result)
            else:
                st.error("❌ Invalid format from `erase()` method. Expected RGB numpy array.")
                st.stop()

        st.image(result_img, caption="✨ Restored Image", use_container_width=True)

        img_buffer = io.BytesIO()
        result_img.save(img_buffer, format="PNG")
        img_buffer.seek(0)

        st.download_button(
            label="Download 📷",
            data=img_buffer,
            file_name="restored_image.png",
            mime="image/png"
        )

    except Exception as e:
        st.error(f"🚨 An error occurred:\n\n`{e}`")
