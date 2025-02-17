import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

def get_project():
    st.title("Select you Project")
    project_options = ["sample-firebase-automation", "second-project-automation"]
    project = st.selectbox("Select your Project:", project_options, index=0)
    return project

# ------- Firebase starts here
# ----Firebase connection
def get_firebase_connection(project):
    cred = credentials.Certificate(rf"C:\Users\naveen.koyada\Downloads\{project}.json")
    app = firebase_admin.initialize_app(cred)
    # Initialize Firestore
    db = firestore.client(app)
    return db, app

# st.session_state.step1_done = True

def get_dashboards():
    default_values = {
        "dashboardName": "partner insights",
        "dashboardNumber": 1,
        "dashboardUid": "partner-insights"
    }

    dashboardName = st.text_input("Dashboard Name:", default_values["dashboardName"])
    dashboardNumber = st.text_input("Dashboard Number:", default_values["dashboardNumber"])
    dashboardUid = st.text_input("Dashboard Uid:", default_values["dashboardUid"])

    dashboard_data = {
        "dashboardName": dashboardName,
        "dashboardNumber": dashboardNumber,
        "dashboardUid": dashboardUid
    }

    return dashboard_data

def get_vis_pages():
    page_name = st.text_input("Page Name:", "")
    page_number = st.number_input("Page Number:", min_value=1, value=1)
    pageUid = st.text_input("Page Uid:", "")
    path = st.text_input("Path:", "/")
    depth = st.number_input("Depth:", min_value=0, value=1)
    icon_name = st.text_input("Icon Name:", "")
    parent = st.text_input("Parent:", None)
    visName = st.text_input("Vis Name:", "")
    visPageUid = st.text_input("Vis Page Uid:", "")
    visUid = st.text_input("Vis Uid:", "")

    vis_page_data = {
        "pageName": page_name,
        "pageNumber": page_number,
        "path": path,
        "depth": depth,
        "iconName": icon_name,
        "parent": parent,
        "visualizations": {
            "visName": visName,
            "visPageUid": visPageUid,
            "visUid": visUid
        }
    }

    return vis_page_data

def close_firebase(app):
    firebase_admin.delete_app(app)


if st.button("start process"):
    st.session_state = "start process"
    if st.session_state == "start process":
        project = get_project()
        db, app = get_firebase_connection(project)
        st.session_state = "connected to firebase"
        st.write("Update/Add Dashboard Details:")
        dashboards = get_dashboards()
        st.write("Update/Add Page Details:")
        if st.session_state == "connected to firebase":
            pages = get_vis_pages()
            st.session_state = "connected to firebase"
        if st.session_state == "connected to firebase" and st.button("dashboards"):
            st.write("firebase initialised")
            # dashboards = get_dashboards()
            dashboard_ref = db.collection("dashboards").document(dashboards["dashboardUid"])
            dashboard_ref.set(dashboards)
            st.write(dashboards)
            st.session_state = "dashboard details updated"
            if st.session_state == "dashboard details updated" and st.button("pages"):
                # pages = get_vis_pages()
                db.collection("pages").document(pages["pageName"]).set(pages)
                st.write(pages)
    st.success("Page details saved successfully!")
    close_firebase(app)