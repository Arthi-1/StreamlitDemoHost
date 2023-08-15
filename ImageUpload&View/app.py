import streamlit as st

st.title("Hello Image Upload & Display App")

uploaded_file = st.file_uploader("Choose an image...", type={'png', 'jpg', 'jpeg'})

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

