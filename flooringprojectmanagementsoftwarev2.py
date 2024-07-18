import streamlit as st
import pandas as pd

# Initialize session state
if 'projects' not in st.session_state:
    st.session_state['projects'] = []
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []
if 'people' not in st.session_state:
    st.session_state['people'] = []
if 'clients' not in st.session_state:
    st.session_state['clients'] = []
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = []
if 'mileage' not in st.session_state:
    st.session_state['mileage'] = []

# Initialize all the session state inputs used in the app
if 'person_name_input' not in st.session_state:
    st.session_state.person_name_input = ''
if 'clear_person_input' not in st.session_state:
    st.session_state.clear_person_input = False

if 'client_name_input' not in st.session_state:
    st.session_state.client_name_input = ''
if 'client_address_input' not in st.session_state:
    st.session_state.client_address_input = ''
if 'client_email_input' not in st.session_state:
    st.session_state.client_email_input = ''
if 'client_phone_input' not in st.session_state:
    st.session_state.client_phone_input = ''
if 'clear_client_inputs' not in st.session_state:
    st.session_state.clear_client_inputs = False

if 'project_name_input' not in st.session_state:
    st.session_state.project_name_input = ''
if 'project_description_input' not in st.session_state:
    st.session_state.project_description_input = ''
if 'project_assigned_to_input' not in st.session_state:
    st.session_state.project_assigned_to_input = ''
if 'project_priority_input' not in st.session_state:
    st.session_state.project_priority_input = 'Low'
if 'project_estimate_hours_input' not in st.session_state:
    st.session_state.project_estimate_hours_input = 0.0
if 'project_client_name_input' not in st.session_state:
    st.session_state.project_client_name_input = ''
if 'clear_project_inputs' not in st.session_state:
    st.session_state.clear_project_inputs = False

if 'task_name_input' not in st.session_state:
    st.session_state.task_name_input = ''
if 'task_description_input' not in st.session_state:
    st.session_state.task_description_input = ''
if 'task_status_input' not in st.session_state:
    st.session_state.task_status_input = 'Not Started'
if 'task_assigned_to_input' not in st.session_state:
    st.session_state.task_assigned_to_input = ''
if 'task_priority_input' not in st.session_state:
    st.session_state.task_priority_input = 'Low'
if 'task_estimate_hours_input' not in st.session_state:
    st.session_state.task_estimate_hours_input = 0.0
if 'task_project_name_input' not in st.session_state:
    st.session_state.task_project_name_input = ''
if 'clear_task_inputs' not in st.session_state:
    st.session_state.clear_task_inputs = False

if 'expense_name_input' not in st.session_state:
    st.session_state.expense_name_input = ''
if 'expense_cost_input' not in st.session_state:
    st.session_state.expense_cost_input = 0.0
if 'expense_quantity_input' not in st.session_state:
    st.session_state.expense_quantity_input = 0
if 'expense_website_link_input' not in st.session_state:
    st.session_state.expense_website_link_input = ''
if 'clear_expense_inputs' not in st.session_state:
    st.session_state.clear_expense_inputs = False

if 'mileage_start_time_input' not in st.session_state:
    st.session_state.mileage_start_time_input = ''
if 'mileage_end_time_input' not in st.session_state:
    st.session_state.mileage_end_time_input = ''
if 'mileage_starting_mileage_input' not in st.session_state:
    st.session_state.mileage_starting_mileage_input = ''
if 'mileage_ending_mileage_input' not in st.session_state:
    st.session_state.mileage_ending_mileage_input = ''
if 'clear_mileage_inputs' not in st.session_state:
    st.session_state.clear_mileage_inputs = False


def add_project():
    client_name = st.session_state.project_client_name_input
    if client_name not in [client['client_name'] for client in st.session_state['clients']]:
        client_id = len(st.session_state['clients']) + 1
        st.session_state['clients'].append({
            'client_id': client_id,
            'client_name': client_name,
        })
    else:
        client_id = next(
            client['client_id'] for client in st.session_state['clients'] if client['client_name'] == client_name)

    st.session_state['projects'].append({
        'name': st.session_state.project_name_input,
        'description': st.session_state.project_description_input,
        'assigned_to': st.session_state.project_assigned_to_input,
        'priority': st.session_state.project_priority_input,
        'estimate_hours': st.session_state.project_estimate_hours_input,
        'client_id': client_id
    })
    st.success(f"Project '{st.session_state.project_name_input}' added successfully")
    st.session_state.clear_project_inputs = True


def add_task():
    st.session_state['tasks'].append({
        'project_name': st.session_state.task_project_name_input,
        'task_name': st.session_state.task_name_input,
        'task_description': st.session_state.task_description_input,
        'status': st.session_state.task_status_input,
        'assigned_to': st.session_state.task_assigned_to_input,
        'priority': st.session_state.task_priority_input,
        'estimate_hours': st.session_state.task_estimate_hours_input
    })
    st.success(f"Task '{st.session_state.task_name_input}' added successfully")
    st.session_state.clear_task_inputs = True


