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
def get_firebase_connection():
    cred = credentials.Certificate(rf"C:\Users\naveen.koyada\Downloads\{project}.json")
    app = firebase_admin.initialize_app(cred)

    # Initialize Firestore
    db = firestore.client(app)
    print(db)

st.session_state.step1_done = True

if st.session_state.step1_done:
    st.write("firebase initialised")

    st.title("Add Report Details to Firestore")

    default_values = {
        "dashboardName": "partner insights",
        "dashboardNumber": 1,
        "dashboardUid": "partner-insights"
    }

    dashboardName = st.text_input("Dashboard Name:", default_values["dashboardName"])
    dashboardNumber = st.text_input("Dashboard Number:", default_values["dashboardNumber"])
    dashboardUid = st.text_input("Dashboard Uid:", default_values["dashboardUid"])
    st.session_state.step2_done = True

if st.session_state.step2_done and st.button("Update/Add Report Details"):
    dashboard_data = {
        "dashboardName": dashboardName,
        "dashboardNumber": dashboardNumber,
        "dashboardUid": dashboardUid
    }
    # st.success("Dashboard details saved successfully!")
    st.session_state.step3_done = True

if st.session_state.step3_done:
    st.title("Add Page Details to Firestore")

    # Default values (Modify as needed)
    # default_values = {
    #     "pageName": "",
    #     "pageNumber": 1,
    #     "pageUid": "",
    #     "path": "/",
    #     "depth": 1,
    #     "iconName": "",
    #     "parent": "",
    # }

    # Create input fields
    page_name = st.text_input("Page Name:", "")
    page_number = st.number_input("Page Number:", min_value=1, value=1)
    pageUid = st.text_input("Page Uid:", "")
    path = st.text_input("Path:", "/")
    depth = st.number_input("Depth:", min_value=0, value=1)
    icon_name = st.text_input("Icon Name:", "")
    parent = st.text_input("Parent:", None)

    #     # Submit Button
    if st.button("Insert Page Details"):
    #         # Create dictionary for Firestore
        page_data = {
            "pageName": page_name,
            "pageNumber": page_number,
            "path": path,
            "depth": depth,
            "iconName": icon_name,
            "parent": parent,
        }
#
#         # Store in Firestore under "pages" collection
        db.collection("pages").document(page_name).set(page_data)
        st.write(page_data)

    #
    #         # st.success("Page details saved successfully!")
    #
        st.title("Add Visualization Details to Firestore")
    #
    #         default_vis_values = {
    #             "visName": "",
    #             "visPageUid": "",
    #             "visUid": ""
    #         }
    #         #
    #         visName = st.text_input("Vis Name:", default_vis_values["visName"])
    #         visPageUid = st.text_input("Vis Page Uid:", default_vis_values["visPageUid"])
    #         visUid = st.text_input("Vis Uid:", default_vis_values["visUid"])
    #
    #         if st.button("Insert Visualization Details"):
    #             visualizations = {
    #                 "visName": visName,
    #                 "visPageUid": visPageUid,
    #                 "visUid": visUid
    #             }
    #
    #             st.write(visualizations)
    #
    #             # st.success("Dashboard details saved successfully!")
    #
    #             # Upload data to Firestore
    #             dashboard_ref = db.collection("dashboards").document(dashboardUid)
    #             dashboard_ref.set({
    #                 "dashboardName": dashboardName,
    #                 "dashboardNumber": dashboardNumber,
    #                 "dashboardUid": dashboardUid
    #             })
    #
    #             # print(data["pages"])
    #
    #             # Add pages as sub-collection
    #             pages_ref = dashboard_ref.collection("pages")
    #             page_ref = pages_ref.document("pageUid")
    #             page_ref.set({
    #                 "pageName": page_name,
    #                 "pageNumber": page_number,
    #                 "depth": depth,
    #                 "iconName": icon_name,
    #                 "parent": parent,
    #                 "path": path,
    #                 "visualizations": {"visName": visName,
    #                                    "visPageUid": visPageUid,
    #                                    "visUid": visUid}
    #                 })
    #
    # print("Data successfully uploaded to Firestore! 🚀")
    #
    # st.write("Data successfully uploaded to Firestore! 🚀")
    #
firebase_admin.delete_app(app)
st.success("Page details saved successfully!")