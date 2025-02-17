import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st

cred = credentials.Certificate(rf"C:\Users\naveen.koyada\Downloads\sample-firebase-automation.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()
print(db)

data = {
    "dashboardUid": "partners-insight",
    "dashboardName": "Partner Insights",
    "dashboardNumber": 3,
    "pages": [
        {
            "pageUid": "partner_insights_0_0",
            "pageName": "CCJ",
            "pageNumber": 1,
            "depth": 0,
            "iconName": None,
            "parent": None,
            "path": "",
            "visualizations": None
        },
        {
            "pageUid": "partner_insights_1_0",
            "pageName": "Valvoline",
            "pageNumber": 1,
            "depth": 1,
            "iconName": None,
            "parent": "partner_insights_0_0",
            "path": "",
            "visualizations": None
        },
        {
            "pageUid": "partner_insights_1_1",
            "pageName": "Ecosystem Insights",
            "pageNumber": 1,
            "depth": 2,
            "iconName": None,
            "parent": "partner_insights_1_0",
            "path": "/partner_insights_1_1",
            "visualizations": [
                {
                    "visName": "Ecosystem Insights",
                    "visPageUid": "ugyejk",
                    "visUid": "whrewdbsewgt23t52ew325tfe"
                }
            ]
        },
        {
            "pageUid": "partner_insights_1_2",
            "pageName": "Ecosystem Insights 2",
            "pageNumber": 2,
            "depth": 2,
            "iconName": None,
            "parent": "partner_insights_1_0",
            "path": "/partner_insights_1_2",
            "visualizations": [
                {
                    "visName": "Ecosystem Insights 2",
                    "visPageUid": "egvwv",
                    "visUid": "dwetgwewtegw-45ccw4yeh-3y4yrhxed43"
                }
            ]
        },
    ]
}

# Upload data to Firestore
dashboard_ref = db.collection("dashboards").document(data["dashboardUid"])
dashboard_ref.set({
    "dashboardName": data["dashboardName"],
    "dashboardNumber": data["dashboardNumber"],
    "dashboardUid": data["dashboardUid"]
})

print(data["pages"])

# Add pages as sub-collection
pages_ref = dashboard_ref.collection("pages")
for page in data["pages"]:
    print(page)
    page_ref = pages_ref.document(page["pageUid"])
    page_ref.set({
        "pageName": page["pageName"],
        "pageNumber": page["pageNumber"],
        "depth": page["depth"],
        "iconName": page["iconName"],
        "parent": page["parent"],
        "path": page["path"],
        "visualizations": page["visualizations"]
    })

print("Data successfully uploaded to Firestore! 🚀")



















#
# dashboard_ref = db.collection("dashboards").document("partners-insight")
# dashboard_ref.set({
#     "dashboardName": "Partner Insights",
#     "dashboardNumber": 3,
#     "dashboardUid": "partners-insight"
# })
#
# # Add multiple documents to 'pages' sub-collection
# pages_ref = dashboard_ref.collection("pages")
#
# pages_data = [
#     {"pageUid": "partner_insights_0"},
#     {"pageUid": "partner_insights_1_0"},
#     {"pageUid": "partner_insights_1_1"},
#     {"pageUid": "partner_insights_7_1"}
# ]
#
# for page in pages_data:
#     pages_ref.document(page["pageUid"]).set(page)
#
# # Add sub-collection 'visualizations' under 'partner_insights_7_1'
# visualizations_ref = pages_ref.document("partner_insights_7_1").collection("partner_insights_7_1")
#
# visualizations_ref.add({"depth": 2,
#                         "pageName": "Ecosystem Insights",
#                         "parent": "partner_insights_7_0",
#                         "visualizations": {"visName": "Ecosystem Insights",
#                                                "visPageUid": "y54u6u5y4wefa",
#                                                "visUid": "wgrhtjy456ytewqeertyuk"}})