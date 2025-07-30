import streamlit as st
import pandas as pd

# Initialize session state for creator data
if "creators" not in st.session_state:
    st.session_state.creators = pd.DataFrame(columns=[
        "Name", "Status", "Email", "Location", "Platform", "Verticals", 
        "Audience Demographics", "Preferred Brands", "Avoided Brands", "Notes"
    ])

# App title
st.title("Creator & Prospect Roster Manager")

# Sidebar for adding a new creator or prospect
st.sidebar.header("Add New Entry")
with st.sidebar.form("add_creator"):
    name = st.text_input("Name")
    status = st.selectbox("Status", ["Creator", "Prospect", "Archived"])
    email = st.text_input("Email")
    location = st.text_input("Location")
    platform = st.text_input("Platform (YouTube, TikTok, etc.)")
    verticals = st.text_input("Verticals (comma-separated)")
    audience = st.text_input("Audience Demographics")
    preferred = st.text_input("Preferred Brand Types")
    avoided = st.text_input("Avoided Brand Types")
    notes = st.text_area("Notes")
    submitted = st.form_submit_button("Add")

    if submitted and name:
        new_entry = {
            "Name": name,
            "Status": status,
            "Email": email,
            "Location": location,
            "Platform": platform,
            "Verticals": verticals,
            "Audience Demographics": audience,
            "Preferred Brands": preferred,
            "Avoided Brands": avoided,
            "Notes": notes
        }
        st.session_state.creators = pd.concat(
            [st.session_state.creators, pd.DataFrame([new_entry])],
            ignore_index=True
        )
        st.success(f"{name} added successfully!")

# Main view: display the roster table
st.header("Current Roster")
st.dataframe(st.session_state.creators, use_container_width=True)

# Export to CSV
st.download_button(
    label="Download CSV",
    data=st.session_state.creators.to_csv(index=False),
    file_name="creator_roster.csv",
    mime="text/csv"
)
