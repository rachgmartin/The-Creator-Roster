import streamlit as st
import pandas as pd
import re
import os

def _split_tags(text) -> list[str]:
    """Return a list of tags from a user provided string."""
    if text is None or pd.isna(text) or str(text).strip() == "":
        return []
    tags = re.split(r"[\n,]+", str(text))
    return [t.strip() for t in tags if t.strip()]


def _tags_to_display(text: str) -> str:
    """Convert a tag string into a bracketed display format."""
    return " ".join(f"[{t}]" for t in _split_tags(text))


def _normalize_tags(text: str) -> str:
    """Normalize a tag input into a comma separated string."""
    return ", ".join(_split_tags(text))

DATA_FILE = "creator_data.csv"


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
                str(row.get("Avoided Brands", "")),
                str(row.get("Preferred Brand Categories", "")),
                str(row.get("Avoided Brand Categories", "")),
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
        [
            "Name",
            "Status",
            "MatchScore",
            "Verticals",
            "Preferred Brands",
            "Preferred Brand Categories",
            "Avoided Brand Categories",
        ]
    ]

# Initialize session state for creator data
if "creators" not in st.session_state:
    if os.path.exists(DATA_FILE):
        st.session_state.creators = pd.read_csv(DATA_FILE)
        for col in [
            "Preferred Brand Categories",
            "Avoided Brand Categories",
        ]:
            if col not in st.session_state.creators.columns:
                st.session_state.creators[col] = ""
    else:
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
            "Preferred Brand Categories",
            "Avoided Brand Categories",
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
    verticals = st.text_area(
        "Verticals",
        help="Press Enter or use commas to separate multiple entries",
    )
    audience = st.text_input("Audience Demographics")
    preferred = st.text_input("Preferred Brands")
    avoided = st.text_input("Avoided Brands")
    preferred_cat = st.text_area(
        "Preferred Brand Categories",
        help="Press Enter or use commas to separate multiple entries",
    )
    avoided_cat = st.text_area(
        "Avoided Brand Categories",
        help="Press Enter or use commas to separate multiple entries",
    )
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
            "Verticals": _normalize_tags(verticals),
            "Audience Demographics": audience,
            "Preferred Brands": preferred,
            "Avoided Brands": avoided,
            "Preferred Brand Categories": _normalize_tags(preferred_cat),
            "Avoided Brand Categories": _normalize_tags(avoided_cat),
            "Notes": notes,
        }
        st.session_state.creators = pd.concat(
            [st.session_state.creators, pd.DataFrame([new_entry])],
            ignore_index=True,
        )
        st.session_state.creators.to_csv(DATA_FILE, index=False)
        st.success(f"{name} added successfully!")

# Main view: display creators and prospects separately
creators_df = st.session_state.creators

# Sidebar filters
st.sidebar.header("Filters")

def _get_tag_options(df: pd.DataFrame, column: str) -> list[str]:
    opts = set()
    for cell in df[column].dropna():
        opts.update(_split_tags(str(cell)))
    return sorted(opts)

vertical_opts = _get_tag_options(creators_df, "Verticals")
pref_cat_opts = _get_tag_options(creators_df, "Preferred Brand Categories")
avoid_cat_opts = _get_tag_options(creators_df, "Avoided Brand Categories")

selected_verticals = st.sidebar.multiselect("Verticals", vertical_opts)
selected_pref_cats = st.sidebar.multiselect(
    "Preferred Brand Categories", pref_cat_opts
)
selected_avoid_cats = st.sidebar.multiselect(
    "Avoided Brand Categories", avoid_cat_opts
)

def _row_matches(tags_str: str, selected: list[str]) -> bool:
    if not selected:
        return True
    tags = set(_split_tags(tags_str))
    return set(selected).issubset(tags)

filter_mask = creators_df.apply(
    lambda r: _row_matches(r.get("Verticals", ""), selected_verticals)
    and _row_matches(r.get("Preferred Brand Categories", ""), selected_pref_cats)
    and _row_matches(r.get("Avoided Brand Categories", ""), selected_avoid_cats),
    axis=1,
)

creators_df = creators_df[filter_mask]

st.header("Creator Roster")
creator_idx = creators_df[creators_df["Status"] == "Creator"].index
edited_creators = st.data_editor(
    creators_df.loc[creator_idx],
    num_rows="dynamic",
    use_container_width=True,
    key="creator_table",
)
for col in ["Verticals", "Preferred Brand Categories", "Avoided Brand Categories"]:
    if col in edited_creators.columns:
        edited_creators[col] = edited_creators[col].apply(_normalize_tags)
st.session_state.creators.loc[creator_idx] = edited_creators

st.header("Prospect Roster")
prospect_idx = creators_df[creators_df["Status"] == "Prospect"].index
edited_prospects = st.data_editor(
    creators_df.loc[prospect_idx],
    num_rows="dynamic",
    use_container_width=True,
    key="prospect_table",
)
for col in ["Verticals", "Preferred Brand Categories", "Avoided Brand Categories"]:
    if col in edited_prospects.columns:
        edited_prospects[col] = edited_prospects[col].apply(_normalize_tags)
st.session_state.creators.loc[prospect_idx] = edited_prospects

# Button to save any changes made in the tables
if st.button("Save Changes"):
    st.session_state.creators.to_csv(DATA_FILE, index=False)
    st.success("Changes saved!")

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
