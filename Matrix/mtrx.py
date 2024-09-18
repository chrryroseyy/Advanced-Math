import streamlit as st
import Adding_matrices as am
import Multiplying_matrices as ma
import transposing_matrices as tm
import Determinant as dm
import Inverse_of_matrices as im
import numpy as np

st.set_page_config(page_title="Matrix Calculator", page_icon=":notebook:", layout="wide")

# Background image style and font style
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://img.freepik.com/premium-photo/teal-color-pastel-turquoise-simple-minimalist-backgrounds-background-pretty-backdrop_715671-1154.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
body {
    font-family: 'Arial, sans-serif';
}
h1, h2, h3, h4, p {
    font-family: 'Arial, sans-serif';
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <h1 style="font-size: 40px; text-align: center; color: #FF6F61">
            Matrix Calculator 🖥️
        </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
        <h2 style="font-size: 20px; font-style: italic; text-align: center; color: black">
            "Matrix algebra is a powerful tool for solving linear systems and has applications in numerous fields." — Gilbert Strang
        </h2>
    """, unsafe_allow_html=True)

with st.container():
    st.write("---")

# Columns for matrix size input
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <h3 style="text-align: center; color: #F5F5DC">
            Enter the size of the matrices:
        </h3>
    """, unsafe_allow_html=True)
with col2:
    row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
with col3:
    column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

# Matrix A input
col4, col5 = st.columns(2)
with col4:
    st.markdown("""
        <h3 style="color: black">
            Matrix A
        </h3>
    """, unsafe_allow_html=True)
    matA = []
    for row_index in range(int(row)):
        columns = st.columns(int(column))
        row_values = []
        for col_index, col in enumerate(columns):
            with col:
                value = st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')
                row_values.append(value)
        matA.append(row_values)

with col5:
    st.markdown("""
        <h3 style="color: black">
            Matrix B
        </h3>
    """, unsafe_allow_html=True)
    matB = []
    for row_index in range(int(row)):
        columns = st.columns(int(column))
        row_values = []
        for col_index, col in enumerate(columns):
            with col:
                value = st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
                row_values.append(value)
        matB.append(row_values)

# Dropdown for matrix operations
operation = st.selectbox("Select an operation:", [
    "Add Matrices",
    "Multiply Matrices",
    "Transpose Matrices",
    "Inverse of Matrices",
    "Determinant of Matrices"
])

# Calculate based on the selected operation
if operation == "Add Matrices":
    try:
        matrix_Result = am.adding_matrices(matA, matB)
        col6, col7, col8 = st.columns(3)
        with col7:
            st.subheader("Sum of Matrix A and B🧮")
            for row_index in range(int(row)):
                columns = st.columns(int(column))
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index], key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
    except Exception as e:
        st.error(f"Error: {e}")

elif operation == "Multiply Matrices":
    try:
        matrix_Result = ma.multiplying_matrices(matA, matB)
        col6, col7, col8 = st.columns(3)
        with col7:
            st.subheader("Product of Matrix A and B🧮")
            for row_index in range(int(row)):
                columns = st.columns(int(column))
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index], key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
    except ValueError as e:
        st.error(f"Error: {e}")

elif operation == "Transpose Matrices":
    try:
        matrix_Result = tm.transpose_matrices(matA, matB)
        col8, col9 = st.columns(2)
        with col8:
            st.subheader("Transposed Matrix A🧮")
            for row_index in range(len(matrix_Result[0])):
                columns = st.columns(len(matrix_Result))
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[0][row_index][col_index], key=f'TArow{row_index + 1}Tcol{col_index + 1}')
        with col9:
            st.subheader("Transposed Matrix B🧮")
            for row_index in range(len(matrix_Result[1])):
                columns = st.columns(len(matrix_Result))
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[1][row_index][col_index], key=f'TBrow{row_index + 1}Tcol{col_index + 1}')
    except IndexError as e:
        st.error(f"Error: {e}")

elif operation == "Inverse of Matrices":
    try:
        inv_matA, inv_matB = im.inverse_matrices(matA, matB)
        if inv_matA is not None and inv_matB is not None:
            col6, col7 = st.columns(2)
            with col6:
                st.subheader("Inverse of Matrix A🧮")
                for row_index in range(len(inv_matA)):
                    for col_index in range(len(inv_matA[row_index])):
                        st.text_input("", value=str(inv_matA[row_index][col_index]), key=f'A_{row_index + 1}Acol{col_index + 1}')
            with col7:
                st.subheader("Inverse of Matrix B🧮")
                for row_index in range(len(inv_matB)):
                    for col_index in range(len(inv_matB[row_index])):
                        st.text_input("", value=str(inv_matB[row_index][col_index]), key=f'B_{row_index + 1}Bcol{col_index + 1}')
        else:
            st.error("Error: Singular matrix. Cannot invert the matrices.")
    except Exception as e:
        st.error(f"Error: {e}")

elif operation == "Determinant of Matrices":
    try:
        det_matA, det_matB = dm.Determinant_matrices(matA, matB)
        col6, col7 = st.columns(2)
        with col6:
            st.subheader("Determinant of Matrix A🧮")
            st.text_input("", value=str(det_matA))
        with col7:
            st.subheader("Determinant of Matrix B🧮")
            st.text_input("", value=str(det_matB))
    except np.linalg.LinAlgError as e:
        st.error(f"Error: {e}")