def add_person():
    st.session_state['people'].append(st.session_state.person_name_input)
    st.success(f"Person '{st.session_state.person_name_input}' added successfully")
    st.session_state.clear_person_input = True


def view_projects():
    if st.session_state['projects']:
        projects_df = pd.DataFrame(st.session_state['projects'])
        clients_df = pd.DataFrame(st.session_state['clients'])
        projects_df['client_id'] = projects_df['client_id'].astype(int)
        clients_df['client_id'] = clients_df['client_id'].astype(int)
        merged_df = pd.merge(projects_df, clients_df, left_on='client_id', right_on='client_id', how='left')
        st.write(merged_df.drop(columns=['client_id']))
    else:
        st.info("No projects added yet.")


def view_tasks():
    if st.session_state['tasks']:
        df = pd.DataFrame(st.session_state['tasks'])
        st.write(df)
    else:
        st.info("No tasks added yet.")


def add_expense():
    st.session_state['expenses'].append({
        'expense_name': st.session_state.expense_name_input,
        'cost': st.session_state.expense_cost_input,
        'quantity': st.session_state.expense_quantity_input,
        'total_cost': st.session_state.expense_cost_input * st.session_state.expense_quantity_input,
        'website_link': st.session_state.expense_website_link_input
    })
    st.success(f"Expense '{st.session_state.expense_name_input}' added successfully")
    st.session_state.clear_expense_inputs = True


def view_expenses():
    if st.session_state['expenses']:
        df = pd.DataFrame(st.session_state['expenses'])
        st.write(df)
    else:
        st.info("No expenses added yet.")


def add_mileage():
    start_time = st.session_state.mileage_start_time_input
    end_time = st.session_state.mileage_end_time_input
    starting_mileage = st.session_state.mileage_starting_mileage_input
    ending_mileage = st.session_state.mileage_ending_mileage_input

    st.session_state['mileage'].append({
        'start_time': start_time,
        'end_time': end_time,
        'starting_mileage': starting_mileage,
        'ending_mileage': ending_mileage
    })
    st.success("Mileage record added successfully")
    st.session_state.clear_mileage_inputs = True


def view_mileage():
    if st.session_state['mileage']:
        df = pd.DataFrame(st.session_state['mileage'])
        st.write(df)
    else:
        st.info("No mileage records added yet.")


def export_data():
    projects_df = pd.DataFrame(st.session_state['projects'])
    tasks_df = pd.DataFrame(st.session_state['tasks'])
    expenses_df = pd.DataFrame(st.session_state['expenses'])
    mileage_df = pd.DataFrame(st.session_state['mileage'])
    return (projects_df.to_csv(index=False), tasks_df.to_csv(index=False),
            expenses_df.to_csv(index=False), mileage_df.to_csv(index=False))


def add_client():
    client_id = len(st.session_state['clients']) + 1
    st.session_state['clients'].append({
        'client_id': client_id,
        'client_name': st.session_state.client_name_input,
        'client_address': st.session_state.client_address_input,
        'client_email': st.session_state.client_email_input,
        'client_phone': st.session_state.client_phone_input
    })
    st.success(f"Client '{st.session_state.client_name_input}' added successfully")
    st.session_state.clear_client_inputs = True


def view_clients():
    if st.session_state['clients']:
        df = pd.DataFrame(st.session_state['clients'])
        st.write(df)
    else:
        st.info("No clients added yet.")


