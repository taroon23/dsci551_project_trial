# app.py
import streamlit as st

# Title of the app
st.title("Streamlit Hello App")

# Display hello message
st.write("Hello!")

import streamlit as st
import pandas as pd
import os

# Path to the folder where the CSV files are stored
DATA_FOLDER = "Data"

# Pre-existing databases (CSV file paths)
DATABASES = {
    "Nutrition Data for Cereals": os.path.join(DATA_FOLDER, "cereal.csv"),
    "People Personality Traits and Factors": os.path.join(DATA_FOLDER, "personality.csv"),
    "Spotify Most Streamed Songs": os.path.join(DATA_FOLDER, "spotify.csv")
}

def load_csv_from_database(database_name):
    # Load CSV from the selected database
    if database_name in DATABASES:
        df = pd.read_csv(DATABASES[database_name])
        return df
    return None

def upload_and_display_csv():
    st.write("Or upload your own CSV file:")
    # File uploader allows users to upload CSV files
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the uploaded file into a pandas dataframe
        df = pd.read_csv(uploaded_file)

        # Display the dataframe on the webpage
        st.write("Here is your uploaded CSV file:")
        st.dataframe(df)
        return df
    else:
        st.write("Please upload a CSV file.")
        return None

# Streamlit App Title
st.title("CSV File Selector or Uploader")

# Step 1: Select from available databases
st.write("Select a database from the list or upload your own CSV:")
option = st.selectbox(
    "Choose from pre-existing databases",
    ["None"] + list(DATABASES.keys())  # Add 'None' for custom upload option
)

# Step 2: Load the selected database or allow CSV upload
if option != "None":
    # Load the selected database
    df = load_csv_from_database(option)
    st.write(f"Displaying data from {option}:")
    st.dataframe(df)
else:
    # Allow custom CSV upload
    df = upload_and_display_csv()
