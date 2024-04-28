import streamlit as st

st.write("Hello World!")

st.markdown("hello World223444433")

#st.video("https://www.youtube.com/watch?v=91s-D0qkeaE")


sex = st.text_input("sex", value="male")

st.write(f"input sex is {sex}")

option = st.selectbox(
'# How would you like to be contacted?',
('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

if st.button('Submit'):
    st.write("555555!")