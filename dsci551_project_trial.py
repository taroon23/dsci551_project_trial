import streamlit as st
import pandas as pd
import mysql.connector
import os

# Path to the folder where the CSV files are stored
DATA_FOLDER = "Data"

# Pre-existing databases (CSV file paths)
DATABASES = {
    "Nutrition Data for Cereals": os.path.join(DATA_FOLDER, "cereal.csv"),
    "People Personality Traits and Factors": os.path.join(DATA_FOLDER, "personality.csv"),
    "Spotify Most Streamed Songs": os.path.join(DATA_FOLDER, "spotify.csv")
}

# Function to connect to MySQL
def connect_to_mysql():
    try:
        # Connect to MySQL localhost using root credentials
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",  # If there's a password, add it here
            database="dsci551_project_trial"  # Specify a default database, if any
        )
        if connection.is_connected():
            st.success("Connected to MySQL database successfully!")
            return connection
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Function to load CSV from the selected database
def load_csv_from_database(database_name):
    if database_name in DATABASES:
        df = pd.read_csv(DATABASES[database_name])
        return df
    return None

# Function for uploading and displaying CSV files
def upload_and_display_csv():
    st.write("Or upload your own CSV file:")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Here is your uploaded CSV file:")
        st.dataframe(df)
        return df
    else:
        st.write("Please upload a CSV file.")
        return None

# Main logic for page navigation
def main():
    # Initialize session state if not already set
    if "db_type" not in st.session_state:
        st.session_state["db_type"] = None

    # Step 1: Database Type Selection
    if st.session_state["db_type"] is None:
        st.title("Choose SQL or NoSQL")
        choice = st.radio("Which type of database would you like to use?", ("SQL", "NoSQL"))

        # Continue button to move to the next page
        if st.button("Continue"):
            st.session_state["db_type"] = choice  # Set the chosen type

    # Step 2: Database Interaction based on the choice
    if st.session_state["db_type"] == "SQL":
        # Try connecting to MySQL
        st.title("SQL Database")
        connection = connect_to_mysql()
        if connection:
            st.write("You are connected to the MySQL database.")
            # Optionally: Add further MySQL operations here
    elif st.session_state["db_type"] == "NoSQL":
        st.title("NoSQL Database (CSV)")
        # Step 1: Select from available databases
        st.write("Select a database from the list or upload your own CSV:")
        option = st.selectbox(
            "Choose from pre-existing databases",
            ["None"] + list(DATABASES.keys())
        )

        # Step 2: Load the selected database or allow CSV upload
        if option != "None":
            df = load_csv_from_database(option)
            st.write(f"Displaying data from {option}:")
            st.dataframe(df)
        else:
            df = upload_and_display_csv()

# Run the main function
if __name__ == "__main__":
    main()
