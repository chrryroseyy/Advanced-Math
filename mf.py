import streamlit as st
import Adding_matrices as am
import Multiplying_matrices as ma
import transposing_matrices as tm
import Determinant as dm
import Inverse_of_matrices as im
import numpy as np
st.set_page_config(page_title="Matrix Calculator", page_icon=":notebook:", layout="wide")
st.markdown(
    """
    <style>
    .stApp{
        background-color : lightblue ;

    }
    </style>
    """,
    unsafe_allow_html=True)
with st.container():
    st.title("MATRIX CALCULATOR🖩💡")
with st.container():
    st.write("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center">
        Enter the size of the matrices:
        </h1>
    """, unsafe_allow_html=True)
with col2:
    row = st.number_input("ROW:", min_value=1, max_value=5, key='row')
with col3:
    column = st.number_input("COLUMN:", min_value=1, max_value=5, key='column')

col4, col5 = st.columns(2)
with col4:
    st.markdown("""
            <h1 style="font-size: 24px; font-family: 'Arial, sans-serif';">
            Matrix A
            </h1>
        """, unsafe_allow_html=True)
    matA = []
    for row_index in range(row):
        columns = st.columns(column)
        row_values = []
        for col_index, col in enumerate(columns):
            with col:
                value = st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')
                row_values.append(value)
        matA.append(row_values)

with col5:
    st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Arial, sans-serif';">
                Matrix B
                </h1>
            """, unsafe_allow_html=True)
    matB = []
    for row_index in range(row):
        columns = st.columns(column)
        row_values = []
        for col_index, col in enumerate(columns):
            with col:
                value = st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
                row_values.append(value)
        matB.append(row_values)

calculate = st.button("Add Matrices", key='add_button')
if calculate:
    matrix_Result = am.adding_matrices(matA, matB)
    col6, col7, col8 = st.columns(3)
    with col7:
        st.subheader("Sum of Matrix A and B🧮")
        for row_index in range(row):
            columns = st.columns(column)
            for col_index, col in enumerate(columns):
                with col:
                    st.text_input("", value=matrix_Result[row_index][col_index],
                                  key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
calculate = st.button("Multiply Matrices", key='multiply_button')
if calculate:
    try:
        matrix_Result = ma.multiplying_matrices(matA, matB)
        col6, col7, col8 = st.columns(3)
        with col7:
            st.subheader("Product of Matrix A and B🧮")
            for row_index in range(row):
                columns = st.columns(column)
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index],
                                    key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
    except ValueError as e:
        st.error(str(e))
calculate = st.button("Transpose Matrices", key='transpose_button')
if calculate:
    try:
        matrix_Result = tm.transpose_matrices(matA, matB)
        col8, col9, col10 = st.columns(3)
        with col9:
            st.subheader("Transposed Matrix of Matrix A and B🧮")
            for row_index in range(row):
                columns = st.columns(column)
                for col_index, col in enumerate(columns):
                    with col:
                        st.text_input("", value=matrix_Result[row_index][col_index],
                                    key=f'Rrow{row_index + 1}Rcol{col_index + 1}')
    except IndexError as e:
        st.error(str(e))
calculate = st.button("Inverse of Matrices", key='inverse_button')
if calculate:
    inv_matA, inv_matB = im.inverse_matrices(matA, matB)
    if inv_matA is not None and inv_matB is not None:
        col6, col7 = st.columns(2)
        with col6:
            st.subheader("Inverse of Matrix A🧮")
            for row_index in range(len(inv_matA)):
                for col_index in range(len(inv_matA[row_index])):
                    st.text_input("", value=str(inv_matA[row_index][col_index]),
                                  key=f'A_{row_index + 1}Acol{col_index + 1}')
        with col7:
            st.subheader("Inverse of Matrix B")
            for row_index in range(len(inv_matB)):
                for col_index in range(len(inv_matB[row_index])):
                    st.text_input("", value=str(inv_matB[row_index][col_index]),
                                  key=f'B_{row_index + 1}Bcol{col_index + 1}')
    else:
        st.error("Error: Singular matrix. Cannot invert the matrices.")

calculate = st.button("Determinant of Matrices", key='determinant_button')
if calculate:
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
        st.error(str(e))

