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

def add_project():
    client_name = st.session_state.project_client_name_input
    if client_name not in [client['client_name'] for client in st.session_state['clients']]:
        client_id = len(st.session_state['clients']) + 1
        st.session_state['clients'].append({
            'client_id': client_id,
            'client_name': client_name,
        })
    else:
        client_id = next(client['client_id'] for client in st.session_state['clients'] if client['client_name'] == client_name)

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
    st.write(st.session_state['projects'])

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
    st.write(st.session_state['tasks'])

def add_person():
    st.session_state['people'].append(st.session_state.person_name_input)
    st.success(f"Person '{st.session_state.person_name_input}' added successfully")
    st.session_state.clear_person_input = True
    st.write(st.session_state['people'])

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
    st.write(st.session_state['clients'])

def add_expense():
    st.session_state['expenses'].append({
        'expense_name': st.session_state.expense_name_input,
        'cost': st.session_state.expense_cost_input,
        'quantity': st.session_state.expense_quantity_input,
        'total_cost': st.session_state.expense_cost_input * st.session_state.expense_quantity_input
    })
    st.success(f"Expense '{st.session_state.expense_name_input}' added successfully")
    st.session_state.clear_expense_inputs = True
    st.write(st.session_state['expenses'])

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

def view_expenses():
    if st.session_state['expenses']:
        df = pd.DataFrame(st.session_state['expenses'])
        st.write(df)
    else:
        st.info("No expenses added yet.")

def export_data():
    projects_df = pd.DataFrame(st.session_state['projects'])
    tasks_df = pd.DataFrame(st.session_state['tasks'])
    expenses_df = pd.DataFrame(st.session_state['expenses'])
    return projects_df.to_csv(index=False), tasks_df.to_csv(index=False), expenses_df.to_csv(index=False)

def main():
    st.title("Project Management App v1.02")

    with st.expander("Add New Person"):
        if st.session_state.get('clear_person_input', False):
            st.session_state.person_name_input = ''
            st.session_state.clear_person_input = False

        with st.form(key='add_person_form'):
            st.text_input("Person Name", key='person_name_input')
            st.form_submit_button(label='Add Person', on_click=add_person)

    with st.expander("Add New Client"):
        if st.session_state.get('clear_client_inputs', False):
            st.session_state.client_name_input = ''
            st.session_state.client_address_input = ''
            st.session_state.client_email_input = ''
            st.session_state.client_phone_input = ''
            st.session_state.clear_client_inputs = False

        with st.form(key='add_client_form'):
            st.text_input("Client Name", key='client_name_input')
            st.text_input("Client Address", key='client_address_input')
            st.text_input("Client Email", key='client_email_input')
            st.text_input("Client Phone", key='client_phone_input')
            st.form_submit_button(label='Add Client', on_click=add_client)

    with st.expander("Add New Project"):
        if st.session_state.get('clear_project_inputs', False):
            st.session_state.project_name_input = ''
            st.session_state.project_description_input = ''
            st.session_state.project_assigned_to_input = ''
            st.session_state.project_priority_input = 'Low'
            st.session_state.project_estimate_hours_input = 0.0
            st.session_state.project_client_name_input = ''
            st.session_state.clear_project_inputs = False

        with st.form(key='add_project_form'):
            st.text_input("Project Name", key='project_name_input')
            st.text_area("Project Description", key='project_description_input')
            st.selectbox("Assigned To", [''] + st.session_state['people'], key='project_assigned_to_input')
            st.selectbox("Priority", ['Low', 'Medium', 'High'], key='project_priority_input')
            st.number_input("Estimated Hours", min_value=0.0, step=0.5, key='project_estimate_hours_input')
            st.selectbox("Client", [''] + [client['client_name'] for client in st.session_state['clients']],
                         key='project_client_name_input')
            st.form_submit_button(label='Add Project', on_click=add_project)

    with st.expander("View Projects"):
        view_projects()

    with st.expander("Add New Task"):
        if not st.session_state['projects']:
            st.warning("Please add a project first.")
        else:
            if st.session_state.get('clear_task_inputs', False):
                st.session_state.task_name_input = ''
                st.session_state.task_description_input = ''
                st.session_state.task_status_input = 'Not Started'
                st.session_state.task_assigned_to_input = ''
                st.session_state.task_priority_input = 'Low'
                st.session_state.task_estimate_hours_input = 0.0
                st.session_state.clear_task_inputs = False

            with st.form(key='add_task_form'):
                st.selectbox("Select Project", [proj['name'] for proj in st.session_state['projects']],
                             key='task_project_name_input')
                st.text_input("Task Name", key='task_name_input')
                st.text_area("Task Description", key='task_description_input')
                st.selectbox("Status", ["Not Started", "In Progress", "Completed"], key='task_status_input')
                st.selectbox("Assigned To", [''] + st.session_state['people'], key='task_assigned_to_input')
                st.selectbox("Priority", ['Low', 'Medium', 'High'], key='task_priority_input')
                st.number_input("Estimated Hours", min_value=0.0, step=0.5, key='task_estimate_hours_input')
                st.form_submit_button(label='Add Task', on_click=add_task)

    with st.expander("View Tasks"):
        view_tasks()

    with st.expander("Add New Expense"):
        if st.session_state.get('clear_expense_inputs', False):
            st.session_state.expense_name_input = ''
            st.session_state.expense_cost_input = 0.0
            st.session_state.expense_quantity_input = 0
            st.session_state.clear_expense_inputs = False

        with st.form(key='add_expense_form'):
            st.text_input("Expense Name", key='expense_name_input')
            st.number_input("Cost", min_value=0.0, step=0.01, key='expense_cost_input')
            st.number_input("Quantity", min_value=1, step=1, key='expense_quantity_input')
            st.form_submit_button(label='Add Expense', on_click=add_expense)

    with st.expander("View Expenses"):
        view_expenses()

    with st.expander("Export Data"):
        projects_csv, tasks_csv, expenses_csv = export_data()
        st.download_button(label="Download Projects CSV", data=projects_csv, file_name='projects.csv', mime='text/csv')
        st.download_button(label="Download Tasks CSV", data=tasks_csv, file_name='tasks.csv', mime='text/csv')
        st.download_button(label="Download Expenses CSV", data=expenses_csv, file_name='expenses.csv', mime='text/csv')

if __name__ == "__main__":
    main()
