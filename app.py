import streamlit as st
import pandas as pd
import re


def match_creators(description: str, df: pd.DataFrame, top_n: int = 5) -> pd.DataFrame:
    """Return top matching creators based on keyword overlap."""
    if not description:
        return pd.DataFrame()

    words = set(re.findall(r"\w+", description.lower()))

    def score_row(row: pd.Series) -> int:
        text = " ".join(
            [
                str(row.get("Verticals", "")),
                str(row.get("Audience Demographics", "")),
                str(row.get("Preferred Brands", "")),
                str(row.get("Notes", "")),
            ]
        ).lower()
        row_words = set(re.findall(r"\w+", text))
        return len(words & row_words)

    df = df.copy()
    df["MatchScore"] = df.apply(score_row, axis=1)
    df = df.sort_values("MatchScore", ascending=False)
    df = df[df["MatchScore"] > 0]
    return df.head(top_n)[
        ["Name", "Status", "MatchScore", "Verticals", "Preferred Brands"]
    ]

# Initialize session state for creator data
if "creators" not in st.session_state:
    columns = [
        "Name",
        "Status",
        "Email",
        "Location",
        "Platform",
        "Channel URL",
        "Monthly Views (Long Form)",
        "Verticals",
        "Audience Demographics",
        "Preferred Brands",
        "Avoided Brands",
        "Notes",
    ]
    st.session_state.creators = pd.DataFrame(columns=columns)

    prospect_data = [
        {
            "Name": "Addy Harajuku",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@AddyHarajuku",
            "Monthly Views (Long Form)": 497200,
        },
        {
            "Name": "Andertons Music Co",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@andertons",
            "Monthly Views (Long Form)": 3200000,
        },
        {
            "Name": "Brianna Mizura",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@briannamizura",
            "Monthly Views (Long Form)": 5900000,
        },
        {
            "Name": "Hazelnuttygames",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@Hazelnuttygames",
            "Monthly Views (Long Form)": 263800,
        },
        {
            "Name": "HopeScope",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@hopescope",
            "Monthly Views (Long Form)": 32600000,
        },
        {
            "Name": "Jay Diggs",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@jaydiggsmusic",
            "Monthly Views (Long Form)": 1800000,
        },
        {
            "Name": "Emmas Rectangle",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@EmmasRectangle",
            "Monthly Views (Long Form)": 61700,
        },
        {
            "Name": "Nobbel87",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@Nobbel87",
            "Monthly Views (Long Form)": 503800,
        },
        {
            "Name": "Omar Nova",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@OmarNovaVideos",
            "Monthly Views (Long Form)": 598000,
        },
        {
            "Name": "penguinz0",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@penguinz0",
            "Monthly Views (Long Form)": 151500000,
        },
        {
            "Name": "Platinum WoW",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@PlatinumWoW",
            "Monthly Views (Long Form)": 969600,
        },
        {
            "Name": "Rhett Shull",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@RhettShull",
            "Monthly Views (Long Form)": 1500000,
        },
        {
            "Name": "Tonio Guajardo",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@TonioGuajardo",
            "Monthly Views (Long Form)": 4400000,
        },
        {
            "Name": "drewdoes",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@imdrewdoes",
            "Monthly Views (Long Form)": 2600000,
        },
        {
            "Name": "Julian Lopez",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/channel/UCnfakL65DOJJubZj469O3pA/about",
            "Monthly Views (Long Form)": 943800,
        },
        {
            "Name": "Cadel and Mia",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/channel/UCGvGMmyEWp9hxDqmfLJbpkQ",
            "Monthly Views (Long Form)": 2500000,
        },
        {
            "Name": "HOPPER",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/channel/UCCip9ix58vFFTo_Nm1ZFmOw",
            "Monthly Views (Long Form)": 2900000,
        },
        {
            "Name": "Andrey Grechka",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/channel/UC6ABNFIGTdN41wC-PccaIKA",
            "Monthly Views (Long Form)": 1300000,
        },
        {
            "Name": "andr3w_wave",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/channel/UCcTNZCkgOrBE_YeATCQ1LsQ",
            "Monthly Views (Long Form)": 123800,
        },
        {
            "Name": "Courtney & Alex",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/channel/UCC1oaRFc9jkPevIOHf2qbpw",
            "Monthly Views (Long Form)": 1400000,
        },
        {
            "Name": "IShowSpeed",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@IShowSpeed",
            "Monthly Views (Long Form)": 88700000,
        },
        {
            "Name": "Brent Rivera",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/channel/UC56D-IHcUvLVFTX_8NpQMXg",
            "Monthly Views (Long Form)": 81300000,
        },
        {
            "Name": "Sofi Manassyan",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@SofiManassyan/videos",
            "Monthly Views (Long Form)": 2500000,
        },
        {
            "Name": "Futcrunch",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@futcrunch/",
            "Monthly Views (Long Form)": 41900000,
        },
        {
            "Name": "Tyler Vitelli",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@tyler.vitelli",
            "Monthly Views (Long Form)": 6700000,
        },
        {
            "Name": "Daquavis",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@DaquavisMC",
            "Monthly Views (Long Form)": 11600000,
        },
        {
            "Name": "Jojo Sim",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/channel/UChK6a3Ro3po3fUfAm3_MyUQ",
            "Monthly Views (Long Form)": 295600,
        },
        {
            "Name": "Mini Katana",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@MiniKatanaStore/",
            "Monthly Views (Long Form)": 798200,
        },
        {
            "Name": "Nizarisaqt",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@Nizarisacutie",
            "Monthly Views (Long Form)": 33800000,
        },
        {
            "Name": "Josh Brett",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@brettjosh",
            "Monthly Views (Long Form)": 1100000,
        },
        {
            "Name": "Daniel Phillips",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@danphillipss",
            "Monthly Views (Long Form)": 2100000,
        },
        {
            "Name": "SuprOrdinary",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@SuprOrdinary/",
            "Monthly Views (Long Form)": 48300,
        },
        {
            "Name": "JustAli",
            "Status": "Prospect",
            "Channel URL": "https://www.youtube.com/@JustAli",
            "Monthly Views (Long Form)": 418900,
        },
        {
            "Name": "Eeowna",
            "Status": "Creator",
            "Channel URL": "",
            "Monthly Views (Long Form)": 0,
        },
        {
            "Name": "Pencilmation",
            "Status": "Creator",
            "Channel URL": "",
            "Monthly Views (Long Form)": 0,
        },
        {
            "Name": "TaylorR1488",
            "Status": "Creator",
            "Channel URL": "",
            "Monthly Views (Long Form)": 0,
        },
        {
            "Name": "Jaclyn Glenn",
            "Status": "Creator",
            "Channel URL": "",
            "Monthly Views (Long Form)": 0,
        },
        {
            "Name": "Kat Buno",
            "Status": "Creator",
            "Channel URL": "",
            "Monthly Views (Long Form)": 0,
        },
    ]

    st.session_state.creators = pd.concat(
        [st.session_state.creators, pd.DataFrame(prospect_data)],
        ignore_index=True,
    )

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
    channel_url = st.text_input("Channel URL")
    monthly_views = st.number_input(
        "Monthly Views (Long Form)",
        value=0,
        step=1,
        format="%d",
    )
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
            "Channel URL": channel_url,
            "Monthly Views (Long Form)": monthly_views,
            "Verticals": verticals,
            "Audience Demographics": audience,
            "Preferred Brands": preferred,
            "Avoided Brands": avoided,
            "Notes": notes,
        }
        st.session_state.creators = pd.concat(
            [st.session_state.creators, pd.DataFrame([new_entry])],
            ignore_index=True,
        )
        st.success(f"{name} added successfully!")

# Main view: display creators and prospects separately
creators_df = st.session_state.creators

st.header("Creator Roster")
creator_idx = creators_df[creators_df["Status"] == "Creator"].index
edited_creators = st.data_editor(
    creators_df.loc[creator_idx],
    num_rows="dynamic",
    use_container_width=True,
    key="creator_table",
)
st.session_state.creators.loc[creator_idx] = edited_creators

st.header("Prospect Roster")
prospect_idx = creators_df[creators_df["Status"] == "Prospect"].index
edited_prospects = st.data_editor(
    creators_df.loc[prospect_idx],
    num_rows="dynamic",
    use_container_width=True,
    key="prospect_table",
)
st.session_state.creators.loc[prospect_idx] = edited_prospects

# Export to CSV
st.download_button(
    label="Download CSV",
    data=creators_df.to_csv(index=False),
    file_name="creator_roster.csv",
    mime="text/csv",
)

# Brand deal matcher section
st.header("Brand Deal Matcher")
deal_description = st.text_area("Paste brand deal description")
if st.button("Analyze Fit"):
    matches = match_creators(deal_description, creators_df)
    if matches.empty:
        st.info("No suitable creators found.")
    else:
        st.dataframe(matches, use_container_width=True)
