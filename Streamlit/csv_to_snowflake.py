# import streamlit as st
# import pandas as pd
# import snowflake.connector
#
# # Snowflake connection function
# def get_snowflake_connection():
#     return snowflake.connector.connect(
#         user="Naveen",
#         password="Hyderabad@123",
#         account="up72233.ap-south-1",
#         warehouse="DBT_COMPUTE_WH",
#         database="EDW",
#         schema="DATA_MODEL"
#     )
#
# # Streamlit UI
# # st.title("Upload CSV to Snowflake Internal Stage")
# #
# # uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
# #
# if True:
# # if uploaded_file is not None:
# #     # Save file temporarily
#     temp_file_path = f"temp_uploaded_file.csv"
# #     with open(temp_file_path, "wb") as f:
# #         f.write(uploaded_file.getbuffer())
#
#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()
#     print(cur, '\n' ,conn)
#     # Create an internal stage if not exists
#     stage_name = "my_internal_stage"
#     cur.execute(f"USE ROLE DBT_DEV;")
#     cur.execute(f"USE WAREHOUSE DBT_COMPUTE_WH;")
#     cur.execute(f"USE SCHEMA EDW.DATA_MODEL;")
#     cur.execute(f"CREATE STAGE IF NOT EXISTS {stage_name}")
#
#     cur.execute(f"LIST @{stage_name};")
#     # df = cur.execute(f"LIST @{stage_name};")
#         #
#         # Upload the file to the internal stage
#
#     print(temp_file_path)
#     put_query = f"PUT file://{temp_file_path} @{stage_name}"
#     cur.execute(put_query)
#     #
#     # query_id = cur.sfqid
#     # cur.get_results_from_sfqid(query_id)
#     results = cur.fetchall()
#     print(f"{results[0]}")
#     # st.write(results)
#
#     create_table_query = f"CREATE OR REPLACE TABLE TEST_STREAMLIT_LOAD AS (SELECT * FROM @my_internal_stage/{temp_file_path+'.gz'});"
#     cur.execute(create_table_query)
#
#     query_id = cur.sfqid
#     cur.get_results_from_sfqid(query_id)
#     results = cur.fetchall()
#     print(f"{results}")
#
#     # st.success(f"File successfully uploaded to Snowflake internal stage: {stage_name}")
#
#     # Close connection
#     cur.close()
#     conn.close()
#

import streamlit as st
import pandas as pd
from snowflake.snowpark import Session
import time
# import chardet

connection_parameters = {
        "user" : "Naveen",
        "password" : "Hyderabad@123",
        "account" : "up72233.ap-south-1",
        "warehouse" : "DBT_COMPUTE_WH",
        "database" : "EDW",
        "schema" : "DATA_MODEL"}


# def detect_encoding(file_path):
#     with open(file_path, 'rb') as file:
#         detector = chardet.universaldetector.UniversalDetector()
#         for line in file:
#             detector.feed(line)
#             if detector.done:
#                 break
#         detector.close()
#     return detector.result['encoding']

with st.spinner("Initializing Snowflake session..."):
    time.sleep(1)
    session = Session.builder.configs(connection_parameters).create()
    st.session_state["session"] = session  # Store session in session_state
# File Uploader
    file = st.file_uploader("Drop your CSV here to load to Snowflake", type=["csv"])

    if file is not None:
        st.session_state["uploaded_file"] = file  # Store file in session_state
        st.success("File uploaded successfully! Now click 'Load File to Snowflake'.")
        # encoding = detect_encoding(file)
        # st.write(f"The encoding of the file is: {encoding}")

# Step 2: Load File to Snowflake
if st.button("Load File to Snowflake"):
    with st.spinner("Processing... Please wait."):
        time.sleep(1)

        file = st.session_state["uploaded_file"]
        file_df = pd.read_csv(file)
        table_name = '_'.join(((file.name).split('.'))[0:-2])
        st.write(table_name)

        session = st.session_state["session"]
        session.sql("USE ROLE DBT_DEV;").collect()
        session.sql("USE SCHEMA EDW.DATA_MODEL;").collect()

        snowpark_df = session.write_pandas(file_df, table_name, auto_create_table=True, overwrite=True)
        st.write(snowpark_df)

        st.success("File successfully loaded to Snowflake!")

# if st.button("Start Process"):
#     with st.spinner("Processing... Please wait."):
#         time.sleep(1)  # Simulating some intermediate step
#         session = Session.builder.configs(connection_parameters).create()
#         file = st.file_uploader("Drop your CSV here to load to Snowflake", type={"csv"})
#         if st.button("Load File to Snowflake"):
#             with st.spinner("Processing... Please wait."):
#                 time.sleep(1)
#                 file_df = pd.read_csv(file)
#                 session.sql("USE ROLE DBT_DEV;").collect()
#                 session.sql("USE SCHEMA EDW.DATA_MODEL;").collect()
#                 snowpark_df = session.write_pandas(file_df, file.name, auto_create_table=True, overwrite=True)
#                 st.write(snowpark_df)
    # st.success("Successfully uploaded file!")
    #     st.success("Successfully loaded file to snowflake!")
# session = Session.builder.configs(connection_parameters).create()
# file = st.file_uploader("Drop your CSV here to load to Snowflake", type={"csv"})
# file_df = pd.read_csv(file)
# session.sql("USE ROLE DBT_DEV;").collect()
# session.sql("USE SCHEMA EDW.DATA_MODEL;").collect()
# snowpark_df=session.write_pandas(file_df,file.name,auto_create_table = True, overwrite=True)
# st.write(snowpark_df)