# Creator Roster Management App

This Streamlit app helps manage your YouTube/TikTok creator and prospect roster. Use it to track key demographics, content verticals, preferred/avoided brand categories, and export to CSV.

## Features

- Add/remove creators or prospects
- Store audience and brand preference data
- Capture preferred and avoided brand categories
- Tag creators by verticals and demographics
- Filter entries by verticals or brand categories
- Export roster as CSV
- Prospects and creators displayed in separate tables
- Edit roster entries directly in the tables
- Save edits using the **Save Changes** button
- Data is loaded from and saved to `creator_data.csv`
- Match creators to brand deal descriptions

## Run Locally

1. Clone this repo:
```bash
git clone https://github.com/your-username/creator_roster_app.git
cd creator_roster_app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the app:
```bash
streamlit run app.py
```

## Deploy on Streamlit Cloud

1. Push the folder to a GitHub repository.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) and connect your GitHub.
3. Select the repo and deploy `app.py`.

---

Created by Rachel Martin.
