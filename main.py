import streamlit as st

st.title("Test")

st.write("More stuff added")

upload_file = st.file_uploader("Choose file", type="txt")
if upload_file is not None:
    content_file = upload_file.read()
    decoded_file = content_file.decode('utf-8')
    st.write(decoded_file)