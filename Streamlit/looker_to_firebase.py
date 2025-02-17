import streamlit as st

st.title("Add Dashboard Details to Firestore")

default_values = {
    "dashboardName": "partner insights",
    "dashboardNumber": 1,
    "dashboardUid": "partner-insights"
}

dashboardName = st.text_input("Dashboard Name:", default_values["dashboardName"])
dashboardNumber = st.text_input("Dashboard Number:", default_values["dashboardNumber"])
dashboardUid = st.text_input("Dashboard Uid:", default_values["dashboardUid"])

if st.button("Insert Dashboard Details"):
    dashboard_data = {
        "dashboardName": dashboardName,
        "dashboardNumber": dashboardNumber,
        "dashboardUid": dashboardUid
    }

    st.success("Dashboard details saved successfully!")

st.title("Add Page Details to Firestore")

# Default values (Modify as needed)
default_values = {
    "pageName": "Default Page Name",
    "pageNumber": 1,
    "path": "/default_path",
    "depth": 1,
    "iconName": "default_icon",
    "parent": "default_parent",
}

# Create input fields
page_name = st.text_input("Page Name:", default_values["pageName"])
page_number = st.number_input("Page Number:", min_value=1, value=default_values["pageNumber"])
path = st.text_input("Path:", default_values["path"])
depth = st.number_input("Depth:", min_value=0, value=default_values["depth"])
icon_name = st.text_input("Icon Name:", default_values["iconName"])
parent = st.text_input("Parent:", default_values["parent"])

# Submit Button
if st.button("Insert Page Details"):
    page_data = {
        "pageName": page_name,
        "pageNumber": page_number,
        "path": path,
        "depth": depth,
        "iconName": icon_name,
        "parent": parent
    }
    # Create dictionary for Firestore

    # Store in Firestore under "pages" collection
    # db.collection("pages").document(page_name).set(page_data)

    st.success("Page details saved successfully!")
st.write(page_name)