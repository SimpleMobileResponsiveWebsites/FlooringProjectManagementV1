import streamlit as st
import pandas as pd
from io import StringIO

# Function to load CSV files
def load_csv(uploaded_file):
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            return data
        except Exception as e:
            st.error(f"Error: {e}")
    return None

# Function to display project overview
def display_project_overview(projects_data):
    st.header("Projects Overview")
    for index, row in projects_data.iterrows():
        st.subheader(f"Project Name: {row['name']}")
        st.write(f"Description: {row['description']}")
        st.write(f"Assigned To: {row['assigned_to']}")
        st.write(f"Priority: {row['priority']}")
        st.write(f"Estimate Hours: {row['estimate_hours']}")
        st.write(f"Client ID: {row['client_id']}")

# Function to display tasks
def display_tasks(tasks_data):
    st.header("Tasks")
    for index, row in tasks_data.iterrows():
        st.subheader(f"Task Name: {row['task_name']}")
        st.write(f"Description: {row['task_description']}")
        st.write(f"Status: {row['status']}")
        st.write(f"Assigned To: {row['assigned_to']}")
        st.write(f"Priority: {row['priority']}")
        st.write(f"Estimate Hours: {row['estimate_hours']}")

# Function to display expenses
def display_expenses(expenses_data):
    st.header("Expenses")
    for index, row in expenses_data.iterrows():
        st.subheader(f"Expense Name: {row['expense_name']}")
        st.write(f"Cost: {row['cost']}")
        st.write(f"Quantity: {row['quantity']}")
        st.write(f"Total Cost: {row['total_cost']}")
        st.write(f"Link: {row['website_link']}")

# Function to display mileage
def display_mileage(mileage_data):
    st.header("Mileage")
    for index, row in mileage_data.iterrows():
        st.write(f"Start Time: {row['start_time']}")
        st.write(f"End Time: {row['end_time']}")
        st.write(f"Starting Mileage: {row['starting_mileage']}")
        st.write(f"Ending Mileage: {row['ending_mileage']}")
        st.write(f"Total Mileage: {row['ending_mileage'] - row['starting_mileage']}")

# Streamlit app
st.title("Flooring Project Dashboard")

# Upload CSV files
st.header("Upload CSV Files")

uploaded_projects = st.file_uploader("Upload Projects CSV", type=["csv"])
uploaded_tasks = st.file_uploader("Upload Tasks CSV", type=["csv"])
uploaded_expenses = st.file_uploader("Upload Expenses CSV", type=["csv"])
uploaded_mileage = st.file_uploader("Upload Mileage CSV", type=["csv"])

# Load and display the data
projects_data = load_csv(uploaded_projects)
tasks_data = load_csv(uploaded_tasks)
expenses_data = load_csv(uploaded_expenses)
mileage_data = load_csv(uploaded_mileage)

if projects_data is not None:
    display_project_overview(projects_data)

if tasks_data is not None:
    display_tasks(tasks_data)

if expenses_data is not None:
    display_expenses(expenses_data)

if mileage_data is not None:
    display_mileage(mileage_data)

# Function to add header and combine data
def combine_data_with_headers(projects, tasks, expenses, mileage):
    csv_data = StringIO()

    if projects is not None:
        csv_data.write("Projects\n")
        projects.to_csv(csv_data, index=False)
        csv_data.write("\n")

    if tasks is not None:
        csv_data.write("Tasks\n")
        tasks.to_csv(csv_data, index=False)
        csv_data.write("\n")

    if expenses is not None:
        csv_data.write("Expenses\n")
        expenses.to_csv(csv_data, index=False)
        csv_data.write("\n")

    if mileage is not None:
        csv_data.write("Mileage\n")
        mileage.to_csv(csv_data, index=False)
        csv_data.write("\n")

    return csv_data.getvalue()

combined_csv = combine_data_with_headers(projects_data, tasks_data, expenses_data, mileage_data)

if combined_csv:
    st.header("Download Combined Data")
    st.download_button(label="Download CSV",
                       data=combined_csv,
                       file_name='combined_dashboard_data.csv',
                       mime='text/csv')
