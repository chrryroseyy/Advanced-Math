import streamlit as st
from streamlit_option_menu import option_menu


# Set up the sidebar for navigation
with st.sidebar:
    selected_page = option_menu(
        menu_title="Info",
        options=["About Me", "Projects", "Contact Info"],
        icons=["person", "briefcase", "telephone"],
        default_index=0
    )

# Function to show contact form
def show_contact_form():
    with st.form(key='contact_form'):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.success(f"Thank you for reaching out, {first_name}!")


# Display content based on the selected page
if selected_page == "About Me":
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

    with col1:
        image_path = "C:/Users/Acer/Downloads/1000000499.jpg"
        st.image(image_path, width=200)

    with col2:
        st.title("Cherry Rose Lubiano", anchor=False)
        st.write(
            "A driven and curious mechanical engineering student seeking immersive experience to enhance skills in the engineering industry.")
        if st.button("✉️ Contact Me"):
            show_contact_form()

    st.write("\n")
    st.subheader("Education", anchor=False)
    st.write(
        """ 
        - BS Mechanical Engineering at Visayas State University (Baybay).

            August 2021-Present
        """
    )

    st.write("\n")
    st.subheader("Relevant Coursework", anchor=False)
    st.write(
        """
        - [Output] Arduino Laboratory Exercises
          
                Basic training specializing in various Arduino circuit configurations and programming.
        - [Paper] DC and AC Motor Controls Manual [Lubiano, et al.]
          
                Configured and discussed conventional motor settings for single-phase and three-phase motors using a fabricated 24 DC Motor Control System and a commercial 240V AC Motor Control System.
        
        - [Output] DC Shunt Motor
          
                Fabrication of a direction-controllable DC Shunt Motor and discussion of its theory.
        - [Project] 5V Powered Miniature House
          
                Planning and construction of a miniature house using vinyl tiles with a 5V lighting circuit.
        """
    )

elif selected_page == "Projects":
    st.title("Advanced Mathematics Related Projects")
    st.write("\n")
    st.write(
        """
         🔢 Decimal-Binary Converter (http://localhost:8501/)
         
                A simple web app that converts base 10 or decimal integer number (positive and negative including zero) into base 2 or binary number and vice versa 
            
         💻 Matrix Calculator (https://advanced-math-7fgrjhnjamwfra9r3xbuny.streamlit.app/)
                
                A matrix calculator allows you to perform various operations on matrices, such as addition, multiplication, transpose, inversion, and determinant.
         
         🧮 System of Linear Equations Calculator (https://advanced-math-cs9nkw5vfvnxoay8gzrtso.streamlit.app/)
         
                A web app that will ask the user about the number of Linear Equations or Unknown variables. It find values for these variables that satisfy all the equations simultaneously.
        """
    )

elif selected_page == "Contact Info":
    st.title("Contact Information")
    st.write("Here is my contact information:")
    st.write(
        """
        ✉️ lubianocherryrose@gmail.com
        
        ⓕ (https://www.facebook.com/cherryrose.lubiano)
        
        ☎️ 09700571309
        
        🏠︎ Core Shelter Brgy. San Miguel, Palompon, Leyte
        """
    )
