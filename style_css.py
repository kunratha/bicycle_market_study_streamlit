import streamlit as st
import plotly.express as px


# Inject the default CSS for setting the background image, navbar, and a transparent overlay
def inject_background_css(bg_option):
    if bg_option == "Background Image":
        background_css = """
        <style>
        /* Main container background with opacity overlay */
        [data-testid="stAppViewContainer"] {
            background-image: url("https://cdn.pixabay.com/photo/2020/09/09/13/03/bike-riding-5557589_960_720.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: scroll;
            position: fixed;
            z-index: 1;
        }

        /* Add a semi-transparent overlay on top of the background image */
        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.85); /* Adjust the opacity with this rgba value */
            z-index: 0;
        }

        /* Ensure main content is positioned above the overlay */
        [data-testid="stAppViewContainer"] > div {
            position: relative;
            z-index: 1;
        }

        /* Sidebar background with opacity overlay */
        [data-testid="stSidebar"] {
            background-image: url("https://i.imgur.com/jUAQYJz.jpeg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: scroll;
            position: relative;
            z-index: 1;
        }

        /* Add a semi-transparent overlay to the sidebar */
        [data-testid="stSidebar"]::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.85); /* Adjust the opacity here too */
            z-index: 0;
        }

        /* Sidebar text and dropdown styling */
        [data-testid="stSidebar"] * {
            color: blue;  /* Change text color */
        }

        /* Customize the dropdown background */
        select {
            background-color: rgba(34, 34, 34, 0.85);
            color: white; /* White text for dropdown */
        }

        /* Customize the file uploader button text and background color */
        [data-testid="stFileUploadDropzone"] {
            background-color: rgba(34, 34, 34, 0.85); /* Dark background */
            color: white; /* White text inside file upload button */
        }

        /* Customize the dropdown arrow icon */
        .css-1msv8fj {
            color: white; /* Ensure dropdown icon color is white */
        }

        /* Navbar background and text */
        header[data-testid="stHeader"] {
            background-color: rgba(0, 0, 0, 0.7); /* Dark background for navbar */
            color: white; /* White text for navbar */
        }

        /* Ensure navbar elements are visible */
        header[data-testid="stHeader"] * {
            color: white;
        }
        </style>
        """
        st.session_state["text_color"] = "white"
        st.session_state["kpi_bg_color"] = "rgba(255, 99, 71, 0.2)"
        st.session_state["chart_colors"] = px.colors.qualitative.Pastel

    elif bg_option == "Dark Color":
        background_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: rgba(34, 34, 34, 0.85);  /* Dark color with opacity */
        }

        /* Sidebar dark background */
        [data-testid="stSidebar"] {
            background-color: rgba(34, 34, 34, 0.85);
            color: white;
        }

        /* Sidebar text and dropdown styling */
        [data-testid="stSidebar"] * {
            color: blue;  /* Change text color */
        }

        select {
            background-color: rgba(34, 34, 34, 0.85);
            color: white;
        }

        option {
            background-color: rgba(34, 34, 34, 0.85);
            color: white;
        }

        /* Customize the file uploader button text and background color */
        [data-testid="stFileUploadDropzone"] {
            background-color: rgba(34, 34, 34, 0.85); /* Dark background */
            color: white; /* White text inside file upload button */
        }

        /* Customize the dropdown arrow icon */
        .css-1msv8fj {
            color: white; /* Ensure dropdown icon color is white */
        }

        /* Navbar background and text */
        header[data-testid="stHeader"] {
            background-color: rgba(34, 34, 34, 0.7); /* Dark background for navbar */
            color: white; /* White text for navbar */
        }

        /* Ensure navbar elements are visible */
        header[data-testid="stHeader"] * {
            color: white;
        }
        </style>
        """
        st.session_state["text_color"] = "white"
        st.session_state["kpi_bg_color"] = "rgba(34, 34, 34, 0.6)"
        st.session_state["chart_colors"] = px.colors.qualitative.Bold

    elif bg_option == "Light Color":
        background_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: rgba(240, 240, 240, 0.9);  /* Light color with opacity */
        }

        /* Sidebar light background */
        [data-testid="stSidebar"] {
            background-color: rgba(240, 240, 240, 0.9);
            color: black;
        }

        /* Sidebar text and dropdown styling */
        [data-testid="stSidebar"] * {
            color: black;  /* Change text color */
        }

        select {
            background-color: rgba(240, 240, 240, 0.9);
            color: black;
        }

        option {
            background-color: rgba(240, 240, 240, 0.9);
            color: black;
        }

        /* Customize the file uploader button text and background color */
        [data-testid="stFileUploadDropzone"] {
            background-color: rgba(240, 240, 240, 0.9); /* Light background */
            color: black; /* Black text inside file upload button */
        }

        /* Customize the dropdown arrow icon */
        .css-1msv8fj {
            color: black; /* Ensure dropdown icon color is black */
        }

        /* Navbar background and text */
        header[data-testid="stHeader"] {
            background-color: rgba(240, 240, 240, 0.9); /* Light background for navbar */
            color: black; /* Black text for navbar */
        }

        /* Ensure navbar elements are visible */
        header[data-testid="stHeader"] * {
            color: black;
        }
        </style>
        """
        st.session_state["text_color"] = "black"
        st.session_state["kpi_bg_color"] = "rgba(240, 240, 240, 0.8)"
        st.session_state["chart_colors"] = px.colors.qualitative.Set3

    elif bg_option == "Daltonien":
        background_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: rgba(255, 228, 196, 0.7);  /* Daltonien-friendly mode */
        }

        /* Sidebar Daltonien-friendly background */
        [data-testid="stSidebar"] {
            background-color: rgba(255, 228, 196, 0.7);
            color: black;
        }

        /* Sidebar text and dropdown styling */
        [data-testid="stSidebar"] * {
            color: black;  /* Change text color */
        }

        select {
            background-color: rgba(255, 228, 196, 0.7);
            color: black;
        }

        option {
            background-color: rgba(255, 228, 196, 0.7);
            color: black;
        }

        /* Customize the file uploader button text and background color */
        [data-testid="stFileUploadDropzone"] {
            background-color: rgba(255, 228, 196, 0.7); /* Daltonien background */
            color: black; /* Black text inside file upload button */
        }

        /* Customize the dropdown arrow icon */
        .css-1msv8fj {
            color: black; /* Ensure dropdown icon color is black */
        }

        /* Navbar background and text */
        header[data-testid="stHeader"] {
            background-color: rgba(255, 228, 196, 0.7); /* Daltonien background for navbar */
            color: black; /* Black text for navbar */
        }

        /* Ensure navbar elements are visible */
        header[data-testid="stHeader"] * {
            color: black;
        }
        </style>
        """
        st.session_state["text_color"] = "black"
        st.session_state["kpi_bg_color"] = "rgba(200, 200, 200, 0.8)"
        st.session_state["chart_colors"] = px.colors.qualitative.Safe

    else:
        # Default background
        background_css = """
        <style>
        [data-testid="stAppViewContainer"] {
            background-image: url("https://cdn.pixabay.com/photo/2020/09/09/13/03/bike-riding-5557589_960_720.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: scroll;
        }

        /* Navbar default background */
        header[data-testid="stHeader"] {
            background-color: rgba(0, 123, 255, 0.7); /* Default background for navbar */
            color: white; /* Default text for navbar */
        }

        /* Ensure navbar elements are visible */
        header[data-testid="stHeader"] * {
            color: white;
        }
        </style>
        """

    # Inject the selected background CSS
    st.markdown(background_css, unsafe_allow_html=True)


# Call the function for testing
inject_background_css("Background Image")  # Change this to test other themes