def main():
    st.title("Project Management App")

    menu = ["Add Person", "View People", "Add Client", "View Clients",
            "Add Project", "View Projects", "Add Task", "View Tasks",
            "Add Expense", "View Expenses", "Add Mileage", "View Mileage", "Export Data"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Person":
        st.subheader("Add New Person")
        if st.session_state.get('clear_person_input', False):
            st.session_state.person_name_input = ''
            st.session_state.clear_person_input = False

        st.session_state.person_name_input = st.text_input("Person Name")
        if st.button("Add Person"):
            add_person()

    elif choice == "View People":
        st.subheader("View People")
        if st.session_state['people']:
            st.write(st.session_state['people'])
        else:
            st.info("No people added yet.")

    elif choice == "Add Client":
        st.subheader("Add New Client")
        if st.session_state.get('clear_client_inputs', False):
            st.session_state.client_name_input = ''
            st.session_state.client_address_input = ''
            st.session_state.client_email_input = ''
            st.session_state.client_phone_input = ''
            st.session_state.clear_client_inputs = False

        st.session_state.client_name_input = st.text_input("Client Name")
        st.session_state.client_address_input = st.text_area("Client Address")
        st.session_state.client_email_input = st.text_input("Client Email")
        st.session_state.client_phone_input = st.text_input("Client Phone")
        if st.button("Add Client"):
            add_client()

    elif choice == "View Clients":
        st.subheader("View Clients")
        view_clients()

    elif choice == "Add Project":
        st.subheader("Add New Project")
        if st.session_state.get('clear_project_inputs', False):
            st.session_state.project_name_input = ''
            st.session_state.project_description_input = ''
            st.session_state.project_assigned_to_input = ''
            st.session_state.project_priority_input = 'Low'
            st.session_state.project_estimate_hours_input = 0.0
            st.session_state.project_client_name_input = ''
            st.session_state.clear_project_inputs = False

        st.session_state.project_name_input = st.text_input("Project Name")
        st.session_state.project_description_input = st.text_area("Project Description")
        st.session_state.project_assigned_to_input = st.text_input("Assigned To")
        st.session_state.project_priority_input = st.selectbox("Priority", ["Low", "Medium", "High"])
        st.session_state.project_estimate_hours_input = st.number_input("Estimated Hours", min_value=0.0, step=0.1)
        st.session_state.project_client_name_input = st.selectbox("Client Name",
                                                                  options=[client['client_name'] for client in
                                                                           st.session_state['clients']])
        if st.button("Add Project"):
            add_project()

    elif choice == "View Projects":
        st.subheader("View Projects")
        view_projects()

    elif choice == "Add Task":
        st.subheader("Add New Task")
        if st.session_state.get('clear_task_inputs', False):
            st.session_state.task_name_input = ''
            st.session_state.task_description_input = ''
            st.session_state.task_status_input = 'Not Started'
            st.session_state.task_assigned_to_input = ''
            st.session_state.task_priority_input = 'Low'
            st.session_state.task_estimate_hours_input = 0.0
            st.session_state.task_project_name_input = ''
            st.session_state.clear_task_inputs = False

        st.session_state.task_name_input = st.text_input("Task Name")
        st.session_state.task_description_input = st.text_area("Task Description")
        st.session_state.task_status_input = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
        st.session_state.task_assigned_to_input = st.text_input("Assigned To")
        st.session_state.task_priority_input = st.selectbox("Priority", ["Low", "Medium", "High"])
        st.session_state.task_estimate_hours_input = st.number_input("Estimated Hours", min_value=0.0, step=0.1)
        st.session_state.task_project_name_input = st.selectbox("Project Name",
                                                                options=[project['name'] for project in
                                                                         st.session_state['projects']])
        if st.button("Add Task"):
            add_task()

    elif choice == "View Tasks":
        st.subheader("View Tasks")
        view_tasks()

    elif choice == "Add Expense":
        st.subheader("Add New Expense")
        if st.session_state.get('clear_expense_inputs', False):
            st.session_state.expense_name_input = ''
            st.session_state.expense_cost_input = 0.0
            st.session_state.expense_quantity_input = 0
            st.session_state.expense_website_link_input = ''
            st.session_state.clear_expense_inputs = False

        st.session_state.expense_name_input = st.text_input("Expense Name")
        st.session_state.expense_cost_input = st.number_input("Cost per Unit", min_value=0.0, step=0.01)
        st.session_state.expense_quantity_input = st.number_input("Quantity", min_value=0, step=1)
        st.session_state.expense_website_link_input = st.text_input("Website Link (Optional)")
        if st.button("Add Expense"):
            add_expense()

    elif choice == "View Expenses":
        st.subheader("View Expenses")
        view_expenses()

    elif choice == "Add Mileage":
        st.subheader("Add New Mileage")
        if st.session_state.get('clear_mileage_inputs', False):
            st.session_state.mileage_start_time_input = ''
            st.session_state.mileage_end_time_input = ''
            st.session_state.mileage_starting_mileage_input = ''
            st.session_state.mileage_ending_mileage_input = ''
            st.session_state.clear_mileage_inputs = False

        st.session_state.mileage_start_time_input = st.text_input("Start Time (in hours since midnight)")
        st.session_state.mileage_end_time_input = st.text_input("End Time (in hours since midnight)")
        st.session_state.mileage_starting_mileage_input = st.text_input("Starting Mileage")
        st.session_state.mileage_ending_mileage_input = st.text_input("Ending Mileage")
        if st.button("Add Mileage"):
            add_mileage()

    elif choice == "View Mileage":
        st.subheader("View Mileage")
        view_mileage()

    elif choice == "Export Data":
        st.subheader("Export Data")
        if st.button("Export"):
            with st.spinner('Exporting data...'):
                projects_csv, tasks_csv, expenses_csv, mileage_csv = export_data()
            st.success("Data exported successfully!")

    # Remaining code omitted for brevity...

if __name__ == '__main__':
    main()
