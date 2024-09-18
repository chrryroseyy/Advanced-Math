import streamlit as st
from streamlit_lottie import st_lottie
import be as BE
import requests

st.set_page_config(page_title="Binary-Decimal Converter", page_icon=":notebook:", layout="wide")

@st.cache_resource
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl("https://lottie.host/bcaabc19-4490-4d49-ab9f-77d5bb7c283f/uPG7Mc18n0.json")
with st.container():
    st.title("DECIMAL-BINARY CONVERTER🔢")
    conversion = st.radio("What do you want to convert?", ["Binary to Decimal Number", "Decimal to Binary Number"])

# Main container
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)

    # Binary to Decimal conversion
    with left_column:
        if conversion == "Binary to Decimal Number":
            st.title('Binary to Decimal Number⌨')
            binary_number = st.text_input("Enter binary number: ", key="binary_number")

            if not binary_number.strip() or set(binary_number) - {"0", "1"}:
                st.error("Please enter a valid binary number consisting of 0s and 1s.")
            else:
                convert_button = st.button("Convert")
                st.session_state["convert_button"] = convert_button
                if convert_button:
                    decimal_num = BE.binary_to_decimal_number(binary_number)
                    st.session_state["decimal_number"] = decimal_num
                    st.text_input("Binary number equivalent to Decimal", value=str(decimal_num))
                    print(st.session_state)

    # Decimal to Binary conversion
    with left_column:
        if conversion == "Decimal to Binary Number":
            st.header("DECIMAL TO BINARY CONVERTER⌨")
            decimal_number = st.text_input("Enter a decimal integer number: ", key="decimal_number")

            try:
                decimal_number = int(decimal_number)
                if decimal_number < 0:
                    st.error("Please enter a non-negative integer.")
            except ValueError:
                st.error("Please enter a valid integer number.")
            else:
                convert_button = st.button("Convert")
                st.session_state["convert_button"] = convert_button
                if convert_button:
                    binary_num = BE.decimal_to_binary_number(decimal_number)
                    st.session_state["binary_number"] = binary_num
                    st.text_input("Binary number equivalent to Decimal", value=str(binary_num))
                    print(st.session_state)

    # Right column for the Lottie animation
    with right_column:
        st_lottie(lottie_animation, height=700, key="animation")
