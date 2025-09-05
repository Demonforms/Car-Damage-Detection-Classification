# Created by Devesh Singh (Demonforms)
import streamlit as st
from utility import predict

st.markdown("<h1 style='white-space: nowrap;'>Car Damage Detection Classification</h1>",
            unsafe_allow_html=True)
st.markdown(
            f"<p style='text-align: center; font-size:14px; color:lightgray;'>"
            f"Project by <b>Devesh Singh</b>"
            f"</p>",
            unsafe_allow_html=True
        )

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp"])

if uploaded_file:
    image_path = "temp_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded File", use_container_width=True)
        prediction = predict(image_path)
        st.info(f"Predicted Class: {prediction}")
