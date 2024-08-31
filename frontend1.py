import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Function Definitions
def binary_to_decimal_number(binary_number):
    decimal_number = 0
    exp = 0
    binary_number = int(binary_number)
    while binary_number > 0:
        decimal = binary_number % 10
        decimal_number += decimal * pow(2, exp)
        binary_number //= 10
        exp += 1
    return decimal_number

def decimal_to_binary_number(decimal_number):
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number //= 2
    return binary_number or "0"

# Streamlit Page Configuration
st.set_page_config(page_title="Binary-Decimal Converter", page_icon=":notebook:", layout="wide")

# Load Lottie Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl("https://lottie.host/bcaabc19-4490-4d49-ab9f-77d5bb7c283f/uPG7Mc18n0.json")

# Main App Layout
with st.container():
    st.title("NUMBER CONVERTER🔢")
    conversion = st.radio("What do you want to convert?", ["Binary to Decimal Number", "Decimal to Binary Number"])

    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        if conversion == "Binary to Decimal Number":
            st.title('Binary to Decimal Number⌨')
            binary_number = st.text_input("Enter binary number: ", key="binary_number")

            if not binary_number.isdigit() or set(binary_number) - {"0", "1"}:
                st.error("Please enter a valid binary number.")
            else:
                convert_button = st.button("Convert")
                if convert_button:
                    decimal_num = binary_to_decimal_number(binary_number)
                    st.session_state["decimal_number"] = decimal_num
                    st.text_input("Binary number equivalent to Decimal", value=str(decimal_num), disabled=True)

        else:
            st.header("DECIMAL TO BINARY CONVERTER⌨")
            decimal_number = st.text_input("Enter a decimal integer number: ", key="decimal_number")

            if not decimal_number.isdigit():
                st.error("Please enter a valid integer number.")
            else:
                convert_button = st.button("Convert")
                if convert_button:
                    binary_num = decimal_to_binary_number(int(decimal_number))
                    st.session_state["binary_number"] = binary_num
                    st.text_input("Binary number equivalent to Decimal", value=str(binary_num), disabled=True)

    with right_column:
        st_lottie(lottie_animation, height=700, key="animation")
