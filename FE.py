import streamlit as st
from streamlit_lottie import st_lottie
import requests
import be as BE

# Set up the page
st.set_page_config(page_title="Binary-Decimal Converter", page_icon=":notebook:", layout="wide")


# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_animation = load_lottieurl("https://lottie.host/bcaabc19-4490-4d49-ab9f-77d5bb7c283f/uPG7Mc18n0.json")

# Main container
with st.container():
    st.title("DECIMAL-BINARY CONVERTER🔢")
    conversion = st.radio("What do you want to convert?", ["Binary to Decimal Number", "Decimal to Binary Number"])

    # Create two columns for layout
    left_column, right_column = st.columns(2)

    with left_column:
        if conversion == "Binary to Decimal Number":
            st.header('Binary to Decimal Number⌨')
            binary_number = st.text_input("Enter binary number: ", key="binary_number")

            # Validate input
            if binary_number:
                if not binary_number.isdigit() or set(binary_number) - {"0", "1"}:
                    st.error("Please enter a valid binary number (only 0s and 1s).")
                else:
                    if st.button("Convert"):
                        decimal_num = BE.binary_to_decimal_number(binary_number)
                        st.text_input("Decimal number equivalent", value=str(decimal_num), key="decimal_output")

        else:
            st.header("Decimal to Binary Converter⌨")
            decimal_number = st.text_input("Enter decimal number: ", key="decimal_number")

            # Validate input
            if decimal_number:
                if not decimal_number.isdigit():
                    st.error("Please enter a valid decimal integer.")
                else:
                    if st.button("Convert"):
                        binary_num = BE.decimal_to_binary_number(int(decimal_number))
                        st.text_input("Binary number equivalent", value=str(binary_num), key="binary_output")

    with right_column:
        st_lottie(lottie_animation, height=700, key="animation")
