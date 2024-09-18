import streamlit as st
import numpy as np
from backend import backend2

#set page config and background image
st.set_page_config(page_title="System of Linear Equations", page_icon=":notebook:", layout="wide")

# Background image style
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://removal.ai/wp-content/uploads/2021/09/black-background-04-coolbackgrounds-768x374.png");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

def solve_backend2(L, U, B): #Function to solve the system of linear equations using LU Decomposition
    n = len(B)
    y = np.zeros(n)
    x = np.zeros(n)

    # Solve Ly = B
    for i in range(n):
        y[i] = B[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


def main():
    with st.container():
        st.markdown("""
            <h1 style="font-size: 40px; font-family: 'Arial, sans-serif'; text-align: center; color: white">
                System of Linear Equations Calculator🧮📶
                </h1>
            """, unsafe_allow_html=True)
        st.markdown("""
                    <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; font-style: italic; text-align: center; color: yellow">
                        Solve system of linear equations using LU Decomposition.
                        </h1>
                    """, unsafe_allow_html=True)

    with st.container():
        st.write("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
                <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center; color: white">
                Enter the number of equations:
                </h1>
            """, unsafe_allow_html=True)
    with col2:
        num_equations = st.number_input("",min_value=2, max_value=5)

    A = np.zeros((num_equations, num_equations))
    B = np.zeros(num_equations)
    with st.container():
        st.write("---")
    with st.container():
        st.markdown("""
                <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: left; color: yellow">
                Please enter the coefficients and the constant of each equation.
                </h1>
            """, unsafe_allow_html=True)

    equation_cols = st.columns(2 * num_equations)

    for i in range(num_equations):
        with equation_cols[2 * i]:
            for j in range(num_equations):
                coeff_title = f"<span style='color: white;'>Coefficient of equation {i + 1}.{j + 1}</span>"
                st.markdown(coeff_title, unsafe_allow_html=True)
                A[i, j] = st.number_input("", format="%f", key=f"A_{i}_{j}")

        with equation_cols[2 * i + 1]:
            const_title = f"<span style='color: white;'>Constant of equation {i + 1}</span>"
            st.markdown(const_title, unsafe_allow_html=True)
            B[i] = st.number_input("", format="%f", key=f"b_{i}")

    L = np.zeros_like(A)
    U = np.zeros_like(A)
    roots = []
    if st.button("Solve"):
        L, U = backend2(A)
        roots = solve_backend2(L, U, B)

        st.markdown("""
                            <h1 style="font-size: 25px; font-family: 'Arial, sans-serif'; text-align: center; color: yellow">
                            SOLUTIONS:
                            </h1>
                            """, unsafe_allow_html=True)
        with st.container():
            st.markdown("""
                <style>
                .centered {
                    margin: auto;
                }
                </style>
                """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
                                    <h1 style="font-size: 25px; font-family: 'Arial, sans-serif'; text-align: left; color: yellow">
                                    Lower Triangular Matrix (L):
                                    </h1>
                                    """, unsafe_allow_html=True)
        st.write(np.round(L, 3))
    with col2:
        st.markdown("""
                                            <h1 style="font-size: 25px; font-family: 'Arial, sans-serif'; text-align: left; color: yellow">
                                            Upper Triangular Matrix (U):
                                            </h1>
                                            """, unsafe_allow_html=True)
        st.write(np.round(U, 3))

    # Center-align the table displaying solution
    st.markdown(
        "<h1 style='text-align: center; font-size: 25px; font-family: \"Arial, sans-serif\"; color: yellow;'>Results:</h1>",
        unsafe_allow_html=True)
    for i, root in enumerate(roots):
        st.markdown(
            f"<p style='text-align: center; font-size: 20px; font-family: \"Arial, sans-serif\"; color: white;'>X<sub>{i + 1} </sub>: {root}</h3>",
            unsafe_allow_html=True)
    st.divider()

if __name__ == "__main__":
    main()

